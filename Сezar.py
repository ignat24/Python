from math import *
import random


B=list()
lang=int(input('1 - русский 2 - английский: '))
A=input('Введите слово: ')
def add(kluch):
    if(kluch>119):
        kluch=kluch-26
    if(kluch>87 and kluch<91):
        kluch=kluch-26
    kluch=kluch+3
    return kluch

def end1(kluch):
    print(kluch)
    if(kluch<1075 and kluch>1070):
        kluch=kluch+32
    if(kluch>1039 and kluch<1043):
        kluch=kluch+32
    kluch=kluch-3
    return kluch

def add1(kluch):
    if (kluch > 1069 and kluch < 1072):
        kluch = kluch - 32
    if(kluch>1100):
        kluch=kluch-32
    kluch=kluch+3
    return kluch

def end(kluch):
    if(kluch<100 and kluch >94):
        kluch=kluch+26
    if(kluch<68 ):
        kluch=kluch+26
    kluch=kluch-3
    return kluch

per2 = input('1 - Зашифровать\n2 - Расшифрование\n:')

for i in range(len(A)):
    kluch=ord(A[i])
    print(kluch)
    if(kluch==32):
        B.append(' ')
    else:
        if(lang==2):
            if(per2 == '1'):
                per1 = add(kluch)
            else:
                per1 = end(kluch)
        else:
            if (per2 == '1'):
                per1 = add1(kluch)
            else:
                per1 = end1(kluch)
        per = chr(per1)
        B.append(per)
print('Шифр Цезаря =',''.join(B))
