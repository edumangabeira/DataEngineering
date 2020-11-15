-- item A

CREATE TABLE LogAcesso(
idSessao INT NOT NULL,
nomPagina TEXT NOT NULL,
PRIMARY KEY (idSessao, nomPagina)
)

-- item B

INSERT INTO LogAcesso(idSessao, nomPagina)
VALUES (10001, "Free_Downloads");

INSERT INTO LogAcesso(idSessao, nomPagina)
VALUES (10001, "Games");

INSERT INTO LogAcesso(idSessao, nomPagina)
VALUES (10001, "Sports");

INSERT INTO LogAcesso(idSessao, nomPagina)
VALUES (10002, "Knowledge_Base");

INSERT INTO LogAcesso(idSessao, nomPagina)
VALUES (10003, "Free_Downloads");

INSERT INTO LogAcesso(idSessao, nomPagina)
VALUES (10003, "Products");

INSERT INTO LogAcesso(idSessao, nomPagina)
VALUES (10004, "Games");

INSERT INTO LogAcesso(idSessao, nomPagina)
VALUES (10004, "News");

INSERT INTO LogAcesso(idSessao, nomPagina)
VALUES (10004, "Web_Site_Gallery")

-- item C

SELECT idSessao FROM LogAcesso WHERE nomPagina = "Free_Downloads"
INTERSECT
SELECT idSessao FROM LogAcesso WHERE nomPagina = "Games"
INTERSECT
SELECT idSessao FROM LogAcesso WHERE nomPagina = "Sports";

-- item D

SELECT idSessao FROM LogAcesso WHERE nomPagina = "Free_Downloads"
EXCEPT
SELECT idSessao FROM LogAcesso WHERE nomPagina = "Games";
