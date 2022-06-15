'''

driver.find_element_by_xpath("").send_keys("")
driver.find_element_by_xpath("").click()

'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("test case started")
driver = webdriver.Firefox(executable_path=r"D:\PY Projects\Test 1\Drivers\geckodriver.exe")


driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
driver.delete_all_cookies()
driver.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[2]/a").click()
driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[1]/div[1]/input").send_keys("Gagan")
driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[1]/div[2]/input").send_keys("Sharma")
driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[2]/div/textarea").send_keys("Add:- XYZ")
driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[3]/div[1]/input").send_keys("gagansharma2131@gmail.com")
driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[4]/div/input").send_keys("7503901611")
driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[5]/div/label[1]/input").click()
driver.find_element_by_id("checkbox1").click()
driver.find_element_by_id("checkbox2").click()
driver.find_element_by_id("checkbox3").click()
time.sleep(2)

driver.find_element_by_id("Skills").click()
driver.find_element_by_id("countries").click()
driver.find_element_by_id("firstpassword").send_keys("123456")
driver.find_element_by_id("secondpassword").send_keys("123456")

driver.find_element_by_id("Button1").click()
time.sleep(5)

driver.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[4]/a").click()
driver.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[4]/ul/li[3]/a").click()
driver.find_element_by_xpath("/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
time.sleep(5)

driver.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[10]/a").click()
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/ul/li[2]/div[1]/a").click()

print(driver.title)
print(driver.current_url)
driver.get("https://google.com/")
print(driver.title)
driver.quit()
print("Successfully completed")