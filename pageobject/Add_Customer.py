from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class new_customer:
    lnkmenu_customer_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkcustomer_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btnadd_new_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtnew_Email_id="Email"
    txtnew_password_id="Password"
    txtnew_firstname_id="FirstName"
    txtnew_lastname_id="LastName"
    rdgender_male_id="Gender_Male"
    rdgender_female_id="Gender_Female"
    txtDOB_id="DateOfBirth"
    drpvendor_xpath="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[11]/div[2]/select"
    txtcompany_id="Company"
    customer_role_xpath="//*[@id='Company']"
    rdtax_exempt_xpath="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[8]/div[2]/input"
    lstitem_newsletter_xpath="//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    lstitem_yourstore_xpath="//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    lstitem_teststore_xpath="//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    txt_customerrole_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitem_administrator_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lstitem_guest_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitem_forummoderator_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    lstitem_registered_xpath="//*[@id='9958dbee-e00a-4deb-8e5c-16a07ae5ca0d']"

    lstitem_vendor_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    lstitem_delete_xpath="//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"
    rdactive_xpath="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[12]/div[2]/input"
    txtAdmin_content_xpath="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[13]/div[2]/textarea"
    btnsave_xpath="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"
    display_custSaved="/html/body/div[3]/div[1]/div[1]"


    def __init__(self,driver):
        self.driver=driver

    def ClickOnCustomerMenu(self):
        self.action = ActionChains(self.driver)
        self.customer_menu=self.driver.find_element(By.XPATH,self.lnkmenu_customer_xpath)
        self.action.double_click(self.customer_menu).perform()

    def ClickOnCustomerItem(self):
        self.driver.find_element(By.XPATH,self.lnkcustomer_xpath).click()

    def ClickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnadd_new_xpath).click()

    def Setemail(self,email):
        self.driver.find_element(By.ID,self.txtnew_Email_id).clear()
        self.driver.find_element(By.ID,self.txtnew_Email_id).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.txtnew_password_id).clear()
        self.driver.find_element(By.ID,self.txtnew_password_id).send_keys(password)

    def setfirst_name(self,first_name):
        self.driver.find_element(By.ID,self.txtnew_firstname_id).clear()
        self.driver.find_element(By.ID,self.txtnew_firstname_id).send_keys(first_name)

    def setlast_name(self,last_name):
        self.driver.find_element(By.ID,self.txtnew_lastname_id).clear()
        self.driver.find_element(By.ID,self.txtnew_firstname_id).send_keys(last_name)

    def setgender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID,self.rdgender_male_id).click()
        elif gender=="Female":
            self.driver.find_element(By.ID,self.rdgender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rdgender_female_id).click()

    def setDOM(self,DOB):
        self.driver.find_element(By.ID,self.txtDOB_id).clear()
        self.driver.find_element(By.ID,self.txtDOB_id).send_keys(DOB)

    def enetercompany_name(self,company_name):
        self.driver.find_element(By.ID,self.txtcompany_id).clear()
        self.driver.find_element(By.ID,self.txtcompany_id).send_keys(company_name)

    def tax_exempt(self):
        self.driver.find_element(By.XPATH,self.rdtax_exempt_xpath).click()

    def news_letter(self,news_letter):
        self.driver.find_element(By.XPATH, self.lstitem_newsletter_xpath).click()
        if news_letter=="Your store name":
            self.news=self.driver.find_element(By.XPATH, self.lstitem_yourstore_xpath)
        else:
            self.news = self.driver.find_element(By.XPATH, self.lstitem_teststore_xpath)
        self.driver.execute_script("arguments[0].click();", self.news)

    def customer_role(self,role):
        self.driver.find_element(By.XPATH,self.txt_customerrole_xpath).click()
        if role == "Registered":
            self.role_selected=self.driver.find_element(By.XPATH, self.lstitem_registered_xpath)
        elif role == "Administrators":
            self.role_selected=self.driver.find_element(By.XPATH,self.lstitem_administrator_xpath)

        elif role == "Forum Moderators":
            self.role_selected=self.driver.find_element(By.XPATH,self.lstitem_forummoderator_xpath)

        elif role == "Vendors":
            self.role_selected=self.driver.find_element(By.XPATH,self.lstitem_vendor_xpath)

        elif role == "Guests":
            self.driver.find_element(By.XPATH,self.lstitem_delete_xpath).click()
            self.role_selected=self.driver.find_element(By.XPATH,self.lstitem_guest_xpath)

        else:
            self.role_selected=self.driver.find_element(By.XPATH,self.lstitem_vendor_xpath)
        self.driver.execute_script("arguments[0].click();",self.role_selected)

    def choosevendor(self,vendor_name):
        name=self.driver.find_element(By.XPATH,self.drpvendor_xpath)
        drp=Select(name)
        drp.select_by_visible_text(vendor_name)

    def Clickactive(self):
        self.driver.find_element(By.XPATH,self.rdactive_xpath).click()

    def setadmin_content(self,admincontent):
        self.driver.find_element(By.XPATH,self.txtAdmin_content_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAdmin_content_xpath).send_keys(admincontent)

    def Clicksave_customer(self):
        self.driver.find_element(By.XPATH,self.btnsave_xpath)





















