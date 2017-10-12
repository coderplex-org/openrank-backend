from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    response = HttpResponse("Hello world")
    response["Access-Control-Allow-Origin"] = "*"
    return response
