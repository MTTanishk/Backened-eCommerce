from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:
    txtbox_username_NAME = "Email"
    txtbox_password_id = "Password"
    button_login_cssselector="div.buttons"
    link_logout_xpath = "/html/body/div[3]/nav/div/ul/li[3]/a"


    #constructor to initialize the driver
    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(By.NAME,self.txtbox_username_NAME).clear()
        time.sleep(2)
        self.driver.find_element(By.NAME,self.txtbox_username_NAME).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.txtbox_password_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID,self.txtbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_login_cssselector).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()












