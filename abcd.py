from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.keys import Keys

print("test case started")
driver = webdriver.Chrome(r"D:\PY Projects\Test 1\Drivers\chromedriver.exe")
driver.implicitly_wait(0.5)
# maximize with maximize_window()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# identify element and click()
l=driver.find_element_by_name("submit")
l.click()
'alert_is_present() expected condition wait for 5 seconds'
try:
   WebDriverWait(driver, 5).until (EC.alert_is_present())
   'switch_to.alert for switching to alert and accept'
   alert = driver.switch_to.alert
   alert.accept()
   print("alert Exists in page")
except TimeoutException:
   print("alert does not Exist in page")
driver.close()
print("Successfully completed")