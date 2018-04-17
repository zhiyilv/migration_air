import requests as rq
from bs4 import BeautifulSoup as bs
from selenium import webdriver


url = 'https://hub.hku.hk/cris/dataset/dataset107483#files'
chm = webdriver.Chrome()
chm.get(url)

files_button = chm.find_element_by_link_text('Files')
files_button.click()

data_buttons = chm.find_elements_by_partial_link_text('.zip')

for b in data_buttons:
    b.click()

