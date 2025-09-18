import pandas as pd
import os

print(os.getcwd())

df_students = pd.read_csv("./Python-Infotec-Course/Pandas/Files/respuestas_estudiantes.csv")
df_grades = pd.read_excel("./Python-Infotec-Course/Pandas/Files/respuestas_correctas.xlsx")

print(df_students)
print(df_grades)