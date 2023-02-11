import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH,
                    "//a [@href='https://rahulshettyacademy.com/documents-request' and @class='blinkingText']").click()
w = driver.window_handles
driver.switch_to.window(w.__getitem__(1))
wait.until(
    expected_conditions.visibility_of(driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com")))


uname=driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
uname= uname.split("@")[1]

driver.switch_to.window(w.__getitem__(0))

driver.find_element(By.ID,"username").send_keys(uname)

driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.CSS_SELECTOR, "#login-form > div:nth-child(4) > div > label:nth-child(2) > span.checkmark").click()
wait.until(
    expected_conditions.visibility_of(driver.find_element(By.ID,"okayBtn")))

driver.find_element(By.ID,"okayBtn").click()
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
time.sleep(15)



