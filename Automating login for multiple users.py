from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# import getpass

print("test case started")
driver = webdriver.Chrome(r"D:\SAI Automation\NSRS_WEB\Drivers\chromedriver.exe")

driver.get("http://192.168.23.253:51/")
driver.maximize_window()
time.sleep(5)
print(driver.title)
print(driver.current_url)

username = ['ronuAt03@gmail.com', 'RahulDiving@yopmail.com', 'Rahulyoga@yopmail.com', 'RahulWrestling@yopmail.com']
for i in username:
    button = driver.find_element(By.CLASS_NAME, "open_button").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div/div/a[1]").click()
    f1 = driver.find_element(By.ID, "username")
    f1.clear()
    f1.send_keys(username[i])

    f2 = driver.find_element(By.ID, "Password")
    f2.clear()
    f2.send_keys("Rana@1234")

    driver.implicitly_wait(20)

    box = driver.find_element(By.ID, "CaptchaInputText")
    box.clear()
    time.sleep(10)

    driver.find_element(By.ID, "login-button").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li/a").click()
    driver.find_element(By.ID, "logout_link").click()
    driver.implicitly_wait(20)

driver.quit()
print("Successfully completed")
