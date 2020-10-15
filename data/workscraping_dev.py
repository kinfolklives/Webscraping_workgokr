from pymongo import MongoClient
import time
import schedule
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

def insertDB(data):
        with MongoClient('mongodb://127.0.0.1:27017/') as client:
                myworkdb = client['mytest']
                myworkdb.test.insert_one(data)

def Scrap():
        path = '/home/rapa01/Documents/Develop/ownproject/data/ch_linux'
        # path = '/workspace/ownproject_01/data/ch_linux'
        with webdriver.Chrome(executable_path=path) as driver:
                url = "https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?keyword=ai"
                # url = "https://www.work.go.kr"
                driver.get(url=url)

                time.sleep(5)

                
list = ['tr', 'a', 'table']
for l in list:
        data = find_all(l)
        if data == ''

keys = ['name', 'title', 'desc']       
for k in keys 

[i*2 for i in range(0,10) if i%2 == 0]