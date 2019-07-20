from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

#launch url
url = 'https://www.takealot.com/4est-shades-wooden-polarized-sunglasses-brown-bamboo/PLID48111025'

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)


#Selenium hands the page source to Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')

print(soup.prettify())