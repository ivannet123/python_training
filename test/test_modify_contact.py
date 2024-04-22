# -*- coding: utf-8 -*-
from model.contact import Contact


def test_change_first_contact_name(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact_to_change_name"))
    app.contact.modify_first_contact(Contact(firstname="new_name"))


def test_change_first_contact_middlename(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="name", middlename="middlename"))
    app.contact.modify_first_contact(Contact(middlename="new_middle_name"))


def test_change_first_contact_lastname(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="name", lastname="lastname"))
    app.contact.modify_first_contact(Contact(lastname="new_last_name"))
