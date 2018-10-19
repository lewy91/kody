DROP TABLE IF EXISTS tabela uczniowie:
CREATE TABLE uczniowie(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    plec BOOLEAN,
    id_klasa INTEGER NOT NULL,
    egz_hum NUMERIC,
    egz_mat NUMERIC,
    egz_jez NUMERIC,
    FOREIGN KEY(id_klasa) REFERENCES klasy(id)
    ON DELETE NO ACTION ON UPDATE NO ACTION
);
DROP TABLE IF EXISTS tabela klasy:
CREATE TABLE klasy(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    klasa TEXT,
    rok_naboru INTEGER,
    rok_matury INTEGER
);
DROP TABLE IF EXISTS tabela przedmioty:
CREATE TABLE przedmioty(
id INTEGER PRIMARY KEY AUTOINCREMENT,
przedmiot TEXT,
nazwisko_naucz TEXT,
imie_naucz TEXT,
plec_naucz BOOLEAN
);
DROP TABLE IF EXISTS tabela oceny:
CREATE TABLE oceny (
id INTEGER PRIMARY KEY AUTOINCREMENT,
datad DATE,
id_uczen INTEGER,
id_przedmiot INTEGER,
ocena DECIMAL,
 FOREIGN KEY(id_przedmiot) REFERENCES uczniowie(id)
 FOREIGN KEY(id_uczen) REFERENCES przedmioty(id)
 );
