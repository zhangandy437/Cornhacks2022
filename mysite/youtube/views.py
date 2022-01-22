from django.shortcuts import render
from django.http import JsonResponse
from random import random

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Create your views here.
def index(request):
    data = {
        'url': randomyoutube()
    }
    return JsonResponse(data)


def randomyoutube() -> str:
    urls = readTxt()
    return urls[int(random() * len(urls))]

def readTxt():
    f = open('youtube/urls.txt', "r")
    lines = f.read().splitlines()
    f.close()
    return [i.split(' ') for i in lines]


# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python



scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.channels().list(
        
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()