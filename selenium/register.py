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

#Click on registration button
register = driver.find_element_by_id("btn_oxygen_registration")
register.click()

#Redirect to registration iframe
frameID = driver.find_element_by_css_selector("#oxygen-container>iframe")
driver.switch_to_frame(frameID)

#Enter first name
firstname = driver.find_element_by_id("firstname_str")
firstname.send_keys("My")

#Enter last name
lastname = driver.find_element_by_id("lastname_str")
lastname.send_keys("Test")

#Enter username
username = driver.find_element_by_id("username_str")
username.send_keys("developer123456")

#Enter email address
email = driver.find_element_by_id("email_str")
email.send_keys("mytest777@gmail.com")

#To confirm email address
emailconfirm = driver.find_element_by_id("email_confirm_str")
emailconfirm.send_keys("mytest777@gmail.com")

#enter password
password = driver.find_element_by_id("password_str")
password.send_keys("Mytest123")

#To confirm password
passwordconfirm = driver.find_element_by_id("password_confirm_str")
passwordconfirm.send_keys("Mytest123")

#To receive email communications from Autodesk
checkbox1 = driver.find_element_by_css_selector("label[class='custom_checkbox']").click()

#To agree with agreement
checkbox2 = driver.find_element_by_css_selector("label[class='custom_checkbox']").click()

#To register
register = driver.find_element_by_css_selector("button[class='ui-button button_submit default ui-widget ui-state-default ui-corner-all ui-button-text-only last_child']")
register.click()

#Waiting time
time.sleep(5)

#-------------------Manage logout(start)-------------------
logout_link = driver.find_element_by_link_text('LOGOUT')
logout_link.click()
#-------------------Manage logout(finish)-------------------

time.sleep(5)

#Close the web browser
driver.close()


