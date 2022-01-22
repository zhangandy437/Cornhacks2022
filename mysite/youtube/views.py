from django.shortcuts import render
from django.http import FileResponse
from random import random
from . import quickstart

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Create your views here.
def index(request):
    filename = quickstart.downloadrandom()
    
