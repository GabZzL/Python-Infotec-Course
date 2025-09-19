import pandas as pd
# Extrar los archivos, y guardarlos en un dataframe
df_students = pd.read_csv("./Pandas/Files/respuestas_estudiantes.csv")
df_answers = pd.read_excel("./Pandas/Files/respuestas_correctas.xlsx")
# Guardar las preguntas y respuestas en listas
questions = df_answers['Pregunta'].values
answers = df_answers['Respuesta'].values
# Obtener el numero total de preguntas
n_questions = len(questions)
# Crear un diccionario para guardar las preguntas, y sus respuestas
right_answers = {}
# Ciclo para agregar la informacion al diccionario
for n in range(n_questions):
    right_answers[questions[n]] = answers[n]
# Crear una nueva columna en el df de estudiantes
df_students['Puntuacion'] = 0
# Comparar las respuestas correctas con las respuestas de los estudiantes
for q in questions:
    # Obtener la respuesta correcta
    right_answer = right_answers[q]
    # Guardar la nueva serie creada en la column 'Puntuacion'
    df_students['Puntuacion'] = df_students['Puntuacion'].add((df_students[q] == right_answer).astype(int))
# Crear una copia del dataframe de estudiantes
df_report = df_students.copy()
# En el nuevo dataframe, se usa el metodo 'where', para modificar los valores donde la respuesta no fue correcta
for q in questions:
    df_report[q] = df_report[q].where(df_report[q] == right_answers[q], df_report[q] + 'x')
# Ordenar el dataframe de manera descendente
df_report = df_report.sort_values('Puntuacion', ascending=False)
# Limpiar el formate del dataframe
df_final = df_report[['Nombre', 'Puntuacion']].sort_values('Puntuacion', ascending=False).to_string(index=False)
# Crear un archivo csv con los resultados obtenidos
df_report.to_csv('resultados_examen.csv', index=False)
# Mostrar los resultados
print(df_final)
