from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def UserHomePage(request):
    response = HttpResponse('wangchen SB')
    HttpResponse.setdefault(response,'header','Access-Control-Allow-Origin')
    return response