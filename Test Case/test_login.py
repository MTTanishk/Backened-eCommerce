from selenium import webdriver
import pytest
import sys
sys.path.append("D:\python Q\e-commerce")
from pageobject.LoginPage import LoginPage
from Utilities.readproperties import reading
from Utilities.customLogger import Log
import time


class Test_001_Login:
    baseurl=reading.getappurl()
    username=reading.getusername()
    password=reading.getpassword()
    logger = Log.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("****************Test_001_Login**************")
        self.logger.info("****************Verying Homepage Title**************")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************Homepage Title Passed**************")
        else:
            self.driver.save_screenshot("D:\python Q\e-commerce\screenshots\homePageTitle.png")
            self.driver.close()
            self.logger.error("****************Homepage title failed**************")
            assert False

    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("****************Verying Login Test**************")
        self.driver = setup
        time.sleep(2)
        self.driver.get(self.baseurl)
        time.sleep(2)
        #You can use " self.lp =LoginPage(self.driver) ",then use self with all the " lp "
        lp=LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_login_title=self.driver.title
        if act_login_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****************lOGIN TEST PASSED**************")
        else: #test case failed on purpose to check screenshot
            self.driver.save_screenshot("D:\python Q\e-commerce\screenshots\Login.png")
            self.driver.close()
            self.logger.error("****************lOGIN TEST FAILED**************")
            assert False


