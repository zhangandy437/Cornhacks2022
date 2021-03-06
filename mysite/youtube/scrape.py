import json
from urllib.error import HTTPError, URLError
import requests, re
from bs4 import BeautifulSoup
import urllib.request

import cv2
import matplotlib.pyplot as plt
import skimage
import skimage.feature
import skimage.viewer
from random import random, choice
from PIL import ImageEnhance, Image, UnidentifiedImageError

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "q": "vaporwave",
    "tbm": "isch",
    "ijn": "0",
}

html = requests.get("https://www.google.com/search", params=params, headers=headers)
soup = BeautifulSoup(html.text, 'lxml')

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "q": "minecraft shaders 8k photo",
    "tbm": "isch",
    "ijn": "0",
}

html = requests.get("https://www.google.com/search", params=params, headers=headers)

def augment(imgpath):
    img = cv2.imread(imgpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Fixes color read issue

    img = cv2.imread(imgpath, 0)
    
    edges = skimage.feature.canny(
        image=img,
        sigma=int(random() * 3 + 2),
        low_threshold=2,
        high_threshold=10,
    )

    plt.imshow(edges, interpolation='nearest', aspect='auto')
    plt.xticks([]), plt.yticks([])
    plt.gca().set_axis_off()
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
                hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.savefig(f'{imgpath}au.jpg')
    plt.clf()
    return f'{imgpath}au.jpg'
    # plt.show()

def enhance(imgpath):
    try:
        image = Image.open(imgpath)
    except UnidentifiedImageError:
        return augment(imgpath)
    rgb_im = image.convert('RGB')
    enhancer = ImageEnhance.Color(rgb_im)
    enhancer.enhance(int(random() * 3 + 4)).save(imgpath+'au.jpg')
    return imgpath+'au.jpg'
    
def get_images_data():

    print('\nGoogle Images Metadata:')
    for google_image in soup.select('.isv-r.PNCib.MSM1fd.BUooTd'):
        title = google_image.select_one('.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')['title']
        source = google_image.select_one('.fxgdke').text
        link = google_image.select_one('.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')['href']
        print(f'{title}\n{source}\n{link}\n')

    # this steps could be refactored to a more compact
    all_script_tags = soup.select('script')

    # # https://regex101.com/r/48UZhY/4
    matched_images_data = ''.join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))

    # https://kodlogs.com/34776/json-decoder-jsondecodeerror-expecting-property-name-enclosed-in-double-quotes
    # if you try to json.loads() without json.dumps it will throw an error:
    # "Expecting property name enclosed in double quotes"
    matched_images_data_fix = json.dumps(matched_images_data)
    matched_images_data_json = json.loads(matched_images_data_fix)

    # https://regex101.com/r/pdZOnW/3
    matched_google_image_data = re.findall(r'\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",', matched_images_data_json)

    # https://regex101.com/r/NnRg27/1
    matched_google_images_thumbnails = ', '.join(
        re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',
                   str(matched_google_image_data))).split(', ')

    print('Google Image Thumbnails:')  # in order
    for fixed_google_image_thumbnail in matched_google_images_thumbnails:
        # https://stackoverflow.com/a/4004439/15164646 comment by Fr??d??ric Hamidi
        google_image_thumbnail_not_fixed = bytes(fixed_google_image_thumbnail, 'ascii').decode('unicode-escape')

        # after first decoding, Unicode characters are still present. After the second iteration, they were decoded.
        google_image_thumbnail = bytes(google_image_thumbnail_not_fixed, 'ascii').decode('unicode-escape')
        print(google_image_thumbnail)

    # removing previously matched thumbnails for easier full resolution image matches.
    removed_matched_google_images_thumbnails = re.sub(
        r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', '', str(matched_google_image_data))

    # https://regex101.com/r/fXjfb1/4
    # https://stackoverflow.com/a/19821774/15164646
    matched_google_full_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]",
                                                       removed_matched_google_images_thumbnails)

    out = []
    print('\nFull Resolution Images:')  # in order
    for index, fixed_full_res_image in enumerate(matched_google_full_resolution_images):
        # https://stackoverflow.com/a/4004439/15164646 comment by Fr??d??ric Hamidi
        original_size_img_not_fixed = bytes(fixed_full_res_image, 'ascii').decode('unicode-escape')
        original_size_img = bytes(original_size_img_not_fixed, 'ascii').decode('unicode-escape')
        print(original_size_img)
        try:
            path = f"imgs/{index}.jpg"
            urllib.request.urlretrieve(original_size_img, path)
            out.append(path)
            fun = choice([enhance, augment])
            out.append(fun(path))
        except (HTTPError, URLError) as e:
            print("o well")
    
    return out
# get_images_data()

