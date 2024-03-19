# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.create(Group("groupnameeee", "headerrrrr", "commenttttt"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
