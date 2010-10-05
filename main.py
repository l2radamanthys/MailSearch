#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *
import urllib
from parser import URLParser


def analizer(url_list=[set()], mail_list=set(), n_iter=1):
    #si la iteracion no es 0 tiene que seguir buscando mails en las urls
    if n_iter != 0:
        id = len(url_list) - 1
        scan_list = list(url_list[id])
        n_list, n_mlist = scan_urls(scan_list)
        url_list.append(n_list)
        del n_list

    else:
        url_file = open(STD_URL_OUT, 'w')
        for lista in url_list:
            for url in lista:
                url_file.write('%s \n' %url)
        url_file.close()

        mail_file = open(STD_MAIL_OUT, 'w')
        for mail in list(mail_list):
            mail_file.write("%s\n" %mail)
        mail_file.close()

        print 'total de mails', len(list(mail_list))


def scan_urls(url_list):
    mi_parser = URLParser()
    urls = []
    for url in url_list:
        sock = urllib.urlopen(url)
        html = sock.read()
        sock.close()

        mi_parser.set_url(url)
        mi_parser.feed(html)
        mi_parser.close()

        urls.extend(list(mi_parser.urls))
        mi_parser.restart()

    return urls, mi_parser.mails


def main():
    url_ini = "http://www.l2radamanthys.com.ar"
    iter = 1
    analizer(url_list=[set(url_ini)], n_iter=iter)


if __name__ == '__main__':
    main()
