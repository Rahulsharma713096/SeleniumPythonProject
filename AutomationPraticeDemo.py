import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "input[value='radio2'][name='radioButton'][class='radioButton']").click()

driver.find_element(By.CSS_SELECTOR, "input[value='radio3'][name='radioButton'][class='radioButton']").click()

driver.find_element(By.CSS_SELECTOR, "input[value='radio1'][name='radioButton'][class='radioButton']").click()

driver.find_element(By.ID, "autocomplete").send_keys("Ind")
# Explicit wait
time.sleep(3)
driver.find_element(By.ID, "ui-id-3").click()
time.sleep(3)

print(driver.find_element(By.ID, "autocomplete").get_attribute("value"))




