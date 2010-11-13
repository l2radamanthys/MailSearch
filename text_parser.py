

from constantes import *



def correg(cad):
    for tok in TOKENS:
        cad = cad.replace(tok,' ')
    cad = cad.replace(" ","")
    return cad


def validar(mail):
    """
    """
    for ele in VALIDOS:
        if ele in mail.lower():
            return True
    return False


def replace(mail):
    for tag in REPLACE:
        if tag in mail.lower():
            mail = mail.replace(tag, REPLACE[tag])
            return mail
    return mail


def main():
    f_name = raw_input('file: ')
    f = open(f_name, 'r')
    data = f.readlines()
    list = []
    olist = []

    for ele in data:
        print ele
        ele = correg(ele)
        ele = replace(ele)
        if validar(ele):
            if not(ele in list):
                list.append(ele)
        else:
            if not(ele in olist):
                olist.append(ele)

    file = open(f_name + '_val.txt','w')
    for ele in list:
        file.write(ele)
    file.close()

    file = open(f_name + '_omi.txt','w')
    for ele in olist:
        file.write(ele)
    file.close()


if __name__ == '__main__':
    main()
