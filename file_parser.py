#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Analiza un archivo de texto plano en busca de Direciones de Email
"""

from extras import *
from constantes import *


FILTRAR = False #si se aplicara filtro de mails

CAR_FILTRAR =  [
    "<",
    ">",
    ",",
    ":",
    ";",
]

def remueve_car(line, rep=" "):
    """
        remueve caracteres extraños que aveses molestan un poco
    """
    for car in CAR_FILTRAR:
        line = line.replace(car, rep)
    return line


def main():

    f_name = raw_input('text: ')
    pars_file = open(f_name, 'r')
    out_file = open('out.txt', 'w')
    data = pars_file.readlines()
    pars_file.close()

    print "INIT"

    for line in data:
        line = remueve_car(line)
        #print line
        mails = EMAIL_RE_SEARCH.findall(line)
        for mail in mails:
            if FILTRAR:
                if is_valid_email(mail):
                    out_file.write('%s \n' %mail)
                    print mail
            else:
                out_file.write('%s \n' %mail)
                print mail

    out_file.close()
    print "END"


if __name__ == '__main__':
    main()
