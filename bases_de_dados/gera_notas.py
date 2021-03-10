import random as rd
import pandas as pd

df = pd.DataFrame(columns=["id_notas", "p1", "p2"], index=None)

for id_notas in range(1, 351):
    p1 = rd.randint(0, 10)
    p2 = rd.randint(0, 10)
    to_append = [int(id_notas), p1, p2]
    a_series = pd.Series(to_append, index=df.columns)
    df = df.append(a_series, ignore_index=True)

df.to_csv("notas_alunos.csv", index=False)
