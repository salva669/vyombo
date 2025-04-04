import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def ShowIndexPage(request):
    return render(request, 'index_page.html')

def ShowCookwarePage(request):
    return render(request, 'cookware_page.html')
    
def ShowDinnerwarePage(request):
    return render(request, 'dinnerware_page.html')    