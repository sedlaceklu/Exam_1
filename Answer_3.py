query_1 = """
    CREATE TABLE Readers(
    id serial PRIMARY KEY,
    name varchar(60),
    email varchar(60) UNIQUE,
    is active boolean NOT NULL DEFAULT true
):
"""

query_2 = """
    CREATE TABLE PublishingHouses(
    id serial PRIMARY KEY,
    name varchar(60),
    city varchar(20),
    adress varchar(120)
):
"""

query_3 = """
    CREATE TABLE Books(
    id serial PRIMARY KEY,
    title varchar(60),
    price decimal(5,2),
    author varchar(60),
    publishing_houses_id int REFERENCES PublishingHouses(id)
):
"""

query_4 = """
    CREATE TABLE Readers_Books(
    reader_id int REFERENCES Readers(id),
    book_id int REFERENCES Books(id),
    PRIMARY KEY(reader_id, book_id)
):
"""

query_5 = """
    SELECT *
    FROM Books
    WHERE price > 10;
"""

query_6 = """
    INSERT INTO PublishingHouses(name, city, adress)
    VALUES ('Super books', 'Wilderness', '120 Main road ');
"""

query_7 = """
    DELETE FROM Books
    WHERE id = 12
"""
query_8 = """
    SELECT DISTINCT Readers. *
    FROM Readers
    JOIN Readers_Books ON Readers.id = Readers_Books.reader_id
"""

query_9 = """
    UPDATE Readers
    SET is_active = false
    WHERE id = 2;
"""

query_10 = """
    ALTER TABLE Readers
    ADD COLUMN date_of_birth date NULL;
"""

