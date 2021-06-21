from bs4 import BeautifulSoup as BS
from selenium import webdriver
from functools import reduce
import pandas as pd
import time
import xport

import numpy as np
import matplotlib.pyplot as plt


from selenium import webdriver
from selenium.webdriver.common.by import By
from functools import reduce

import time
import xport

import numpy as np
import re
import requests
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options
import os

from bank_variables import url_bank, url_banks, driver 


def enable_download_headless(browser,download_dir):
    
    
    
    
    
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


def auto_bank_csv_downloader(url_banks): 
    

    for k, v in url_banks.items():
        driver.get(v)

        button = driver.find_element(By.XPATH,'//button[@href ="#BHCPR"]');
        button.click()
        time.sleep(10)
    

        search_input=driver.find_element(By.XPATH,'/html/body/div[4]/div[4]/div/div/div/div/div[2]/div/ul/li/span/a');


        search_input.click()

def file_path_maker():

    url_banks = {

    'JPM':"https://www.ffiec.gov/npw/Institution/Profile/1039502?dt=20190519"
    , 'BAC':"https://www.ffiec.gov/npw/Institution/Profile/1073757?dt=20141231"
    , "C":"https://www.ffiec.gov/npw/Institution/Profile/1951350?dt=20170701"
    ,"WFC":"https://www.ffiec.gov/npw/Institution/Profile/1120754?dt=20200331"
    , 'GS': "https://www.ffiec.gov/npw/Institution/Profile/2380443?dt=20150101"

}
    download_dir = "/Users/cp/Documents/dsi/practice"
    bank_csv_file_path = []
    bank_csv_file_path_dct = {}
    for k, v in url_banks.items():
        pattern = "https://www.ffiec.gov/npw/Institution/Profile/(.*?)\?dt="
        substring = re.search(pattern, v).group(1) 
        print (substring)
        final_name = f'BHCPR_{substring}_20201231.csv'
        print(final_name)
        file_path = download_dir+final_name
        print(file_path)
        bank_csv_file_path.append(file_path)
        bank_csv_file_path_dct[k] = file_path
    print(bank_csv_file_path)
    print(bank_csv_file_path_dct)
    return bank_csv_file_path_dct

if __name__ == "__main__":
    download_dir = "/Users/cp/Documents/dsi/practice"

  



    # tcbi = pd.read_csv("/Users/cp/Documents/dsi/capstone1/data/BHCPR_2706735_20200930.csv", index_col='ItemName' )
    # tcbi2 = bank(tcbi, 'tcbi')
    # tcbi2.assets()
    
    
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/cp/Downloads/chromedriver2")
    auto_bank_csv_downloader(url_banks)

    # print(file_path_maker())



    # enable_download_headless(driver, download_dir)