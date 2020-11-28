#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : Author.py
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

class Author(object):
    """docstring for Author."""

    def __init__(self, id: int, name: str = ""):
        super(Author, self).__init__()
        self.name = str(name)
        self.id = int(id)
        self.score = 0
        self.position = 0
        self.challenges = []  # List of Challenge objects
        self.solutions = []  # List of Solution objects
        self.validations = []  # List of Challenge objects

    def load(self, data: dict):
        if 'nom' in data.keys():
            self.name = data['nom']
        if 'score' in data.keys():
            self.score = int(data['score'])
        if 'position' in data.keys():
            self.position = int(data['position'])
        return self

    def __dict__(self):
        self.data_dict = {
            'id': self.id,
            'nom': self.name,
            'score': self.score,
            'position': self.position,
            'challenges': [],
            'solutions': [],
            'validations': [],
        }

    def __iter__(self):
        self.data_dict = {
            'id': self.id,
            'nom': self.name,
            'score': self.score,
            'position': self.position,
            'challenges': [],
            'solutions': [],
            'validations': [],
        }
        for key in self.data_dict.keys():
            yield (key, self.data_dict[key])

    def __repr__(self):
        return "<Author name=\"%s\", id=%d>" % (self.name, self.id)
