#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sgmllib import SGMLParser

from extras import *
from constantes import *


class URLParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.urls = set()
        self.mails = set()
        self.url = ''


    def set_url(self, url=''):
        self.url = url


    def reset(self):
        SGMLParser.reset(self)
        self.url = ''
        self.urls = set()
        self.mails = set()


    def restart(self):
        SGMLParser.reset(self)
        self.urls = set()
        self.url = ''


    def add_email(self, value):
        if not(value in self.mails):
            self.mails.add(value.lower())


    def start_a(self, attrs):
        for tag, value in attrs:
            tag = tag.lower()
            if tag == 'href' and len(value) > 7:
                if value[:4] != 'http':
                    if 'mailto' in value:
                        self.handle_data(value.split(':')[1])
                        self.handle_data(value)

                    elif self.url != '':
                        value = self.url + '/' + value
                    else:
                        print "Omitido, ", value
                elif es_html(value):
                    self.urls.add(value)


    def handle_data(self, text):
        """
            por el momento esta funcion solo extrae los mails del cont
            falta implementar la busqueda y extracion de dir webs
        """
        if text != '':
            mails = EMAIL_RE_SEARCH.findall(text)
            for mail in mails:
                if is_valid_email(mail):
                    self.add_email(mail)

