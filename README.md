## Introdução ao MySQL

Vou deixar esse espaço aqui para os scripts em python que eu escrever enquanto faço o cursinho de MySQL. 
Devo usar alguns só pra praticar conceitos básicos tipo gerar nomes e números de CPF. Apesar de já poder usar bases prontas, deve ser divertido esse exercício,
ainda mais que eu estava namorando generators há algum tempo hahahaha. Finalmente vou poder usar em alguma coisa, assim espero.


### [atualização 02/09]

- Acabei não precisando de generators para nada rs. 

- O Workbench deixa tudo infinitamente mais fácil, tanto que na hora de criar a base não precisei fazer nenhuma
query na mão. 

- Fiz alguns joins pelos ids das tabelas e sinto que a modelagem poderia ser bem melhor. Vou passar a deixar salvas algumas queries nesse repositório,
até entrar no sangue. Ainda preciso fazer mais exercícios nesse sentido, se possível com bases prontas. 

- Construir a base do zero foi importante e acredito que tenha sido proveitoso, mas agora quero focar em fazer consultas mais elaboradas.

# Bases de dados

### [atualização 02/10]


O período letivo começou e acabei não tendo tempo para voltar a esse projeto, mas - pensando melhor - acabei percebendo que o restante do curso da udemy
de introdução ao MySQL talvez não fosse tão interessante para mim, já que não é meu foco me tornar DBA.

As aulas da disciplina de bases de dados estão cobrindo bem a parte que cabe a um cientista de dados. O professor está usando o SQLite, provavelmente por 
ser bem mais leve(assim todos podem usar em casa). Se eu achar que vale a pena, vou registrar meu progresso nessas aulas, de repente publicando como
eu projetei o banco de dados com um desenho do esquema.


## Udacity nanodegree

### [atualização 04/12/2020]

Até agora as aulas da disciplina de bases de dados estão sendo sensacionais, o professor é incrível. Já aprendi sobre álgebra relacional, revisitei diagramas entidade-relacionamento, aprendi a criar um banco do zero(e preencher) sem fazer besteira com as chaves e também aprendi a fazer consultas mais avançadas com SQL. O professor usa o SQLite, o que é ótimo, pois já me acostumo a interagir com diferentes SGBD's.

Comecei um nanodegree da Udacity em engenharia de dados por conta do desconto absurdo da black friday e o primeiro capítulo é sobre SQL. Até agora está sendo bem interessante. Curti muito um [texto](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems) externo recomendado pela Udacity que explica as diferenças entre os três SGBD's relacionais mais usados hoje em dia: MySQL, SQLite e PostgreSQL.


### [atualização 12/12/2020]

Eu ainda não tinha visto conceitos básicos do SQL, como joins e aggregations, então o nanodegree tomou um ritmo bem acelerado. Achei bem esquisita a quantidade de blocos try/except em um único script para conectar a um banco PostgreSQL, mesmo existindo uma explicação que faz sentido. Vou seguir sem prestar muita atenção a isso agora. Começarei a parte de NoSQL e espero finalmente entender como o MongoDB funciona de verdade, já deu para ver que os bancos NoSQL têm finalidades bem específicas, apesar de funcionarem bem em diversos contextos.

 ### [atualização 30/01/2021]
 
 Ufa, foi um período muito intenso. Sinto que aprendi bastante sobre SQL e já consigo fazer diversos tipos de consultas, além de poder pensar em projetos de bancos de dados relacionais com mais maturidade, considerando comportamentos inusitados de um banco relacional. O Nanodegree ajudou imensamente, claro, mas as aulas do professor Eduardo Correa Gonçalves são fora de série, a didática dele é impressionante. A partir da próxima semana poderei voltar a me dedicar as projetos do Nanodegree e vou tentar dar uma acelerada, esse período(principalmente o final) foi bem puxado com 6 matérias + monitoria + projeto Rio em Dados. Espero não repetir a loucura período que vem para poder me dedicar ao estudo de Data Engineering e quem sabe machine learning ou estrutura de dados.
 
 ## [atualização 11/02/2021]

Minhas férias começaram e posso finalmente continuar o Nanodegree. O arquivo ```sql_queries.py``` já está completo, mas terei que ler o projeto inteiro novamente, já faz um tempo desde a última tentativa.

## [atualização 08/03/2021]

1 - Surpreendentemente, o código de ```sql_queries.py``` não rodou, pois alguns pequenos erros apareceram devido à sintaxe de declaração da chave primária e questões de palavras reservadas, mas agora estão resolvidos. As próximas etapas são corrigir algumas relações e iniciar o teste.

2 - Terminada a criação de tabelas, o código funciona perfeitamente. Agora estou indo para a parte ETL.

## [atualização 09/03/2021]

1 - Último empurrão! A parte final do etl.ipynb me pegou, no entanto. Estou realmente lutando para entender exatamente como a instrução select deve ser escrita.

2 - Finalmente, todas as tarefas estão concluídas e tudo parece estar funcionando bem. Inicialmente, não consegui executar etl.py, mas alterar as restrições das instruções de inserção acabou sendo uma solução bem direta.



## [atualização 10/03/2021]

Depois de uma revisão, o projeto de modelagem de dados com postgres foi aceito! Agora vou partir para o projeto com Apache Cassandra.

