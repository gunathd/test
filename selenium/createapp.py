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

#Click on add a new app hyperlink
addapp_link = driver.find_element_by_link_text('Add a new app')
addapp_link.click()

#Enter app name
appname = driver.find_element_by_id("new_machine_name")
appname.send_keys("OpenWeatherMapApp")

#Enter callback url
callback_url = driver.find_element_by_id("new_callback_url")
callback_url.send_keys("http://api.openweathermap.org/data/2.5/weather")

#Select option from product dropdownlist
product = driver.find_element_by_css_selector("select[class='form-select required selectlist-select'] > option[value='prod-Autodesk-Viewing-API']").click()

#####To remove selected option
#####remove = driver.find_element_by_css_selector("span[class='btn btn-primary pull-right remove-product']")
#####remove.click()

#Click on create app button
createapp = driver.find_element_by_id("edit-submit")
createapp.click()

time.sleep(5)

#-------------------Manage logout(start)-------------------
logout_link = driver.find_element_by_link_text('logout')
logout_link.click()
#-------------------Manage logout(finish)-------------------

#Waiting time
time.sleep(5)

#Close the web browser
driver.close()

