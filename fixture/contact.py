from selenium.webdriver.support.ui import Select
import os


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def fill_contact_information(self, contact):
        wd = self.app.wd

        if contact.firstname:
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename:
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
        if contact.lastname:
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname:
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.photo_path:
            absolute_path = os.path.abspath(contact.photo_path)
            wd.find_element_by_name("photo").send_keys(absolute_path)
        if contact.title:
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)
        if contact.company:
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company)
        if contact.address:
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.home_phone:
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.home_phone)
        if contact.mobile_phone:
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        if contact.work_phone:
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.work_phone)
        if contact.fax_phone:
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contact.fax_phone)
        if contact.email1:
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email1)
        if contact.email2:
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3:
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.homepage:
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if contact.bday_day:
            dropdown_element = wd.find_element_by_name("bday")
            dropdown_select = Select(dropdown_element)
            dropdown_select.select_by_visible_text(contact.bday_day)
        if contact.bday_month:
            dropdown_element = wd.find_element_by_name("bmonth")
            dropdown_select = Select(dropdown_element)
            dropdown_select.select_by_visible_text(contact.bday_month)
        if contact.bday_year:
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.bday_year)
        if contact.ann_day:
            dropdown_element = wd.find_element_by_name("aday")
            dropdown_select = Select(dropdown_element)
            dropdown_select.select_by_visible_text(contact.ann_day)
        if contact.ann_month:
            dropdown_element = wd.find_element_by_name("amonth")
            dropdown_select = Select(dropdown_element)
            dropdown_select.select_by_visible_text(contact.ann_month)
        if contact.ann_year:
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contact.ann_year)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_information(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt='Edit']").click()
        self.fill_contact_information(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))
