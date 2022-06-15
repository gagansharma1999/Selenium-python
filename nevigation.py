
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

print("test case started")
# driver = webdriver.Firefox(executable_path=r"D:\SAI Automation\NSRS_WEB\Drivers\geckodriver.exe")
driver = webdriver.Chrome(r"D:\SAI Automation\NSRS_WEB\Drivers\chromedriver.exe")

driver.get("http://192.168.23.253:51/")
driver.maximize_window()
time.sleep(5)
print(driver.title)
print(driver.current_url)
# action = ActionChains(driver)
# action.move_to_element("closeMIBPopup1()").click("closeMIBPopup1()").perform()

button = driver.find_element(By.CLASS_NAME, "open_button").click()
time.sleep(5)
# driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div/div/a[1]").click()
# driver.find_element_by_id("username").send_keys("ranaAt01@gmail.com")
# driver.find_element_by_id("Password").send_keys("Rana@1234")
# driver.find_element_by_id("CaptchaInputText")
#driver.find_element_by_xpath("/html/body/main/div/div[1]/div/div/section[2]/div/div/div[1]/div/div/div/div/div/figure/img").click()
# time.sleep(5)
#
# driver.get("https://google.com/")
# print(driver.title)
# time.sleep(5)
# driver.back()
# print(driver.title)
# time.sleep(5)
# driver.forward()
# print(driver.title)
# time.sleep(5)
driver.quit()
print("Successfully completed")