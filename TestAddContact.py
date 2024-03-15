# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact


def is_alert_present(self):
    try:
        self.wd.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.login(wd, "admin", "secret")
        self.add_new_contact(wd, Contact("Ivan", "Ivanovich", "Ivanov", "Nickname",
                                         "example_title", "Roga i kopyta", "Lenina, 1",
                                         "+78127020411", "+79650000000", "88005553535",
                                         "+123456789", "email1@gmail.com", "email2@gmail.com", "email3@gmail.com",
                                         "www.google.com",
                                         "1", "February", "1977", "2", "March", "1988"))
        self.logout(wd)

    def add_new_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_phone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()

        dropdown_element = wd.find_element_by_name("bday")
        dropdown_select = Select(dropdown_element)
        dropdown_select.select_by_visible_text(contact.bday_day)

        dropdown_element = wd.find_element_by_name("bmonth")
        dropdown_select = Select(dropdown_element)
        dropdown_select.select_by_visible_text(contact.bday_month)

        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.bday_year)

        dropdown_element = wd.find_element_by_name("aday")
        dropdown_select = Select(dropdown_element)
        dropdown_select.select_by_visible_text(contact.ann_day)

        dropdown_element = wd.find_element_by_name("amonth")
        dropdown_select = Select(dropdown_element)
        dropdown_select.select_by_visible_text(contact.ann_month)

        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ann_year)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
