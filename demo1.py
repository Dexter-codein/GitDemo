from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.find_element(By.ID, "email").send_keys('rishabh')
driver.find_element(By.ID, "pass").send_keys('qwerty')
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']" )
submit_button.click()
