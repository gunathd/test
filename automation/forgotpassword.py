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

#------------------Manage forgot password(start)-----------------------
login = driver.find_element_by_id("btn_oxygen_login")
login.click()

frameID = driver.find_element_by_id("oxygen_ifr")
driver.switch_to_frame(frameID)

forgotpassword= driver.find_element_by_link_text('Forgot your password?')
forgotpassword.click()

driver.switch_to_default_content()

frame = driver.find_element_by_css_selector("#oxygen-container>iframe")
driver.switch_to_frame(frame)

username = driver.find_element_by_id("username_str")
username.send_keys("seleniumtest222@gmail.com")

to_continue1 = driver.find_element_by_css_selector("button[class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']")
to_continue1.click()

to_continue2 = driver.find_element_by_css_selector("a[class='ui-button default ui-widget ui-state-default ui-corner-all ui-button-text-only']")
to_continue2.click()
#------------------Manage forgot password(finish)-----------------------

