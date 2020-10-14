from pymongo import MongoClient
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import schedule
import time

def insertDB(data):
        with MongoClient('mongodb://127.0.0.1:27017/') as client: 
                myworkdb = client['mytest']
                myworkdb.test.insert_one(data)

def Scrap():
        driver = webdriver.Chrome(executable_path='/workspace/ownproject02/data/chromedriver')
        url = "https://www.work.go.kr"
        driver.get(url=url)

        time.sleep(5) 

        search_form = driver.find_element_by_name("topQuery")
        search_box = search_form.find_elements_by_css_selector("#topQuery")
        search_form.send_keys("AI")
        search_bnt = driver.find_element_by_css_selector("#searchFrm > div.header-search > a").click()
        
        for i in range(0, 11):
                data = {}
                try:
                        data['name'] = driver.find_element_by_css_selector(f"#list{i} > td:nth-child(2) > a").text
                        data['title'] = driver.find_element_by_css_selector(f"#list{i} > td:nth-child(3) > div > div > a").text
                        data['desc'] = driver.find_element_by_css_selector(f"#jobContLine{i}").text
                        data['career'] = driver.find_element_by_css_selector(f"#list{i} > td:nth-child(3) > div > p:nth-child(3) > em:nth-child(1)").text
                        data['academic'] = driver.find_element_by_xpath(f'//*[@id="list{i}"]/td[3]/div/p[2]/em[1]').text
                        data['payment'] = driver.find_element_by_css_selector(f"#list{i} > td:nth-child(4) > div > p:nth-child(1) > strong").text
                        data['location'] = driver.find_element_by_css_selector(f"#list{i} > td:nth-child(3) > div > p:nth-child(3) > em:nth-child(3)").text
                        data['d_day1'] = driver.find_element_by_css_selector(f"#dDayInfo{i}").text
                        data['d_day2'] = driver.find_element_by_css_selector(f"#list{i} > td:nth-child(5) > div > p:nth-child(2)").text
                except Exception as e:
                        pass
                
                print(data)
                insertDB(data)
                driver.quit()
                
# schedule.every(12).hours.do(Scrap)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
