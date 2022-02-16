from selenium import webdriver
from selenium.webdriver.common.by import By

import sys
sys.path.append("D:\python Q\e-commerce")
from pageobject.LoginPage import LoginPage
from Utilities.readproperties import reading
from Utilities.customLogger import Log
from Utilities import ExcelUtils
import time


class Test_002_DDT_Login:
    baseurl=reading.getappurl()
    path=r"D:\python Q\e-commerce\Test Data\data_proj.xlsx"
    logger=Log.loggen()

    def test_Login(self,setup):
        self.logger.info("****************Verying Data Driven Testing**************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)

        self.row=ExcelUtils.getRowCount(self.path,"Sheet1")
        self.column=ExcelUtils.getColCount(self.path,"Sheet1")
        status=[]
        for r in range(2,self.row+1):
            self.username=ExcelUtils.ReadData(self.path,"Sheet1",r,1)
            self.password=ExcelUtils.ReadData(self.path,"Sheet1",r,2)
            self.exp = ExcelUtils.ReadData(self.path, "Sheet1", r, 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_login_title=self.driver.title
            if act_login_title == "Dashboard / nopCommerce administration":
                if self.exp=="Pass":
                    self.logger.info("passed")
                    time.sleep(3)
                    self.lp.clickLogout()
                    status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("Failed")
                    time.sleep(3)
                    self.lp.clickLogout()
                    status.append("Fail")
            elif act_login_title != "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("failed")
                    status.append("Failed")
                elif self.exp == "Fail":
                    self.logger.info("passed")
                    status.append("Pass")

        if "Fail" not in status:
            self.logger.info("Login DDT Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT failed")
            self.driver.close()
            assert False

        self.logger.info("Test case 001 passed,end ")
        print(status)




