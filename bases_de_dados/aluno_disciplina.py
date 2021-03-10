import random as rd
import numpy as np
import pandas as pd

df = pd.DataFrame(columns=["id_aluno", "id_disciplina"], index=None)

for id_aluno in range(1, 351):
    id_disciplina = rd.randint(0, 10)
    to_append = [int(id_aluno), id_disciplina]
    a_series = pd.Series(to_append, index=df.columns)
    df = df.append(a_series, ignore_index=True)

df['id_aluno'] = np.random.permutation(df['id_aluno'].values)
df.to_csv("aluno_disciplina.csv", index=False)
