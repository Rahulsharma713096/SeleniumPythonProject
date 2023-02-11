from selenium import webdriver

driver= webdriver.Chrome()

driver.get("https://www.google.co.in/")

driver.maximize_window()

driver.get("https://www.google.co.in/")

driver.maximize_window()

driver.back()
print(driver.window_handles.__sizeof__())

driver.refresh()

driver.close()