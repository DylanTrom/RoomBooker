from selenium import webdriver
from datetime import datetime
from threading import Timer
import time

x=datetime.today()
y=x.replace(day=x.day+0, hour=19, minute=52, second=45, microsecond=0)
delta_t=y-x
#Remember to change day in element title!

secs=delta_t.seconds+1

def hello_world():
    #Load WebDriver file location after install...webdriver.edge changes based on browser, webdriver.chrome, etc.
    browser=webdriver.Edge('C:\\Windows\SysWOW64\MicrosoftWebDriver.exe')
    #Load Page
    browser.get('https://booking.lib.buffalo.edu/space/19769')
    weeks=browser.find_element_by_xpath('//button[@class="fc-resourceTimeGridWeek-button fc-button fc-button-primary"]')
    weeks.click()
    time.sleep(2)
    #Must be changed based on day, may be able to automate with datetime library
    elem=browser.find_element_by_xpath('//*[@title="6:00am Friday, January 31, 2020 - Room 16 - Available"]')
    elem.click()
    time.sleep(2)
    button=browser.find_element_by_xpath('//button[@name="submit_times"]')
    button.click()
    time.sleep(1)
    cont=browser.find_element_by_id('terms_accept')
    cont.click()
    name=browser.find_element_by_id('fname')
    name.send_keys('Dylan')
    lname=browser.find_element_by_id('lname')
    lname.send_keys('Trommetter')
    email=browser.find_element_by_id('email')
    email.send_keys('dmtromme@buffalo.edu')
    final=browser.find_element_by_id('btn-form-submit')
    final.click()
    time.sleep(3)
    #Confirm in email:
    browser.get('https://mail.google.com/?ui=html')
    #basic=browser.find_element_by_xpath('//input[@class="maia-button maia-button-secondary"]')
    #basic.click()
    mail=browser.find_element_by_xpath('//tr[@bgcolor="#ffffff"]')
    #mail=browser.find_elements_by_xpath('//tr[@bgcolor="#e8eef7"]')[3]
    mail.click()
    time.sleep(1)
    confirm=browser.find_element_by_partial_link_text('https://booking.lib.buffalo.edu/equipment/confirm/')
    time.sleep(1)
    #confirm.click()
    tab=confirm.get_attribute('href')
    browser.get(tab)
    last=browser.find_element_by_id('s-lc-verify-button')
    last.click()
    #...

t = Timer(secs, hello_world)
t.start()

#browser=webdriver.Edge('C:\\Windows\SysWOW64\MicrosoftWebDriver.exe')
#browser.get('https://mail.google.com/mail/u/1/#inbox/?ui=html')
#browser.get('https://mail.google.com/?ui=html')
#basic=browser.find_element_by_xpath('//input[@class="maia-button maia-button-secondary"]')
#basic.click()
#mail=browser.find_element_by_xpath('//tr[@bgcolor="#ffffff"]')
#mail.click()
#mail=browser.find_elements_by_xpath('//tr[@bgcolor="#e8eef7"]')[3]
#mail.click()
#time.sleep(1)
#confirm=browser.find_element_by_partial_link_text('https://booking.lib.buffalo.edu/equipment/confirm/')
#time.sleep(1)
#confirm.click()