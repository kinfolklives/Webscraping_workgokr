from django.shortcuts import render
from pymongo import MongoClient

# Create your views here.
def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        mydb=client.mydb
        result = list(mydb.economic.find({})) # get Collection with find()
        data['page_obj'] = result
    return render(request, 'board/listwithmongo.html', context=data)