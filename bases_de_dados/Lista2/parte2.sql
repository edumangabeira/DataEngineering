-- 3.2

SELECT cod_uf, COUNT(*) AS tot_domicilios_vazios
FROM t_domicilio_pnad a
WHERE NOT EXISTS
(SELECT *
FROM t_pessoa_pnad b
WHERE b.cod_domicilio = a.cod_domicilio)
GROUP BY cod_uf
ORDER BY cod_uf;

-- 3.3

SELECT num_comodos, COUNT(*) AS tot_domicilios
FROM t_domicilio_pnad
GROUP BY num_comodos
ORDER BY num_comodos DESC;

-- 3.4

SELECT MIN(val_rend_total),
MAX(val_rend_total),
AVG(val_rend_total)
FROM t_pessoa_pnad;

-- 3.5

SELECT MIN(val_rend_total),
MAX(val_rend_total),
AVG(val_rend_total)
FROM t_pessoa_pnad
WHERE num_idade >= 30
AND (cod_curso_ant = '08' OR cod_curso_ant = '09');

-- 3.6

SELECT c.nom_uf as nom_uf,
AVG(a.val_rend_total) as renda_media
FROM t_pessoa_pnad a
JOIN t_domicilio_pnad b
ON a.cod_domicilio = b.cod_domicilio
JOIN t_uf c
ON b.cod_uf  = c.cod_uf
GROUP BY nom_uf
ORDER BY renda_media DESC;

-- 3.7

CREATE VIEW v_renda_media_regiao AS
SELECT AVG(a.val_rend_total) as renda_media,
CASE
WHEN b.cod_uf LIKE '1%' THEN 'Norte'
WHEN b.cod_uf LIKE '2%' THEN 'Nordeste'
WHEN b.cod_uf LIKE '3%' THEN 'Sudeste'
WHEN b.cod_uf LIKE '4%' THEN 'Sul'
WHEN b.cod_uf LIKE '5%' THEN 'Centro-Oeste'
ELSE 'NULL'
END AS nom_regiao
FROM t_pessoa_pnad a
JOIN t_domicilio_pnad b
ON a.cod_domicilio = b.cod_domicilio
JOIN t_uf c
ON b.cod_uf = c.cod_uf
GROUP BY nom_regiao
ORDER BY renda_media DESC;

SELECT * FROM v_renda_media_regiao;

-- 3.8

SELECT *
FROM t_pessoa_pnad a
JOIN t_domicilio_pnad b
ON a.cod_domicilio = b.cod_domicilio
WHERE a.val_rend_total = (SELECT MAX(val_rend_total) FROM t_pessoa_pnad );

-- 3.9

SELECT cod_domicilio, num_comodos, b.nom_uf, c.dsc_condicao_domic
FROM t_domicilio_pnad a
JOIN t_uf b
ON a.cod_uf = b.cod_uf
JOIN t_condicao_domicilio c
ON a.cod_condicao = c.cod_condicao_domic
JOIN t_pessoa_pnad d
ON a.cod_domicilio = d.cod_domicilio
WHERE d.num_idade > 80 OR d.num_idade < 1;


-- 3.10

SELECT a.num_comodos,
b.sgl_uf,
d.cod_domicilio, d.cod_pessoa, d.cod_curso_ant,
d.cod_sexo, d.num_idade,
e.nom_raca,
f.nom_ocupacao
FROM t_domicilio_pnad a
JOIN t_uf b
ON a.cod_uf = b.cod_uf
JOIN t_condicao_domicilio c
ON a.cod_condicao = c.cod_condicao_domic
JOIN t_pessoa_pnad d
ON a.cod_domicilio = d.cod_domicilio
JOIN t_raca e
ON d.cod_raca = e.cod_raca
JOIN t_cbo f
ON d.cod_ocupacao = f.cod_ocupacao
WHERE a.num_comodos > 20
ORDER BY a.num_comodos DESC, a.cod_domicilio, d.cod_pessoa;


-- 3.11

SELECT f.nom_ocupacao
FROM t_cbo f
WHERE NOT EXISTS(SELECT cod_ocupacao FROM t_pessoa_pnad WHERE cod_ocupacao = f.cod_ocupacao);

-- 3.12

SELECT e.nom_raca as raca, d.cod_sexo as sexo , COUNT(*) as total
FROM t_pessoa_pnad d
JOIN t_raca e
ON e.cod_raca = d.cod_raca
GROUP BY raca, sexo
ORDER BY total DESC;

-- 3.13

SELECT e.nom_raca as raca, d.cod_sexo as sexo,
COUNT(*) as total, ROUND(AVG(val_rend_total), 2) as media
FROM t_pessoa_pnad d
JOIN t_raca e
ON e.cod_raca = d.cod_raca
WHERE num_idade > 18
GROUP BY raca, sexo
ORDER BY media;

-- 3.14

SELECT f.nom_ocupacao, d.*
FROM t_pessoa_pnad d
JOIN t_cbo f
ON f.cod_ocupacao = d.cod_ocupacao
WHERE f.nom_ocupacao LIKE '%SOFT%' OR f.nom_ocupacao LIKE '%ESTAT%'

-- 3.15

SELECT f.nom_ocupacao, AVG(d.val_rend_trab_princ) as media_salario
FROM t_pessoa_pnad d
JOIN t_cbo f
ON f.cod_ocupacao = d.cod_ocupacao
GROUP BY f.nom_ocupacao
HAVING AVG(d.val_rend_trab_princ) > 1000
ORDER BY media_salario DESC

-- 3.16

SELECT *
FROM t_domicilio_pnad
WHERE cod_domicilio =
    (SELECT cod_domicilio FROM t_pessoa_pnad
  GROUP BY cod_domicilio
  HAVING COUNT(cod_domicilio) =
      (SELECT MAX(sub1.pessoas) as max_pessoas FROM
          (SELECT COUNT(cod_domicilio) as pessoas,
          cod_domicilio FROM t_pessoa_pnad GROUP BY cod_domicilio) sub1
       )
     )
