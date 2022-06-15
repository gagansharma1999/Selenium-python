from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
#from config import settings
#import xlrd
import time

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(r"D:\SAI Automation\NSRS_WEB\Drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("http://192.168.23.253:51/Login/New_registration")


class Athletes_tests:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Athletes_tests()
        return cls.instance

    def registration(self):
        try:
            file_path = settings['test_data_loc']
            workbook = xlrd.open_workbook(file_path)
            sheet = workbook.sheet_by_name("Athlete")
            rowcount = sheet.nrows
            # colCount = sheet.ncols

            for curr_row in range(1, rowcount):
                firstname = sheet.cell_value(curr_row, 0)
                mothername = sheet.cell_value(curr_row, 1)
                fathername = sheet.cell_value(curr_row, 2)
                gender = sheet.cell_value(curr_row, 3)
                email_add = sheet.cell_value(curr_row, 4)
                sport_sel = sheet.cell_value(curr_row, 5)

            # Click Register here
            #driver.find_element_by_xpath("//a[text()='Register Here']").click()
            #driver.implicitly_wait(5)
            # Click on Athlete button on new registration
            driver.find_elements(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div/a").click()
            driver.implicitly_wait(2)

            # to upload image
            driver.find_elements(By.ID, 'profile_image_btn')#.send_keys("C:\Users\ACER\Pictures\\test001.jpg")

            # to upload first name, mother name and father name
            driver.find_elements(By.ID, 'first_name').send_keys(firstname)
            mother_name = driver.find_elements(By.ID, 'mother_full_name')
            mother_name.send_keys(mothername)
            father_name = driver.find_elements(By.ID, 'father_full_name')
            father_name.send_keys(fathername)

            # to select Gender
            element_gen = driver.find_element(By.ID, 'gender')
            select = Select(element_gen)
            select.select_by_value(gender)
            # select.select_by_visible_text('Male')
            # select.select_by_index(2)
            # select.select_by_value('F')

            # to Select DOB
            dob = driver.find_elements(By.ID, 'userDateofBirth')
            dob.click()
            dob.clear()
            dob.send_keys('04/10/2015')

            # to fill Address
            driver.find_elements(By.ID, "address_of_name").send_keys('Rohit')
            driver.find_elements(By.ID, "post_office").send_keys('742101')
            driver.find_elements(By.XPATH, 'sub_district').send_keys('sub')

            # to fill permanent address
            chk = driver.find_elements(By.ID, 'filladdress')
            chk.click()
            driver.implicitly_wait(10)

            # to fill mobile number and email id
            driver.find_elements(By.ID, 'MobileNoUser').send_keys('9878108494')
            email = driver.find_elements(By.ID, 'email_id')
            email.send_keys(email_add)

            # select Sport
            sports = driver.find_elements(By.ID, 'DDLSports')
            sport = Select(sports)
            sport.select_by_value(sport_sel)

            # select Event Type
            eventtype = driver.find_elements(By.XPATH, 'ddlEventType')
            event_type = Select(eventtype)
            event_type.select_by_value('16')

            event = driver.find_elements(By.XPATH, "//button[@class='multiselect dropdown-toggle btn btn-default']")
            event1 = Select(event)
            event1.select_by_visible_text('100 m hurdle')

            # select Tracksuit
            # tracksuit = driver.find_element_by_xpath("//select[@id ='blazer_size']")
            # blazer = Select(tracksuit)
            # blazer.select_by_visible_text('44')

            trackshirt = driver.find_elements(By.XPATH, "//select[@id ='tshirt_size']")
            shirt = Select(trackshirt)
            shirt.select_by_visible_text('40')

            # trackpant = driver.find_element_by_xpath("//select[@id ='pant_size']")
            # pant = Select(trackpant)
            # pant.select_by_visible_text('52')

            # shoesize = driver.find_element_by_xpath("//select[@id ='shoe_size']")
            # shoe = Select(shoesize)
            # shoe.select_by_visible_text('10')

            # select Login password
            driver.find_elements(By.XPATH, "//input[@id = 'login_password']").send_keys('Admin@123')
            driver.find_elements(By.XPATH, "//input[@id = 'confirm_password']").send_keys('Admin@123')

            # Click on Checkbox (Terms & Condition)
            action = ActionChains(driver)
            source = driver.find_elements(By.XPATH, "//input[@name= 'terms_conditions']")
            action.click(source)
            action.perform()
            

            driver.find_elements(By.XPATH, '//a[@id="AthletePILink"]').click()
            driver.implicitly_wait(20)

            output = driver.find_elements(By.XPATH, "//div[@class ='col-6 block block-2']//"
                                                  "div[@class ='label-user']//span")
            kid = output.text

            print(kid)
            # KID = driver.find_element_by_css_selector('.block-2 ')
            # kid = KID.text
            # print(kid)

        except Exception as e:
            print("Error while accessing page : " + str(e))
            # driver.quit()

        time.sleep(20)
        # driver.quit()


Athletes_tests = Athletes_tests.get_instance()
