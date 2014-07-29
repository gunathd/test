#Author : Dinusha Gunathilaka

from selenium import webdriver
import time

#Open Firefox browser
driver = webdriver.Firefox()

#Maximize the window size
driver.maximize_window()
driver.implicitly_wait(10)

#Open app
driver.get('http://developer-stg.autodesk.com')

#-----------------Manage login(start)-----------------
login = driver.find_element_by_id("btn_oxygen_login")
login.click()

frameID = driver.find_element_by_css_selector("div[class=fancybox-inner]>iframe")
driver.switch_to_frame(frameID)

username = driver.find_element_by_id("userName_str")
username.send_keys("selenium505@gmail.com")

password = driver.find_element_by_id("password_str")
password.send_keys("Pythontest123")

signin = driver.find_element_by_css_selector("button[class='ui-button button_submit default adskBtn-primary ui-widget ui-state-default ui-corner-all ui-button-text-only last_child']")
signin.click()
#-----------------Manage login(finish)-----------------

#Click on logout hyperlink
logout_link = driver.find_element_by_link_text('LOGOUT')
logout_link.click()

#Waiting time
time.sleep(5)

#Close the web browser
driver.close()

