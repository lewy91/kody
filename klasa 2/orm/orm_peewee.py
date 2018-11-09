#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py

import os
from peewee import*

baza_plik ='test.db'
baza =SqliteDatabase(baza_plik)

### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(BazaModel):
    nazwa = charField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
class Uczen(BazaModel):
    imie = charField(null=False)
    nazwisko = charField(null=False)
    plec= Boolean()
    uczen = ForeignKeyField(Klasa, related_name= 'uczniowie')
    
class Wynik(BazaModel):
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name= 'wyniki')
    
def main(args):
    if os.path_exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() #połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wyniki])
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
