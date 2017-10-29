from django.shortcuts import render
from django.http import HttpResponse

def prepareResponse(response):
    # The front end URL has to eventually come from a configuration file to awoid
    # hardcoding in source code
    response["Access-Control-Allow-Origin"] = "*"
    return response

# Create your views here.
def helloworld(request):
    response = HttpResponse("Hello from API Server")
    return prepareResponse(response)


