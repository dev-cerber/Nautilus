from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    print('initial ...')
    return render(request, 'first_nav_demo.html')
    # return HttpResponse("Home")
