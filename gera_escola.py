import random as rd
import pandas as pd
import datetime


def gera_nascimento():

    mais_velho = datetime.date(1999, 1, 1)
    mais_novo = datetime.date(2010, 12, 31)

    idades = mais_novo - mais_velho
    dias = idades.days
    n_dias = rd.randrange(dias)
    data = mais_velho + datetime.timedelta(days=n_dias)
    return data


def gera_endereco(enderecos):

    numero = rd.randint(1, 450)
    endereco = rd.randint(0, len(enderecos) - 1)
    endereco = enderecos[endereco]
    return endereco + ', ' + str(numero)


def gera_cpf():
    cpf = [rd.randint(0, 9) for digito in range(11)]
    d_1 = ''.join(map(str, cpf[0:3]))
    d_2 = ''.join(map(str, cpf[3:6]))
    d_3 = ''.join(map(str, cpf[6:9]))
    d_f = ''.join(map(str, cpf[9:12]))
    return "{}.{}.{}-{}".format(d_1, d_2, d_3, d_f)


def gera_alunos(nomes, sobrenomes, enderecos, quantidade_alunos=60):
    '''
    argumentos: nomes, sobrenomes, quantidade_alunos(default=60)

    nomes: lista com nomes do brasil em maiúsculo, sem acentos.
    sobrenomes: lista com sobrenomes do brasil em maiúsculo, sem acentos.
    quantidade_alunos: número de alunos que serão criados.
    '''

    df = pd.DataFrame(columns=["nome", "data_nascimento", "endereco", "cpf"], index=None)

    for i in range(0, quantidade_alunos):

        # nome
        nome = rd.randint(0, len(nomes) - 1)
        nome = nomes[nome]
        sobrenome = rd.randint(0, len(sobrenomes) - 1)
        sobrenome = sobrenomes[sobrenome]
        sobrenome_2 = ""
        sorteado = rd.randint(0, 2)
        if sorteado == 0:
            sobrenome_2 = rd.randint(0, len(sobrenomes) - 1)
            sobrenome_2 = sobrenomes[sobrenome_2]
            sobrenome_2 = " " + sobrenome_2
            while sobrenome_2 == sobrenome:
                sobrenome_2 = rd.randint(0, len(sobrenomes) - 1)
                sobrenome_2 = sobrenomes[sobrenome_2]
                sobrenome_2 = " " + sobrenome_2
        nome = nome + ' ' + sobrenome + sobrenome_2
        # data de nascimento
        nascimento = gera_nascimento()
        # endereço
        endereco = gera_endereco(enderecos)
        # cpf
        cpf = gera_cpf()

        # tabela
        to_append = [nome, nascimento, endereco, cpf]
        a_series = pd.Series(to_append, index=df.columns)
        df = df.append(a_series, ignore_index=True)
    df.to_csv("escola.csv", index=False)


if __name__ == '__main__':

    # nomes brasileiros
    nomes = pd.read_csv("nomes.csv")
    nomes = nomes[nomes["frequency_total"] > 100000]
    nomes = nomes["group_name"].values.tolist()
    sobrenomes = ["SILVA", "SANTOS", "ALVES", "FREIRE", "GARCIA", "MARQUES", "FERREIRA", "OLIVEIRA", "DOS ANJOS", "SANTANA", "CASTRO", "MARTINS", "SOUZA", "JUNQUEIRA", "ANDRADE", "AZEVEDO", "RIBEIRO", "BORGES", "LOPES", "MEDEIROS", "NUNES", "LIMA", "BATISTA", "PEREIRA", "TEIXEIRA", "COSTA", "SAMPAIO", "CRUZ"]

    enderecos = ["AV. BRASIL", "RUA SAO JOSE", "AV. PEREIRA PASSOS", "RUA RODOLFO MOTA LIMA", "TRAVESSA SANTA RITA", "AV. TREZE DE MAIO", "AV. SETE DE SETEMBRO", "RUA URANOS", "RUA CACEQUI", "PRAÇA VANHAGEN", "PRAÇA DA BANDEIRA", "RUA CLARA NUNES", "LARGO DO MACHADO", "PRAÇA TIRADENTES", "RUA DO OUVIDOR", "AV. CHILE", "RUA RIACHUELO", "RUA ANDRE CAVALCANTI", "RUA FREI CANECA", "AV. GOMES FREIRE", "TRAVESSA CASSIANO", "RUA DO ORIENTE"]

    gera_alunos(nomes, sobrenomes, enderecos, 360)
