from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.rahulshettyacademy.com/client/")



