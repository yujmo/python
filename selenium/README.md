# Selenium #

*简介：Selenium是一款自动化测试工具，支持各种浏览器，实现Web页面的测试*

*1.pip3 install selenium*
*2.yaourt -S geckodriver*

[selenium官网](http://selenium-python.readthedocs.io/index.html)

*小试牛刀：使用selenium 打开firefox浏览器，并自动访问百度*
` 
from selenium import webdriver 
browser = webdriver.Firefox()
browser.get("https://www.baidu.com/")
browser.close()
`
