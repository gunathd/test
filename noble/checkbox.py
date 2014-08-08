#Author : Dinusha Gunathilaka

from selenium import webdriver
import time

#Open Firefox browser
driver = webdriver.Firefox()

#Maximize the window size
driver.maximize_window()
driver.implicitly_wait(10)

#Open app
driver.get('http://developer-local.autodesk.com:8000/')

signin = driver.find_element_by_id("btn_oxygen_login")
signin.click()

frameID = driver.find_element_by_id("oxygen_ifr")
driver.switch_to_frame(frameID)

id_link= driver.find_element_by_link_text('Need an Autodesk ID?')
id_link.click()

driver.switch_to_default_content()

frame = driver.find_element_by_css_selector("#oxygen-container>iframe")
driver.switch_to_frame(frame)

#Enter first name
firstname = driver.find_element_by_id("firstname_str")
firstname.send_keys("My")

#To receive email communications from Autodesk
checkbox1 = driver.find_element_by_css_selector("label[class='custom_checkbox']").click()

#To agree with agreement
#checkbox2 = driver.find_element_by_css_selector("label[class='custom_checkbox']").click()

checkbox2 = driver.find_element_by_tag_name('div')
checkbox2.click()
