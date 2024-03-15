# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.add_new_contact(Contact("Ivan", "Ivanovich", "Ivanov", "Nickname", "photo.jpg",
                                     "example_title", "Roga i kopyta", "Lenina, 1",
                                     "+78127020411", "+79650000000", "88005553535",
                                     "+123456789", "email1@gmail.com", "email2@gmail.com", "email3@gmail.com",
                                     "www.google.com",
                                     "1", "February", "1977", "2", "March", "1988"))
    app.logout()


