from selenium import webdriver
from selenium.webdriver.common.by import By

class Serch:
    txtEmail_xpath="//*[@id='SearchEmail']"
    txtFname_xpath="//*[@id='SearchFirstName']"
    txtLastname_xpath="//*[@id='SearchLastName']"
    btnSearch_xpath="//*[@id='search-customers']"
    table_xpath="//*[@id='customers-grid_wrapper']/div[1]/div"
    tableEmail_xpath="//*[@id='customers-grid']/tbody/tr/td[2]"
    tableName_xpath="//*[@id='customers-grid']/tbody/tr/td[3]"

    def __init__(self,driver):
        self.driver=driver

    def Enter_Email(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def Enter_fname(self,fname):
        self.driver.find_element(By.XPATH,self.txtFname_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtFname_xpath).send_keys(fname)

    def Enter_Lname(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastname_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtLastname_xpath).send_keys(lname)

    def Click_Search(self):
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()




