#!/usr/bin/env python
# -*- coding: utf-8 -*-

STD_MAIL_OUT = 'mails.txt'
STD_URL_OUT = 'urls.txt'

OMITIR = [
    '.bmp',
    '.png',
    '.jpg',
    '.gif',

    '.zip',
    '.rar',
    '.gz',

    '.exe',
    '.msi',

    '.pdf',
    '.doc',
    '.ppt',
    '.odt',

    #tags de sitios a omitir
    'google',
    'yahoo',
    'mozilla',
    'wikipedia',
    'creativecommons',
]

VALIDOS = [
    'hotmail.com',
    'hotmail.es',
    'gmail.com',
    'yahoo.com.ar',
    'yahoo.com',
    'msn.com' ,
    'live.com.ar',
    'argentina.com',

    '.com.ar',
    '.org.ar',
    '.edu.ar',

    #'infovia.com.ar',
    #'sancristobalseguros.com.ar',
    #'ole.com',
    #'latinmail.com',
    #'aol.com',
    #'terra.es',
    #'sinectis.com.ar',
    #'arnet.com.ar',
    #'fibertel.com.ar',
    #'ciudad.com.ar',
    #'uolsinectis.com.ar',

]

REPLACE = {
    'msm.com':'msn.com',
    'hotmail.co':'hotmail.com',
    'hotmial.':'hotmail.',
    'homail.':'hotmail.',
    'terrra.':'terra.'
}


TOKENS = [
    '(',
    ')',
    '<',
    '>',
    '"',
    "'",
    ';',
    ':',
    '=',
    "",
    '?',
    ',',
    '/',
]
