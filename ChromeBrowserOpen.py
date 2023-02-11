from selenium import webdriver

# driver=webdriver.chrome("path")
# for selenium manger  we can use without path

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")

getTitle = driver.title
print(getTitle)

url = driver.current_url
print(url)
driver.close()