from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pavani(request):
    return HttpResponse('<marquee><h1><i>my is pavani....</i></h1></marquee><hr>')

def bhumika(request):
    return HttpResponse('<marquee><h1>she is good girl in class</h1></marquee>')

def penchal(request):
    return HttpResponse('<marquee><h1>handsome boy in my life</h1></marquee>')