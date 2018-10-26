#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3


def kwerenda1(cur):
    cur.execute("""
    SELECT imie, nazwisko, COUNT(ocena) AS poile FROM uczniowie INNER JOIN oceny ON uczniowie.id=oceny.id_uczen GROUP BY uczniowie.id ORDER BY poile DESC
    """)
    #("""SELECT imie, nazwisko, AVG(ocena) FROM uczniowie INNER JOIN oceny ON uczniowie.id=oceny.id_uczen WHERE nazwisko = 'Nowak' AND imie ='Dorota'""")
    #SELECT klasa, COUNT(uczniowie.id) AS ile FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa ORDER BY ile DESC
    #SELECT klasa, COUNT(*) FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa
    #SELECT COUNT(*) FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa WHERE klasa ='1A' 
    #SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie WHERE plec = 1 ORDER BY egz_hum DESC LIMIT 5
    #SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowieWHERE imie LIKE '%a' ORDER BY egz_hum DESC LIMIT 5
    #SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie ORDER BY egz_hum DESC LIMIT 5
    #SELECT * FROM uczniowie WHERE nazwisko = 'Lewandowski' AND imie = 'Seba'
    #SELECT egz_hum, egz_mat FROM uczniowie WHERE nazwisko = 'Lewandowski' AND imie = 'Seba'
    #SELECT COUNT(*) FROM uczniowie WHERE nazwisko LIKE 'G%'
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)
        
    
def main(args):
    baza_nazwa ='uczniowie'
    tabele= ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda1(cur)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
