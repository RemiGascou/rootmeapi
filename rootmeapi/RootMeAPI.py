#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import getpass
import json

import requests

from .types import *


class RootMeAPI(object):
    """
    Documentation for RootMeAPI
    """

    def __init__(self, debug=False):
        super(RootMeAPI, self).__init__()
        self.debug_status = debug
        self.debug("RootMeAPI.__init__()")
        self.api_link = 'https://api.www.root-me.org'
        self.credentials = {'connected': False, 'cookies': {}}

    def login(self, login, password=""):
        """
        Documentation for login
        """
        self.debug("login(\"%s\",\"%s\")" % (login.lower(), '*' * 15))
        if password == "":
            password = getpass.getpass("[RootMe] Password : ")
        # Sending request
        r = requests.post(
            self.api_link + '/login',
            data={
                'login': login.lower(),
                'password': password
            }
        )
        del password
        response = json.loads(r.content)[0]
        if 'error' in response.keys():
            self.debug("Error %s : %s" % (response['error']['code'], response['error']['message']), level='warn')
            self.debug("Not connected.", level='warn')
        elif 'info' in response.keys():
            if "spip_session" in response['info'].keys() and response['info']['code'] == 200:
                self.credentials = {
                    'connected': True,
                    'cookies': {
                        "spip_session": response['info']["spip_session"]
                    }
                }
                self.debug("spip_session=%s" % self.credentials['cookies']['spip_session'], level='info')
                self.debug('Successfully connected !', level='info', force=True)
                return True
        return False

    def get_challenges(self):
        """
        Documentation for get_challenges
        """
        self.debug("get_challenges()")
        # Sending request
        r = requests.get(
            self.api_link + '/challenges',
            cookies=self.credentials['cookies']
        )
        response = json.loads(r.content)[0]
        return response

    def get_challenge_by_id(self, id: int):
        """
        Documentation for get_challenge_by_id
        """
        self.debug("get_challenges(%d)" % id)
        # Sending request
        r = requests.get(
            self.api_link + '/challenges/%d' % id,
            cookies=self.credentials['cookies']
        )
        response = json.loads(r.content)[0]
        return response

    def get_authors(self, start_index=0):
        """
        Documentation for get_authors
        """
        self.debug("get_authors()")
        # Sending request
        r = requests.get(
            self.api_link + '/auteurs?debut_auteurs=%d' % start_index,
            cookies=self.credentials['cookies']
        )
        response = json.loads(r.content)
        return response

    def get_author_by_id(self, id: int):
        """
        Documentation for get_author_by_id
        """
        self.debug("get_author_by_id(%d)" % id)
        # Sending request
        r = requests.get(
            self.api_link + '/auteurs/%d' % id,
            cookies=self.credentials['cookies']
        )
        return Author(int(id)).load(json.loads(r.content))

    def search_author_by_name(self, name: str):
        """
        Documentation for search_author_by_name
        """
        self.debug("search_author_by_name(\"%s\")" % name)
        # Sending request
        r = requests.get(
            self.api_link + '/auteurs?nom=%s' % name,
            cookies=self.credentials['cookies']
        )
        response = json.loads(r.content)[0]
        results = [
            Author(int(response[key]['id_auteur']), response[key]["nom"])
            for key in response.keys()
        ]
        return results

    def get_ctfatd(self):
        """
        Documentation for get_ctfatd
        """
        self.debug("get_ctfatd")
        # Sending request
        r = requests.get(
            self.api_link + '/environnements_virtuels',
            cookies=self.credentials['cookies']
        )
        response = json.loads(r.content)[0]
        return response

    def get_ctfatd_by_id(self, id: int):
        """
        Documentation for get_ctfatd
        """
        self.debug("get_ctfatd_by_id(%d)" % id)
        # Sending request
        r = requests.get(
            self.api_link + '/environnements_virtuels/%d' % id,
            cookies=self.credentials['cookies']
        )
        response = json.loads(r.content)[0]
        return response

    # Debugging
    def debug(self, message: str, level='debug', force=False):
        """
        Documentation for debug function :

        Prints a debug message

        Parameters :
         - message : String
        """
        if self.debug_status == True or force == True:
            if level == 'warn':
                print("\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m " + message)
            elif level == 'debug':
                print("\x1b[1m[\x1b[93mDEBUG\x1b[0m\x1b[1m]\x1b[0m " + message)
            elif level == 'info':
                print("\x1b[1m[\x1b[92mINFO\x1b[0m\x1b[1m]\x1b[0m " + message)
            else:
                print("\x1b[1m[\x1b[93mDEBUG\x1b[0m\x1b[1m]\x1b[0m " + message)
        else:
            if level == 'warn':
                print("\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m " + message)

        return None
