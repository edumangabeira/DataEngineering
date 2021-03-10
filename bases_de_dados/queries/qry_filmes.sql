-- QUESTÕES GUIA

--  1. Quais são os 10 filmes mais apreciados pelo público?

select filme, nota_audiencia from filmes
order by nota_audiencia desc
limit 10

-- 2. Quais são os 10 filmes mais apreciados pela crítica especializada?

select filme, nota_especialistas from filmes
order by nota_especialistas desc
limit 10

-- 3. Quais são os 10 filmes mais odiados pelo público?

-- Obs: Tem duas notas zero, seria bom investigar caso fosse um problema cotidiano em vez de um exercício

select filme, nota_audiencia from filmes
order by nota_audiencia asc
limit 10

-- 4. Quais são os 10 filmes mais odiados pela crítica especializada?

select filme, nota_especialistas from filmes
order by nota_especialistas asc
limit 10

-- 5. Qual filme com maior custo e qual filme com menor custo?

-- maior
select filme, custo from filmes
order by custo desc
limit 1
--menor
select filme, custo from filmes
order by custo
limit 1

-- 6. Qual a média da nota da crítica especializada?
select avg(nota_especialistas) from filmes

-- 7. Qual a média da nota do público?

select avg(nota_audiencia) from filmes

-- 8. Qual a média de custo de filmes?

select avg(custo) from filmes

-- 9. Quantos filmes custaram mais do que o custo médio dos filmes da tabela?

select filme, custo from filmes
where custo > (select avg(custo) from filmes)
order by custo desc

-- 10. Quais são os filmes com nota acima da média das notas dadas pela crítica especializada?

select filme, nota_especialistas from filmes
where nota_especialistas > (select avg(nota_especialistas) from filmes)
order by nota_especialistas desc

-- 11. Quais são os filmes com nota acima da média das notas dadas pelo público? Quais os melhores?

select filme, nota_audiencia from filmes
where nota_audiencia > (select avg(nota_audiencia) from filmes)
order by nota_audiencia desc

-- 12. Quais são os tipos de categoria (gêneros) existentes?

select genero from filmes
group by genero

-- 13. Quais são os gêneros com maior quantidade de filmes?

select genero, count(filme) as filmes_count from filmes
group by genero

-- 14. Qual gênero tem a mais alta média de custo?

select genero, avg(custo) as media_custo from filmes
group by genero
order by media_custo desc

-- 15. Qual gênero tem a mais alta média de nota para o público?

select genero, avg(nota_audiencia) as media_audiencia from filmes
group by genero
order by media_audiencia desc

-- 16. Qual gênero tem a mais alta média de nota para a crítica especializada?

select genero, avg(nota_especialistas) as nota_especialistas from filmes
group by genero
order by nota_especialistas desc

-- 17. Quantos filmes foram produzidos por ano?

select ano, count(filme) as filmes_count from filmes
group by ano

-- 18. Qual ano foram produzidos mais filmes?

select ano, count(filme) as filmes_count from filmes
group by ano
order by filmes_count desc
limit 1

-- 19. Qual gênero produziu mais filmes em um ano?

select genero, count(filme) as filmes_count from filmes
group by genero
order by filmes_count desc
limit 1

-- 20. Qual o filme mais amado pela audiência e pelos especialistas ao mesmo tempo?

select filme, greatest(nota_especialistas, nota_audiencia) as favoritos from filmes
order by favoritos desc
