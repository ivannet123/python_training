# -*- coding: utf-8 -*-
from model.contact import Contact
import time


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="Ivan",
                               middlename="Ivanovich",
                               lastname="Ivanov",
                               nickname="Nickname",
                               photo_path="photo.jpg",
                               title="example_title",
                               company="Roga i kopyta",
                               address="Lenina, 1",
                               home_phone="+78127020411",
                               mobile_phone="+79650000000",
                               work_phone="88005553535",
                               fax_phone="+123456789",
                               email1="email1@gmail.com",
                               email2="email2@gmail.com",
                               email3="email3@gmail.com",
                               homepage="www.google.com",
                               bday_day="1",
                               bday_month="February",
                               bday_year="1977",
                               ann_day="2",
                               ann_month="March",
                               ann_year="1988"
                            ))
    app.session.logout()
    time.sleep(1)
