# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.create(Group("groupnameeee", "headerrrrr", "commenttttt"))
    app.session.logout()
    time.sleep(1)


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
    time.sleep(1)
