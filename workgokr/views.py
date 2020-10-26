from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

# Create your views here.

def hello(request):
    return HttpResponse("Hello, Django!")

def workDB(request):
    data = request.GET.copy()
    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        myworkdb=client.saraminDB
        result = list(myworkdb.saraminCollection.find({})) # get Collection with find()
        data['page_obj'] = result
    return render(request, 'board/workdb.html', context=data)

def home(request):
    return render(request, 'home.html')