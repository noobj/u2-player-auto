#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
import os
from os.path import expanduser
import time
import getopt
import sys
import signal


path =  expanduser("~") +'/' + 'python/chromedriver'
driver = webdriver.Chrome(path)

#let driver waits for at most 5 seconds to find elements
driver.implicitly_wait(5)
#for store url
url_list = []
#for store name of video
text_list = []

i = 0
search_query = ''

def handler(sig, frame):
    print "chill man"
    driver.quit()

#fetch the args for the search query
opt, args = getopt.getopt(sys.argv[1:], '')
for arg in args:
    search_query += arg + '+'
search_query = search_query[:-1]

driver.get('https://www.youtube.com/results?search_query='+search_query)
time.sleep(3)
tags = driver.find_elements_by_class_name('yt-lockup-title')
for tag in tags:
    print "[%d] %s" % (i, tag.text)
    text_list.append(tag.text)
    a = tag.find_element_by_tag_name('a')
    url_list.append(a.get_attribute('href'))
    i += 1

user_input = input("which one you like to play:")
driver.get(url_list[user_input])
print "now playing ----- %s -------" % (text_list[user_input])

signal.signal(signal.SIGINT, handler)
signal.pause()
