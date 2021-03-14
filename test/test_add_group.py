# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
        app.group.create(Group(name="name gr1111", header="header222", footer="footer333"))

def test_add_empty_group(app):
        app.group.create(Group(name="", header="", footer=""))


