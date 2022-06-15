
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("test case started")
driver = webdriver.Firefox(executable_path=r"D:\PY Projects\Test 1\Drivers\geckodriver.exe")
driver.get("https://qainfotech.com/")
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("/html/body/header/nav/div/ul/li[1]/a/span").click()
driver.find_element_by_xpath("/html/body/header/nav/div/ul/li[1]/div/ul/li[1]/a/span").click()

driver.find_element_by_xpath("/html/body/header/nav/div/ul/li[1]/a/span").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/main/div/div[1]/div/div/section[2]/div/div/div[1]/div/div/div/div/div/div/h2").click()

time.sleep(5)
driver.quit()
print("Successfully completed")