#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    exporta los mails a una DB en SQLite
"""

import sqlite3 as dbapi
import os


def crear_bd():
    print "creando BD"
    conecion = dbapi.connect("mails.db")
    cursor = conecion.cursor()
    #ejecutamos un instrucion sql en este caso creamos una tabla
    cursor.execute( """CREATE TABLE Mails(
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        email VARCHAR(60) UNIQUE);""")
    conecion.commit()
    cursor.close()


def cargar_txt():
    os.system('clear')
    f_name = raw_input('file: ')
    data = open(f_name, 'r').readlines()

    conecion = dbapi.connect("mails.db")
    cursor = conecion.cursor()

    for mail in data:
        mail = mail.replace("\n", "")
        mail = mail.replace(" ", "")
        instr_sql = "INSERT INTO Mails(email) VALUES(\"%s\")" %mail
        try:
            cursor.execute(instr_sql)
        except:
            print "ERROR", mail
        conecion.commit()
    cursor.close()


def export_txt():
    f = open('db_mails.txt', 'w')
    conecion = dbapi.connect("mails.db")
    cursor = conecion.cursor()
    instr_sql = "SELECT * FROM Mails"
    cursor.execute(instr_sql)
    for id,mail in cursor.fetchall():
        f.write("%s - %s\n" %(com(id), mail))
    f.close()


def menu():
    os.system('clear')
    print """
    1 - Cargar archivo de texto
    2 - Exportar a Texto Plano
    3 - Exportar a CSV
    4 - Mostrar todos
    5 - crear BD
    0 - Salir
    """
    return raw_input("opc: ")


def com(num):
    """completa con 0 un numero entero de 5 cifras"""
    if num < 10:
        cad = '0000'+str(num)
    elif num < 100:
        cad = '000'+str(num)
    elif num < 1000:
        cad = '00'+ str(num)
    elif num < 10000:
        cad = '0'+ str(num)
    else:
        cad = str(num)
    return cad


def main():
    loop = True
    while loop:
        opc = menu()
        if opc == "1":
            cargar_txt()
            raw_input('CARGA COMPLETA')

        elif opc == "2":
            export_txt()
            raw_input('BD EXPORTADA')

        elif opc == "3":
            pass

        elif opc == "5":
            crear_bd()

        elif opc == "0":
            print "BYE"
            loop = False

        else:
            raw_input("opcion invalidar ->")


if __name__ == '__main__':
    main()
