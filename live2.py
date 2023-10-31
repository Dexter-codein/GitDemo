from selenium import webdriver



driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys('rishabh')
driver.find_element_by_id("pass").send_keys('rishabh')

submit_button = driver.find_element_by_xpath("//button[@type='submit']")
driver.implicitly_wait(10)
submit_button.click()
