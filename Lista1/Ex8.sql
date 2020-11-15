-- item (a)

UPDATE Personalidade
SET nascimento = '1815'
WHERE id = 2

-- item (b)

INSERT INTO Area
VALUES ("Estatística")

-- item (c)

INSERT INTO Area
VALUES("Literatura");

INSERT INTO Personalidade
VALUES (8, "Alice Munro", "Literatura",1931,'S');

-- item (d)

DELETE FROM Personalidade
WHERE area = "Astronomia";

DELETE FROM Area
WHERE nome = "Astronomia";

-- item (e)

INSERT INTO Area
VALUES("Enfermagem");

INSERT INTO Personalidade(id, nome, area)
VALUES(9, "Florence Nightingale", "Enfermagem");
