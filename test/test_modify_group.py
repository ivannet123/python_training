# -*- coding: utf-8 -*-
from model.group import Group


def test_rename_first_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group("new name", "", ""))
    app.session.logout()


def test_change_first_group_header(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group("", "new header", ""))
    app.session.logout()


def test_change_first_group_footer(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group("", "", "new footer"))
    app.session.logout()
