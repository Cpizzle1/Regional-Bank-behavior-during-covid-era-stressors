
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from functools import reduce
import pandas as pd
import time
import xport

import numpy as np
import matplotlib.pyplot as plt


from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from functools import reduce

import time
import xport

import numpy as np
import matplotlib.pyplot as plt
import re
import requests
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

download_dir = "/Users/cp/Documents/dsi/practice"
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')

# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/cp/Downloads/chromedriver2")

# change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file


# function to handle setting up headless download
download_dir = "/Users/cp/Documents/dsi/practice"


url_bank = "https://www.ffiec.gov/npw/Institution/Profile/1039502?dt=20190519"
url_banks = {

    'JPM':"https://www.ffiec.gov/npw/Institution/Profile/1039502?dt=20190519"
    , 'BAC':"https://www.ffiec.gov/npw/Institution/Profile/1073757?dt=20141231"
    , "C":"https://www.ffiec.gov/npw/Institution/Profile/1951350?dt=20170701"
    ,"WFC":"https://www.ffiec.gov/npw/Institution/Profile/1120754?dt=20200331"
    , 'GS': "https://www.ffiec.gov/npw/Institution/Profile/2380443?dt=20150101"

}