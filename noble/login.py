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

login = driver.find_element_by_id("btn_oxygen_login")
login.click()

frameID = driver.find_element_by_id("oxygen_ifr")
driver.switch_to_frame(frameID)

#Enter username details
username = driver.find_element_by_id("userName_str")
username.send_keys("selenium505@gmail.com")

#Enter password details
password = driver.find_element_by_id("password_str")
password.send_keys("Pythontest123")

#####Click on signin button using xpath
#####signin= driver.find_element_by_xpath("//*[@id='login_container']/div[1]/p/button")
#####signin.click()

#Click on signin button using css selector
signin = driver.find_element_by_css_selector("button[class='ui-button button_submit default adskBtn-primary ui-widget ui-state-default ui-corner-all ui-button-text-only last_child']")
signin.click()

#Waiting time
time.sleep(5)

#Close the web browser
driver.close()


