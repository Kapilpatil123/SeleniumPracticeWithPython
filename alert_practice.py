from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
#lounch webdriver.chrome
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,10)
#########################
#Alert ,simple popup accept or dismiss these alerts.
driver.get("http://demo.automationtesting.in/Alerts.html")
alert = driver.find_element_by_xpath(".//button[@onclick='alertbox()']")
print(alert.text)
alert.click()
alert2 = driver.switch_to.alert
print(alert2.text)
alert2.accept()

###########################
#A confirm box is similar to an alert, except the user can also choose to cancel the message

driver.find_element_by_xpath(".//a[@href='#CancelTab']").click()
driver.find_element_by_xpath(".//button[@class='btn btn-primary']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()

###############################
#Prompts are similar to confirm boxes, except they also include a text input.Pressing the cancel button will not submit any text

driver.find_element_by_xpath(".//a[@href='#Textbox']").click()
driver.find_element_by_xpath(".//button[@class='btn btn-info']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.send_keys("kapilpatil")
print(alert.text)
alert.accept()
driver.close()
#####################################