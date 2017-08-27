#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
import os
from os.path import expanduser
import time

path =  expanduser("~") +'/' + 'python/chromedriver'
driver = webdriver.Chrome(path)
url_list = []
i = 0

driver.get('https://www.youtube.com/results?search_query=oh+wonder')
time.sleep(3)

tags = driver.find_elements_by_class_name('yt-lockup-title')
for tag in tags:
    print "[%d] %s" % (i, tag.text)
    a = tag.find_element_by_tag_name('a')
    url_list.append(a.get_attribute('href'))
    i += 1

user_input = input("which one you like to play:")
driver.get(url_list[user_input])

