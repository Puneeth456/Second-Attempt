from selenium import webdriver

class Login:
    def __init__(self,driver):
        self.driver=driver

    def actlogin(self,un,pwd):
        self.driver.find_element_by_id("username").send_keys(un)
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_id("loginButton").click()