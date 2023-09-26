from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)
def index(request):
    logger.info('Main page accessed')
    return HttpResponse("""
    <h1>My First Django Project</h1>
    <p>This is my first project, I hope you find it interesting.</p>
    <p>See you later!</p>
    """)

# Create your views here.

def about(response):
    logger.info('About page accessed')
    return HttpResponse("""
        <h1>About me</h1>
        <p>My name is Egor and I am doing my job.</p>
        <p>You can contact me via +445566778899</p>
        """)
