DROP TABLE IF EXISTS zamowienie;
CREATE TABLE zamowienie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Numer_Zamowienia INTEGER,
    Adres_Klienta TEXT,
    Data_Zamowienia DATE,
    Szczegoly_Zamowienia TEXT,
    );
DROP TABLE IF EXISTS zamowienie2;
CREATE TABLE zamowienie2
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Klienta INTEGER,
    Nazwa_Klienta TEXT,
    Adres TEXT,
    Kod_Pocztowy TEXT,
    Miasto TEXT,
    Wojewodztwo TEXT
    );
DROP TABLE IF EXISTS zamowienie3;
CREATE TABLE zamowienie3    
