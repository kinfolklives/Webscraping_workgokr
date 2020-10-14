from pymongo import MongoClient
import requests
import time
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

def insertDB(data):
        with MongoClient('mongodb://127.0.0.1:27017/') as client: 
                myworkdb = client['mytest']
                myworkdb.test.insert_one(data)

driver = webdriver.Chrome(executable_path='/home/rapa01/Documents/Develop/chromedriver')
url = "https://www.work.go.kr"
driver.get(url=url)

time.sleep(5) 

search_form = driver.find_element_by_name("topQuery")
search_box = search_form.find_elements_by_css_selector("#topQuery")
search_form.send_keys("AI")
search_bnt = driver.find_element_by_css_selector("#searchFrm > div.header-search > a").click()

names = driver.find_elements_by_css_selector('a[href^="#none"]')
titles = driver.find_elements_by_css_selector('a[onclick^="try"]')

for t in titles:
        title = t.text.split('\n')
        print(title)
# name = [n.text for n in name]

        

driver.quit()
 
# list = ['tr', 'a', 'table']
# for l in list:
#         data = find_all(l)
#         if data == ''

# keys = ['name', 'title', 'desc']       
# for k in keys 

# [i*2 for i in range(0,10) if i%2 == 0]