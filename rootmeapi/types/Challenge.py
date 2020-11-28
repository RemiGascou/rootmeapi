#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : Challenge.py
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*


class Challenge(object):
    """docstring for Challenge."""

    def __init__(self, id: int):
        super(Challenge, self).__init__()
        self.id = id

    def load(self, data: dict):
        if 'name' in data.keys():
            self.name = data['name']
        return self

    def __repr__(self):
        return "<Challenge id=%d>" % (self.id)
