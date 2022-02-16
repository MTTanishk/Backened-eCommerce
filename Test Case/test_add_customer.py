import sys
sys.path.append("D:\python Q\e-commerce")
from pageobject.Add_Customer import new_customer
from pageobject.LoginPage import LoginPage
from Utilities.readproperties import reading
from Utilities.customLogger import Log
from selenium.webdriver.common.by import By
import string
import random
import time


class Test_002_AddCustomer:
    baseurl=reading.getappurl()
    username=reading.getusername()
    password=reading.getpassword()
    logger = Log.loggen()


    def test_addcustomer(self,setup):
        self.logger.info("****************Test__002 Add Customer**************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("----------Login Successfull----------")

        self.logger.info("----------Add_Customer Test Starting----------")
        addCustomer=new_customer(self.driver)
        addCustomer.ClickOnCustomerMenu()
        addCustomer.ClickOnCustomerItem()
        time.sleep(3)
        addCustomer.ClickOnAdd()
        customer_title=self.driver.title
        if customer_title=="Add a new customer / nopCommerce administration":
            self.logger.info("Providing Customer Details")
            random_email=random_generator()
            self.email=random_email + "@gmail.com"
            addCustomer.Setemail(self.email)
            addCustomer.setpassword("Taniji9934")
            addCustomer.setfirst_name("Tanishk")
            addCustomer.setlast_name("MT")
            addCustomer.setgender("Female")
            addCustomer.setDOM("9/6/1997")
            addCustomer.enetercompany_name("L and T")
            addCustomer.tax_exempt()
            addCustomer.news_letter("Test store 2")
            addCustomer.customer_role("Vendors")
            addCustomer.choosevendor("Vendor 2")
            addCustomer.Clickactive()
            addCustomer.setadmin_content("just testing chilll")
            time.sleep(3)
            self.driver.find_element(By.NAME,"save").click()
            #addCustomer.Clicksave_customer()
            self.logger.info("Customer info Filled")
            time.sleep(3)
            self.logger.info("Checking if saved")
            msg=self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]").text
            print(msg)
            if "The new customer has been added successfully." in msg:
                self.driver.close()
                self.logger.info("**********The customer added sucessully**********")
                assert True
            else:
                self.driver.save_screenshot("D:\python Q\e-commerce\screenshots\\add_customerfailed.png")
                self.driver.close()
                self.logger.info("**********The customer not added sucessully**********")
                assert False
        else:
            self.logger.warning("*********Customer Add page not opened********")
            assert False



def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    new_email=""
    for x in range(size):
        new_email=new_email+random.choice(chars)
    return new_email






