#Author : Dinusha Gunathilaka

from selenium import webdriver
webdriver.ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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

#Enter last name
lastname = driver.find_element_by_id("lastname_str")
lastname.send_keys("Test")

#Enter username
username = driver.find_element_by_id("username_str")
username.send_keys("developer12345")

#Enter email address
email = driver.find_element_by_id("email_str")
email.send_keys("mytest999@gmail.com")

#To confirm email address
emailconfirm = driver.find_element_by_id("email_confirm_str")
emailconfirm.send_keys("mytest999@gmail.com")

#enter password
password = driver.find_element_by_id("password_str")
password.send_keys("Mytest123")

#To confirm password
passwordconfirm = driver.find_element_by_id("password_confirm_str")
passwordconfirm.send_keys("Mytest123")

#To receive email communications from Autodesk
checkbox1 = driver.find_element_by_css_selector("label[class='custom_checkbox']").click()

#To agree with agreement
#checkbox2 = driver.find_element_by_css_selector("label[class='custom_checkbox']").click()

#------------------------
#mouse = webdriver.ActionChains(driver)
#
#mouse.move_to_element(checkbox2).click()

try:
   
	checkbox2 = driver.find_element_by_css_selector("label[class='custom_checkbox']")
  
   	if (checkbox2.is_selected()):

    		print("Checkbox is selected..now deselecting")

    		checkbox2.click()

   	else:

       		print("Checkbox is not selected..now selecting it")

      		checkbox2.click()

except Exception as e:

    print ("Exception occured", format(e));

finally:

    #driver.quit()

    print ("finally")


try:

	checkbox1  = driver.find_element_by_css_selector("label[class='custom_checkbox']")

	if (checkbox1.is_selected()):

		print("Checkbox is selected")
	
		checkbox1.click()

	else:

		print("Checkbox is not selected")

		checkbox1.click()

except Exception as e:

	print("Exception occured", format(e));

finally:

	#driver.quit()

	print ("finally")
#-------------------------

#To register
register = driver.find_element_by_css_selector("button[class='ui-button button_submit default ui-widget ui-state-default ui-corner-all ui-button-text-only last_child']")
register.click()

