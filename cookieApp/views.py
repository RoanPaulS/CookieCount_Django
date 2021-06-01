from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cookie_Count_View(request):
    count = request.COOKIES.get('counts',0)
    totalCount = int(count) + 1
    response = render(request , 'cookiePage.html' , {'count' : totalCount})
    response.set_cookie('counts',totalCount)
    return response
