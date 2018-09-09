#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
import os
from os.path import expanduser
import time
import getopt
import sys
import signal
from subprocess import call



def toggle_auto(driver):
    a = driver.find_element_by_id('autoplay-checkbox')
    a.click()

def toggle_video(driver):
    a = driver.find_element_by_css_selector('.player-api.player-width.player-height')
    a.click()


path =  expanduser("~") +'/' + 'python/chromedriver'
driver = webdriver.Chrome(path)

#let driver waits for at most 5 seconds to find elements
#driver.implicitly_wait(5)

#for store url
url_list = []
#for store name of video
text_list = []

i = 0
search_query = ''

def handler(sig, frame):
    print "peace man"
    driver.quit()
    sys.exit()

#fetch the args for the search query
opt, args = getopt.getopt(sys.argv[1:], '')
for arg in args:
    search_query += arg + '+'
search_query = search_query[:-1]

driver.get('https://www.youtube.com/results?search_query='+search_query)
time.sleep(3)
tags = driver.find_elements_by_id('video-title')
for tag in tags:
    print "[%d] %s" % (i, tag.text)
    text_list.append(tag.text)
    url_list.append(tag.get_attribute('href'))
    i += 1

user_input = input("which one you like to play:")
driver.get(url_list[user_input])
print "now playing ----- %s -------" % (text_list[user_input])

signal.signal(signal.SIGINT, handler)

while True:
    print "what shit you would like to do?"
    print "a - for toggle auto play"
    print "s - for pause"
    print "+ - for increase volume"
    print "- - for decrease volume"
    print "n - next track"
    print "p - previous track"
    print "m - mute"
    print "r - refresh"
    user_input = raw_input("choose one shit:")

    if user_input == 'n':
        a = driver.find_element_by_css_selector('.content-link.spf-link.yt-uix-sessionlink.spf-link')
        driver.get(a.get_attribute('href'))
    elif user_input == 'p':
        driver.back()
    elif user_input == "a":
        toggle_auto(driver)
    elif user_input == 's':
        toggle_video(driver)
    elif user_input == '+':
        call(["amixer", "-q", "sset", "Master", "5%+"])
    elif user_input == '-':
        call(["amixer", "-q", "sset", "Master", "5%-"])
    elif user_input == 'm':
        a = driver.find_element_by_css_selector('.player-api.player-width.player-height')
        a.send_keys('m')
    elif user_input == 'r':
        driver.refresh()
