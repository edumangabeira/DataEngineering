-- criando e povoando as tabelas

CREATE TABLE t_aluno(
matricula TEXT,
nome TEXT,
municipio TEXT,
idade INT,
PRIMARY KEY(matricula)
);

CREATE TABLE t_resultado(
matricula TEXT,
exame INT,
nota FLOAT,
PRIMARY KEY(matricula),
FOREIGN KEY(matricula) REFERENCES t_aluno(matricula)
);

INSERT INTO t_aluno
VALUES('m1', "Jonathan Faro", "Nova Iguaçu", NULL);

INSERT INTO t_aluno
VALUES('m2', "Carlos Berger", "Cabo Frio", 31);

INSERT INTO t_aluno
VALUES('m3', "Elisa Palmeirão", "Duque de Caxias", 22);

INSERT INTO t_aluno
VALUES('m4', "Marta Silva", NULL, NULL);


INSERT INTO t_resultado
VALUES('m1', 1, 6.4);

INSERT INTO t_resultado
VALUES('m1', 2, 8.2);

INSERT INTO t_resultado
VALUES('m2', 1, 3.4);

INSERT INTO t_resultado
VALUES('m3', 1, 5.4);

INSERT INTO t_resultado
VALUES('m3', 2, 9.8);

INSERT INTO t_resultado
VALUES('m4', 1, 7.9);

INSERT INTO t_resultado
VALUES('m4', 2, 8.6);


-- item (a)

SELECT a.matricula, a.nome, a.municipio, b.exame, b.nota FROM t_aluno a
NATURAL JOIN t_resultado b
ORDER BY a.nome, b.exame;

-- item (b)

SELECT a.matricula, a.nome, a.municipio, b.exame, b.nota FROM t_aluno a
NATURAL JOIN t_resultado b
WHERE b.exame = 1
AND b.nota < 5.0

-- item (c)

SELECT matricula, nome FROM t_aluno
WHERE municipio IS NULL
OR idade IS NULL

-- item (d)

SELECT idade FROM t_aluno
JOIN
(SELECT idade FROM t_aluno)
EXCEPT
SELECT idade FROM t_aluno WHERE idade IS NULL
ORDER BY idade DESC
LIMIT 1

-- item (e)

CREATE TABLE Relatorio(
matricula TEXT,
media_final FLOAT,
FOREIGN KEY(matricula) REFERENCES t_aluno(matricula)
);

INSERT INTO Relatorio
SELECT a.matricula, (a.nota + b.nota)/2 as media_final
FROM t_resultado a, t_resultado b
WHERE a.exame= 1
AND b.exame = 2
AND a.matricula = b.matricula
