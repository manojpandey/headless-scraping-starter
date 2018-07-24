#!/usr/bin/env python3

from pyvirtualdisplay import Display
from selenium import webdriver
import os

chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Chrome(chromedriver)
browser.get('http://www.google.com')
print(browser.title)
browser.quit()
display.stop()
