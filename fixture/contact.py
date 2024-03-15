from selenium.webdriver.support.ui import Select
import os


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        absolute_path = os.path.abspath(contact.photo_path)
        wd.find_element_by_name("photo").send_keys(absolute_path)
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
