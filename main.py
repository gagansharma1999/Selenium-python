# This is a sample Python script.

#============================================
#driver code:-
#1. for firefox:-{
# driver = webdriver.Firefox(executable_path=r"D:\PY Projects\Test 1\Drivers\geckodriver.exe")
# }
#2. for chrome:-{
# driver = webdriver.Chrome(r"D:\PY Projects\Test 1\Drivers\chromedriver.exe")
# }

#============================================
'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("test case started")
driver = webdriver.Chrome(r"D:\PY Projects\Test 1\Drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()
time.sleep(5)

driver.quit()
print("Successfully completed")

'''