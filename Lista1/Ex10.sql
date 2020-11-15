-- item (a)

SELECT titulo, ano, avaliacao FROM Filme
WHERE avaliacao >= 9.0
ORDER BY avaliacao DESC

-- item (b)
SELECT titulofilme, ano FROM FilmeGenero
WHERE nomegenero = "Suspense"
OR nomegenero = "Filme Noir"

-- item (c)

SELECT a.titulo, a.ano, a.resumo  FROM Filme a
NATURAL JOIN FilmeElenco b
WHERE a.titulo = b.titulofilme
AND a.ano = b.ano
AND b.nomeartista = "Fernanda Montenegro"


-- item (d)

SELECT DISTINCT a.nome FROM Artista a
NATURAL JOIN
FilmeElenco b
NATURAL JOIN
Filme c
WHERE (c.pais = "FR" OR c.pais ="BE")
AND b.titulofilme = c.titulo
AND b.ano = c.ano
AND a.sexo = "F"
AND c.ano < 2000


-- item (e)

SELECT DISTINCT a.nome FROM Artista a
NATURAL JOIN
FilmeGenero b
NATURAL JOIN
Filme c
WHERE c.pais = "BR"
AND b.titulofilme = c.titulo
AND b.ano = c.ano
AND b.nomegenero = "Musical"
ORDER BY b.nomegenero

