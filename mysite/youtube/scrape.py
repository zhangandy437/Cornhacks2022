import requests
from bs4 import BeautifulSoup

def scrape(URL = "https://www.reuters.com/world/middle-east/turkish-journalist-arrested-insulting-erdogan-cnn-turk-2022-01-22/"):
    page = requests.get(URL)
    print('Scraping for images...')
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="fusion-app")
    job_elements = results.find_all("img")
    images = []
    for element in job_elements:
        print(element["src"])
        images.append(element['src'])
    return images