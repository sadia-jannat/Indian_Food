from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import date

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#add first create
from django.contrib import admin
from indiafood import views
#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
#query ar jonno
from django.db.models import Q

#django.db.model all item need for use
from django.db.models import Avg, Max, Min, Count
#from numpy import product
#google map ar jonno
#from __future__ import division
from multiprocessing import context
from turtle import color
from unittest import result
from django.db.models import Q
import json
# all models and forms name add korar jonno * use kora jay
from .models import *

def SearchFood(request):
    food=Food.objects.all()
    mainfood=Food.objects.all()
  
    if request.method == 'GET':
        query = request.GET.get('query')
        if query :
            food = Food.objects.filter(name__icontains=query).order_by('name') 
            
    return render(request, 'index.html', {'food':food,'mainfood':mainfood}) 

