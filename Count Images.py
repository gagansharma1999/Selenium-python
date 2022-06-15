import os
directory = r"C:\Users\ACER\Pictures\Screenshots"

for filename in os.listdir(directory):
    if filename.endswith(".png"):
      #do smth
      print("Running  " + str(len(filename)))
    else:
        print("Stops here  " + str(len(filename)))

print(len(filename))




#
# import requests
# import urllib3
# import pytest
# from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
#
# capabilities = {
#     "build": "[Python] Finding broken images on a webpage using Selenium",
#     "name": "[Python] Finding broken images on a webpage using Selenium",
#     "platform": "Windows 10",
#     "browserName": "Chrome",
#     "version": "latest"
# }
#
# user_name = "user-name"
# app_key = "access-key"
# URL = "file:///C:/Users/ACER/Pictures/Screenshots/"
# iBrokenImageCount = 0
#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# driver = webdriver.Chrome(r"D:\SAI Automation\NSRS_WEB\Drivers\chromedriver.exe")
#
# driver.maximize_window()
# driver.get(URL)
#
#
#
# image_list = driver.findElements(By.tagName("img"))
# print('Total number of images on '+ URL + ' are ' + str(len(image_list)))
#
#
# for img in (image_list):
#     try:
#         response = requests.URLRequired.driver.get(image_list)
#         if (response.status_code != 200):
#             print(img.get_attribute('outerHTML') + " is broken.")
#             iBrokenImageCount = (iBrokenImageCount + 1)
#
#     except requests.exceptions.MissingSchema:
#         print("Encountered MissingSchema Exception")
#     except requests.exceptions.InvalidSchema:
#         print("Encountered InvalidSchema Exception")
#     except:
#         print("Encountered Some other Exception")
#
# driver.quit()
#
# print('The page ' + URL + ' has ' + str(iBrokenImageCount) + ' broken images')

