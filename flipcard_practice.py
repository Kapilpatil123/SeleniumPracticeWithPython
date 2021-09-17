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

#navigate to to flipkart
driver.get("https://www.flipkart.com/")

#handling unnecessary popup
driver.find_element_by_xpath('.//button[@class="_2KpZ6l _2doB4z"]').click()

ele = wait.until(EC.presence_of_element_located((By.XPATH,".//div[text()='Electronics']")))
action = ActionChains(driver)
action.move_to_element(ele).perform()


driver.find_element_by_xpath('.//button[@class="_2KpZ6l _2doB4z"]').click()


#mouse overing the electronics menu option by hand and click on laptop accesories




