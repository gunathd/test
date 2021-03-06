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

#####Click on signin button using xpath
#####signin= driver.find_element_by_xpath("//*[@id='login_container']/div[1]/p/button")
#####signin.click()

signin = driver.find_element_by_css_selector("button[class='ui-button button_submit default adskBtn-primary ui-widget ui-state-default ui-corner-all ui-button-text-only last_child']")
signin.click()
#-----------------Manage login(finish)-----------------

#-----------------Manage profile(start)-----------------
profile_link = driver.find_element_by_link_text('PROFILE')
profile_link.click()

editprofile = driver.find_element_by_id("edit_myprofile")
editprofile.click()

#Fill up contact information
addressline1 = driver.find_element_by_id("ContactInformation_Address1")
addressline1.clear()
addressline1.send_keys("1 Fusionopolis Walk")

addressline2 = driver.find_element_by_id("ContactInformation_Address2")
addressline2 .clear()
addressline2.send_keys("#04-11 North Tower, Solaris")

zipcode = driver.find_element_by_id("ContactInformation_Zipcode")
zipcode.clear()
zipcode.send_keys("138628")

country = driver.find_element_by_css_selector("select[id=ContactInformation_Country] > option[value='']").click()
country = driver.find_element_by_css_selector("select[id=ContactInformation_Country] > option[value='SG']").click()

phone = driver.find_element_by_name("ContactInformation.Phones[0].Number")
phone.clear()
phone.send_keys("81511725")

#Fill up professional information
company = driver.find_element_by_id("ProfessionalInformation_Company")
company.clear()
company.send_keys("Autodesk Asia Pte Ltd")

jobtitle = driver.find_element_by_id("ProfessionalInformation_JobTitle")
jobtitle.clear()
jobtitle.send_keys("SQA Engineer")

industry = driver.find_element_by_css_selector("select[id=ProfessionalInformation_Industry] > option[value='']").click()
industry = driver.find_element_by_css_selector("select[id=ProfessionalInformation_Industry] > optgroup[value='ACSP'] > option[value='ACSPArchConstServiceProviders']").click()

#Waiting time
time.sleep(3)

#Save profile changes
save= driver.find_element_by_id("btn_save")
save.click()

#####cancel profile changes
#####cancel = driver.find_element_by_id("btn_cancel")
#####cancel.click()

#Redirect to the home page
done = driver.find_element_by_css_selector("a[class='ui-button btn_done ui-widget ui-state-default ui-corner-all ui-button-text-only']")
done.click()
#-----------------Manage profile(finish)-----------------

time.sleep(5)

#-----------------Manage logout(start)-------------------
logout_link = driver.find_element_by_link_text('LOGOUT')
logout_link.click()
#-----------------Manage logout(finish)-------------------

time.sleep(5)

#Close the web browser
driver.close()




