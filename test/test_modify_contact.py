# -*- coding: utf-8 -*-
from model.contact import Contact


def test_change_first_contact_name(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(firstname="new_name",
                                             middlename="",
                                             lastname="",
                                             nickname="",
                                             photo_path="",
                                             title="",
                                             company="",
                                             address="",
                                             home_phone="",
                                             mobile_phone="",
                                             work_phone="",
                                             fax_phone="",
                                             email1="",
                                             email2="",
                                             email3="",
                                             homepage="",
                                             bday_day="",
                                             bday_month="",
                                             bday_year="",
                                             ann_day="",
                                             ann_month="",
                                             ann_year=""))
    app.session.logout()


def test_change_first_contact_middlename(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(firstname="",
                                             middlename="new_middle_name",
                                             lastname="",
                                             nickname="",
                                             photo_path="",
                                             title="",
                                             company="",
                                             address="",
                                             home_phone="",
                                             mobile_phone="",
                                             work_phone="",
                                             fax_phone="",
                                             email1="",
                                             email2="",
                                             email3="",
                                             homepage="",
                                             bday_day="",
                                             bday_month="",
                                             bday_year="",
                                             ann_day="",
                                             ann_month="",
                                             ann_year=""))
    app.session.logout()


def test_change_first_contact_lastname(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(firstname="",
                                             middlename="",
                                             lastname="new_last_name",
                                             nickname="",
                                             photo_path="",
                                             title="",
                                             company="",
                                             address="",
                                             home_phone="",
                                             mobile_phone="",
                                             work_phone="",
                                             fax_phone="",
                                             email1="",
                                             email2="",
                                             email3="",
                                             homepage="",
                                             bday_day="",
                                             bday_month="",
                                             bday_year="",
                                             ann_day="",
                                             ann_month="",
                                             ann_year=""))
    app.session.logout()
