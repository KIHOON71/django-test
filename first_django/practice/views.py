from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def TellHello(requests):
    html = "<h1> 식사하러 갑시다 </h2>"
    return HttpResponse(html)