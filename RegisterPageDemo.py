from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[class*='form-control ']").send_keys("RAHUL")

driver.find_element(By.XPATH,
                    "//input[@class='form-control ng-untouched ng-pristine ng-invalid' and @name='email']").send_keys(
    "abc@gmail.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("ILoveIndia")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = driver.find_element(By.ID, "exampleFormControlSelect1")
dPwn = Select(dropdown)
dPwn.select_by_visible_text("Male")

driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR, "body > app-root > form-comp > div > form > div:nth-child(8) > input").click()

driver.find_element(By.CSS_SELECTOR, "input[class*='btn-success'][type='submit']").click()

message = driver.find_element(By.CSS_SELECTOR, "div [class='alert alert-success alert-dismissible']").text
print(message)
assert ("Success" in message)

lenAElement = driver.find_elements(By.XPATH, "//a").__sizeof__()

print(lenAElement)
print("End")
driver.close()

