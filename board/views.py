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

from board.mongopaginator import MongoPaginator
from django.core.paginator import Paginator
def listwithmongowithpaginator(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/')  as client:
        mydb = client.mydb
        contact_list = list(mydb.economic.find({}))			# get Collection with find()
        for info in contact_list:						# Cursor
            print(info)

    paginator = MongoPaginator(contact_list, 5) # Show 15 contacts per page.

    page_number = request.GET.get('page', 1)
    data['page_obj'] = paginator.get_page(page_number)

    page_obj=data['page_obj']
    for row in page_obj:
        print(f"{row['title']}, {row['link']}")

    return render(request, 'board/listwithmongowithpaginator.html', context=data)