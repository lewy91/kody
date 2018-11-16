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
        
class Klasy(BazaModel):
    klasa= CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    

class Uczniowie (BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec= BooleanField()
    klasa = ForeignKeyField(Klasy, related_name='uczniowie')
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)

    

    
class Przedmioty(BazaModel):
   przedmiot= CharField(null=False)
   imienaucz= CharField(null=False)
   nazwiskonaucz= CharField(null=False)
   plecnaucz= BooleanField()
    
class Oceny(BazaModel):

    datad=DataTimeField()
    uczen=ForeignKeyField(Uczniowie, related_name='oceny')
    przedmiot= ForeignKeyField(Przedmioty, related_name='oceny')
    ocena= DecimaField(null=False)
    
def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() #połączenie z bazą
    baza.create_tables(Klasy, Uczen, Przedmioty, Oceny)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
