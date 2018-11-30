#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py

from modele import*

def kw01():
    #Uczen.select().where(Uczen.imie.startswith('G'))
    for row in obj:
        print(row.nazwisko, row.imie)
        Uczen.select().where(Uczen.imie == 'Rafał')

def main(args):
    baza.connect()
    
    kw01()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
