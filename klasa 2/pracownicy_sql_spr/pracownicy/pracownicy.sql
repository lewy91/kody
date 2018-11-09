DROP TABLE IF EXISTS  pracownicy;
CREATE TABLE pracownicy(
    id_p INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    kod TEXT,
    miasto_z TEXT,
    ulica TEXT,
    data_u DATE,
    miasta_u TEXT
);
DROP TABLE IF EXISTS  place;
CREATE TABLE place(
    id_p INTEGER PRIMARY KEY AUTOINCREMENT,
    id_s INTEGER,
    placa INTEGER,
    data_z DATE,
     FOREIGN KEY(id_p) REFERENCES pracownicy(id_p) ON DELETE CASCADE ON UPDATE NO ACTION
);
DROP TABLE IF EXISTS  kontakty;
CREATE TABLE kontakty(
    id_pracownika INTEGER PRIMARY KEY AUTOINCREMENT,
    typ_k BOOLEAN,
    kontakt TEXT,
    uwagi TEXT,
     FOREIGN KEY(id_pracownika) REFERENCES pracownicy(id_p) ON DELETE CASCADE ON UPDATE NO ACTION
);
DROP TABLE IF EXISTS  stanowiska;
CREATE TABLE stanowiska (
    id_s INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT,
 FOREIGN KEY(id_s) REFERENCES place(id_s) ON DELETE CASCADE ON UPDATE NO ACTION
 );
