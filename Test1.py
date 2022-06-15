from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("sample test case started")

driver = webdriver.Firefox(executable_path=r"D:\PY Projects\Test 1\Drivers\geckodriver.exe")

# maximize the window size
driver.maximize_window()
time.sleep(3)
print(driver.title)
print(driver.current_url)

# close the browser
driver.quit()

print("sample test case successfully completed")