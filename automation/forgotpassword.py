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

#------------------Manage login(start)-----------------------
login = driver.find_element_by_id("btn_oxygen_login")
login.click()


frameID = driver.find_element_by_css_selector("div[class=fancybox-inner]>iframe")
driver.switch_to_frame(frameID)

forgotpassword= driver.find_element_by_link_text('Forgot your password?')
forgotpassword.click()

#frameID = driver.find_element_by_css_selector("iframe")
#driver.switch_to_frame(frameID)
frameID = driver.find_element_by_css_selector("body[class= iframe_mode ForgotCredentials ]")
driver.switch_to_frame(frameID)


username = driver.find_element_by_id("username_str")
username.send_keys("selenium505@gmail.com")
