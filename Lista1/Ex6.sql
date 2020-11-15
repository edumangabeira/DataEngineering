CREATE TABLE Pais(
sigla VARCHAR(2) NOT NULL,
nome TEXT NOT NULL,
PRIMARY KEY(nome)
);

CREATE TABLE Atleta(
matAtleta INT NOT NULL,
nome TEXT NOT NULL,
idade INT NOT NULL,
sexo TEXT NOT NULL,
siglaPais VARCHAR(2) NOT NULL,
PRIMARY KEY(matAtleta),
FOREIGN KEY (siglaPais) REFERENCES Pais(sigla)
);

CREATE TABLE Resultado(
matAtleta INT NOT NULL,
codModalidade INT NOT NULL,
posicao INT NOT NULL,
PRIMARY KEY(codModalidade),
FOREIGN KEY (matAtleta) REFERENCES Atleta(matAtleta)
);


CREATE TABLE Modalidade(
codModalidade INT NOT NULL,
nomModalidade TEXT NOT NULL,
PRIMARY KEY (codModalidade),
FOREIGN KEY (codModalidade) REFERENCES Resultado(codModalidade)
)
