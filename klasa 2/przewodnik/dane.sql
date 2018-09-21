DROP TABLE IF EXISTS miasta;
CREATE TABLE miasta
(
    id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
    Nazwa_miasta TEXT(30),
    Województwo TEXT(30)
    );
    
DROP TABLE IF EXISTS powierzchnie;
CREATE TABLE powierzchnie 
( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Powierzchnia_miasta DECIMAL,
    Powierzchnia_terenow_zielonych DECIMAL,
    Data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY(id_miasta) REFERENCES miasta(id_miasta)
    );
DROP TABLE IF EXISTS dane_gus;
CREATE TABLE dane_gus
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Liczba_mieszkancow INTEGER,
    Liczba_kobiet INTEGER,
    Grupa_wiekowa TEXT,
    Data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES maista(id_miasta)
);
    
