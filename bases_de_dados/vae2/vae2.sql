-- Questão 01
-- 1

SELECT a.id, a.nome
FROM Comida a
JOIN CategoriaComida b
ON b.id = a.idCategoria
WHERE b.nome LIKE 'JunkFood';

-- 2

SELECT COUNT(*) as total, b.nome
FROM Comida a
JOIN CategoriaComida b
ON b.id = a.idCategoria
GROUP BY b.nome
ORDER BY total;

-- 3

SELECT DISTINCT d.id, d.titulo, d.temporada
FROM Comida a
JOIN CategoriaComida b
ON b.id = a.idCategoria
JOIN EpisodioComida c
ON c.idComida = a.id
JOIN Episodio d
ON c.idEpisodio = d.id
WHERE b.nome LIKE 'JunkFood';

-- 4

SELECT DISTINCT a.nome
FROM Comida a
JOIN EpisodioComida c
ON c.idComida = a.id
JOIN Episodio d
ON c.idEpisodio = d.id
WHERE d.titulo LIKE '%namorada%' OR d.titulo LIKE '%amor%'
ORDER BY a.nome;

-- 5

SELECT COUNT(*)
FROM
(
SELECT c.idComida
FROM
Comida a
JOIN EpisodioComida c
ON c.idComida = a.id
JOIN Episodio d
ON c.idEpisodio = d.id
WHERE a.nome LIKE 'Café'
INTERSECT
SELECT c.idComida
FROM
Comida a
JOIN EpisodioComida c
ON c.idComida = a.id
JOIN Episodio d
ON c.idEpisodio = d.id
WHERE a.nome LIKE 'Donuts'
);

-- 6

SELECT
AVG(sub1.total_consumo)
FROM
(SELECT COUNT(DISTINCT a.nome) as total_consumo,
d.titulo
FROM Comida a
JOIN EpisodioComida c
ON c.idComida = a.id
JOIN Episodio d
ON c.idEpisodio = d.id
GROUP BY d.titulo
) sub1;

-- Questão 02

-- 1
SELECT a.id FROM Familia a
JOIN Municipio b
ON a.cod_municipio = b.cod_municipio
WHERE b.nom_municipio = 'Fortaleza' OR b.nom_municipio = 'Recife';

-- 2

SELECT DISTINCT sub1.id, sub1.nom_prod FROM
(SELECT d.id as id, d.nom_prod as nom_prod
FROM Familia a
JOIN Municipio b
ON a.cod_municipio = b.cod_municipio
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id) sub1
LEFT JOIN
(SELECT d.id as id, d.nom_prod
FROM Familia a
JOIN Municipio b
ON a.cod_municipio = b.cod_municipio
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
WHERE b.cod_municipio = '2304400') sub2
ON sub1.id = sub2.id
WHERE sub2.id IS NULL;

-- 3

SELECT d.nom_prod as nom_prod, COUNT(*)
FROM Familia a
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
WHERE d.nom_prod LIKE 'Ovos de galinha'
OR d.nom_prod LIKE 'Carne bovina de 1a. : File mignon'
GROUP BY d.nom_prod;

-- 4

SELECT b.nom_municipio as nom_municipio, COUNT(*) as total
FROM Familia a
JOIN Municipio b
ON a.cod_municipio = b.cod_municipio
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
WHERE d.nom_prod LIKE 'Lentilha'
GROUP BY b.nom_municipio
ORDER BY total DESC;

-- 5

Eu não sabia se deveria incluir também os produtos e dados territoriais,
consequentemente tendo mais de uma linha como resultado do select.
Por conta disso fiz duas consultas diferentes.
Primeira consulta só com renda e dados da família:
SELECT *
FROM Familia a
JOIN FaixaRenda b
ON a.id_faixa_renda = b.id_faixa
WHERE a.qtd_membros = (SELECT MAX(qtd_membros) FROM Familia);
Segunda consulta que inclui produtos consumidos e dados territoriais:
SELECT *
FROM Familia a
JOIN FaixaRenda b
ON a.id_faixa_renda = b.id_faixa
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
JOIN Municipio e
ON e.cod_municipio = a.cod_municipio
JOIN Regiao f
ON f.cod_regiao = e.cod_regiao
WHERE a.qtd_membros = (SELECT MAX(qtd_membros) FROM Familia);

-- 6

SELECT DISTINCT sub1.nom_prod FROM
(SELECT d.id as id, d.nom_prod as nom_prod
FROM Familia a
JOIN Municipio b
ON a.cod_municipio = b.cod_municipio
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
WHERE b.cod_municipio = '2304400') sub1
LEFT JOIN
(SELECT d.id as id, d.nom_prod
FROM Familia a
JOIN Municipio b
ON a.cod_municipio = b.cod_municipio
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
WHERE b.cod_municipio = '4205407') sub2
ON sub1.id = sub2.id
WHERE sub2.id IS NULL;

-- 7

SELECT DISTINCT id_faixa, dsc_faixa
FROM Familia a
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
JOIN FaixaRenda e
ON e.id_faixa = a.id_faixa_renda
WHERE d.nom_prod = 'Ostras';

-- 8

SELECT DISTINCT nom_prod
FROM Familia a
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
JOIN FaixaRenda e
ON e.id_faixa = a.id_faixa_renda
WHERE a.id_faixa_renda = 1;

-- 9

SELECT id, qtd_membros,
CASE
WHEN qtd_membros = 1 THEN 'Pessoa sozinha'
WHEN qtd_membros = 2 THEN 'Dupla'
WHEN qtd_membros = 3 THEN 'Trio'
WHEN qtd_membros >= 4 THEN 'Familia Grande'
ELSE 'NULL'
END AS descricao_tamanho
FROM Familia;

--10

SELECT COUNT(*)
FROM
(
SELECT c.id_familia
FROM
Familia a
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
WHERE d.nom_prod LIKE 'Milho verde em conserva'
INTERSECT
SELECT c.id_familia
FROM
Familia a
JOIN Compras c
ON c.id_familia = a.id
JOIN Produto d
ON c.id_produto = d.id
WHERE d.nom_prod LIKE 'Ervilhas em conserva (petit-pois)'
);
