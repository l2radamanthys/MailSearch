#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *
import re

#exprecion para verificar si el mail es valido extraido del parser de Django
#
EMAIL_RE_VALID = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$', re.IGNORECASE)  # domain+


#exprecion mas sencilla que se usa en la busqueda de mails
EMAIL_RE_SEARCH = re.compile("[\w\.]{1,60}@[\w\.]{1,30}")


def es_html(url):
    """
        pregunta si la url que se pasa hace referencia a un
        archivo html o de texto y no a un archivo binario definido
        en omitir. devo buscar una mejor forma
    """
    for tag in OMITIR:
        if tag in url:
            return False
    return True


def es_email(value):
    if EMAIL_RE_VALID.search(value):
        return True
    else:
        return False
