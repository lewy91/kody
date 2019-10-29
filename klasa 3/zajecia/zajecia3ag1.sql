DROP TABLE IF EXISTS osoby;
CREATE TABLE osoby (
    id_osoby INTEGER PRIMARY KEY AUTO_INCREMENT,
    imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
    nazwisko VARCHAR(30) NOT NULL CHECK (nazwisko <> ''),
    plec CHAR(1)
);
DROP TABLE IF EXISTS obiekty;
CREATE TABLE obiekty (
    id_obiektu INTEGER PRIMARY KEY AUTO_INCREMENT,
    nazwa VARCHAR(30)
);
DROP TABLE IF EXISTS zajecia;
CREATE TABLE zajecia (
    id_osoby INTEGER,
    id_obiektu INTEGER,
    id_zajec INTEGER PRIMARY KEY AUTO_INCREMENT,
    zajecia VARCHAR(30) NOT NULL CHECK (zajecia <> ''),
    cena integer,
    FOREIGN KEY (id_obiektu) REFERENCES obiekty (id_obiektu)
    ON DELETE CASCADE,
    FOREIGN KEY (id_osoby) REFERENCES osoby (id_osoby)
    ON DELETE CASCADE
);
DROP TABLE IF EXISTS wejscia;
CREATE TABLE wejscia (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_osoby INTEGER,
    id_zajec INTEGER,
    data DATE,
    FOREIGN KEY (id_osoby) REFERENCES osoby (id_osoby)
    ON DELETE CASCADE,
    FOREIGN KEY (id_zajec) REFERENCES zajecia (id_zajec)
    ON DELETE CASCADE
);




