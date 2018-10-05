#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def kwerenda_1(cur):
    cur.execute("""
        SELECT name AS nazwa, genre AS gatunek FROM apps
     """)

    wyniki = cur.fetchall()  # pobranie wszystkich rekordów na raz
    for row in wyniki:  # odczytanie rekordów
        print(tuple(row))  # drukowanie pól


def main(args):
    con = sqlite3.connect('szkola.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('szkola.sql', 'r') as plik:
        cur.executescript(plik.read())

     #dodawanie danych do bazy
    dane = dane_z_pliku('szkoła_z6pr052010_oceny.txt')
    dane.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO oceny VALUES(?, ?, ?, ?)', oceny)

    dane = dane_z_pliku('szkoła_z6pr052010_przedmioty.txt')
    dane.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO przedmioty VALUES(?, ?, ?, ?)', przedmiot)
    
    dane = dane_z_pliku('szkoła_z6pr052010_uczniowie.txt')
    dane.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO uczniowie VALUES(?, ?, ?, ?, ?, ?)', uczniowie)
    
    # przykład zapytania (kwerendy)
    con.commit()
    con.close()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
