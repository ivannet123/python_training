# -*- coding: utf-8 -*-
from model.group import Group


def test_rename_first_group(app):
    app.open_home_page()
    if app.group.count() == 0:
        app.group.create(Group(name="change_name_group"))
    app.group.modify_first_group(Group("new name", "", ""))


def test_change_first_group_header(app):
    app.open_home_page()
    if app.group.count() == 0:
        app.group.create(Group(name="change_header_group", header="header"))
    app.group.modify_first_group(Group("", "new header", ""))


def test_change_first_group_footer(app):
    app.open_home_page()
    if app.group.count() == 0:
        app.group.create(Group(name="change_footer_group", footer="footer"))
    app.group.modify_first_group(Group("", "", "new footer"))
