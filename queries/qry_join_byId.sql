SELECT * FROM cadastro.alunos_disciplinas;
SELECT * FROM cadastro.disciplinas;
SELECT * FROM cadastro.escola;
SELECT * FROM cadastro.notas;

-- Join por id nas tabelas, o modelo tá meio esquisito

SELECT A.nome, A.id_escola,
AC.id_aluno_disciplina,
C.id_disciplinas, C.nome,
N.id_notas, N.p1, N.p2
FROM escola A, alunos_disciplinas AC, disciplinas C, notas N
WHERE A.id_escola = AC.id_aluno and AC.id_disciplina = C.id_disciplinas and A.id_escola =N.id_notas
