#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import urllib

from mi_parser import URLParser
from constantes import *


def analizer(url_list=[], mail_list=[], n_iter=1):
    #si la iteracion no es 0 tiene que seguir buscando mails en las urls
    if n_iter != 0:
        print 'ITER:',n_iter
        id = len(url_list) - 1
        scan_list = list(url_list[id])
        n_list, n_mlist = scan_urls(scan_list)
        url_list.append(n_list)
        mail_list += n_mlist
        del n_list

        analizer(url_list, mail_list, n_iter-1)

    else:
        url_file = open(STD_URL_OUT, 'w')
        for lista in url_list:
            for url in lista:
                url_file.write('%s \n' %url)
        url_file.close()

        mail_file = open(STD_MAIL_OUT, 'w')
        for mail in list(mail_list):
            mail_file.write("%s \n" %mail)
        mail_file.close()

        print 'total de mails', len(list(mail_list))



def scan_urls(url_list):
    mi_parser = URLParser()
    urls = []
    for url in url_list:
        print url
        try:
            sock = urllib.urlopen(url)
            html = sock.read()
            sock.close()
        except:
            continue

        mi_parser.set_url(url)
        mi_parser.feed(html)
        mi_parser.close()

        urls.extend(list(mi_parser.urls))
        mi_parser.restart()
    print 'total de mails', len(mi_parser.mails)
    return urls, mi_parser.mails


def main():
    f = open('salida.txt', 'w')
    sys.stdout = f

    urls_ini = [
        "http://elistas.egrupos.net/lista/bonsaisuiseki/archivo/indice/2899/msg/2943/",
    ]
    iter = 3
    analizer([urls_ini], [], iter)

    f.close()



if __name__ == '__main__':
    main()
