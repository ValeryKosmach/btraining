# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_group(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_group(driver, Group(name="name gr1111", header="header222", footer="footer333"))
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_group(driver, Group(name="", header="", footer=""))
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def create_group(self, driver, group):
        self.open_groups_page(driver)
        # init group creation
        driver.find_element_by_name("new").click()
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page(driver)

    def open_groups_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def login(self, driver, username, password):
        self.open_home_page(driver)
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost:8080/addressbook/group.php")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
