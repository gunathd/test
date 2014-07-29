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

#####Get access key by clicking request an accsses key
#####myapps = driver.find_element_by_id("request-access-key")
#####myapps.click()

#------------------Manage login(start)-----------------------
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
#------------------Manage login(finish)-----------------------

#Click on view myapp button
myapps = driver.find_element_by_id("my-apps")
myapps.click()

#To view app details
app_link = driver.find_element_by_link_text('OpenWeatherMapApp')
app_link.click()

#Waiting time
time.sleep(3)

#To view product details
app_link = driver.find_element_by_link_text('Products')
app_link.click()

time.sleep(3)

#To view app details
app_link = driver.find_element_by_link_text('App Details')
app_link.click()

time.sleep(3)

#To view access key details
app_link = driver.find_element_by_link_text('Keys')
app_link.click()

time.sleep(3)

#To edit app details
app_link = driver.find_element_by_link_text('Edit App')
app_link.click()

#-------------------Manage logout(start)-------------------
logout_link = driver.find_element_by_link_text('logout')
logout_link.click()
#-------------------Manage logout(finish)-------------------

time.sleep(5)

#Close the web browser
driver.close()
