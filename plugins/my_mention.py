from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import requests
import time
import os
import re
import sys
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@respond_to('url')
def mention_func(message):
    message.send("URLを取得中...")
    options = Options()
    options.binary_location = '/usr/bin/google-chrome'
    options.add_argument('--headless')
    driver = webdriver.Chrome(os.path.join(os.getcwd(),'chromedriver'), chrome_options=options)

    driver.implicitly_wait(10)

    driver.get('https://utas.adm.u-tokyo.ac.jp/campusweb/campussquare.do?_flowExecutionKey=_c3D62D42F-9CB0-81FF-7A6F-AC476A308446_kEC46B2DD-6031-5AED-1B0C-4268592673B1')

    #time.sleep(2)

    driver.find_elements_by_class_name("ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")[-1].click()

    #time.sleep(1)

    #########自分のアカウント情報########
    driver.find_element_by_id("userNameInput").send_keys("EMAIL")
    driver.find_element_by_id("passwordInput").send_keys("PASSWORD")
    
    driver.find_element_by_id("submitButton").click()
    driver.find_element_by_id("tab-sy").click()
    

    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[2]/div/div/ul/li[2]/span').click()
    
    driver.switch_to_frame(driver.find_element_by_xpath('/html/body/div[7]/div[2]/table/tbody/tr[4]/td[3]/div/div[1]/iframe'))
    time.sleep(3)

    ########時間割コードを入れる########
    driver.find_element_by_xpath("/html/body/div[2]/div/form/table[2]/tbody/tr[5]/td[3]/input").send_keys("時間割コード")

    driver.find_element_by_xpath("/html/body/div[2]/div/form/table[2]/tbody/tr[7]/td/p/input[1]").click()


    

    driver.find_element_by_xpath("/html/body/table/tbody/tr/td[12]/input").click()



    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element_by_xpath("/html/body/div[2]/ul/li[2]/a").click()
    #time.sleep(2)
    print(driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[26]/td/a/font").text)
    print(driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[27]/td").text)
    text = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[26]/td/a/font").text
    text += '\n'
    text += driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[27]/td").text
    message.send(text)






