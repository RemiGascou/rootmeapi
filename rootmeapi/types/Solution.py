#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : Solution.py
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

class Solution(object):
    """docstring for Solution."""

    def __init__(self, id: int, url=""):
        super(Solution, self).__init__()
        self.id = int(id)
        self.url = url

    def load(self, data: dict):
        if 'name' in data.keys():
            self.name = data['name']
        return self

    def __repr__(self):
        return "<Solution id=%d>" % (self.id)
