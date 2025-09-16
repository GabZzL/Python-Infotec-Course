from datetime import datetime

"""  
Trabajas en una compañía que ofrece seguros de vida y de gastos
médicos. La empresa está desarrollando una herramienta tecnológica,
para que los agentes puedan calcular el monto de una póliza. Para dicho
cálculo, se consideran varios factores de riesgo, entre los que se encuentra
la edad. Por ello, el contratante debe llenar un formulario, incluyendo su
fecha de nacimiento. Como primer reto, deberás calcular la edad del
cliente al momento de la cotización.
• La captura de la fecha de nacimiento debe ser en una sola cadena
de texto con formato DD-MM-AAAA.
• Validar que sea una fecha existente, si supera los 31 días o menor a 1
día de un mes, se deberá marcar como inválido.
• El año de nacimiento debe ser mayor de 1900.
• Validar si el cliente ya cumplió años en la fecha de captura o aún no.
• Validar que no se puede dejar información en blanco o campos
vacíos. 
"""

# Funcion principal
def calculate_age():
    # Capturar la fecha de nacimiento del usuario
    date = input("Insert your birthday(dd-mm-aaaa): ")
    # Obtener cada campo la fecha
    arr_date = date.split("-")
    
    # Validar todos los campos de la fecha
    if len(arr_date) != 3:
        print("Invalid date")
        return
        
    # Convertir la fecha a numeros enteros 
    day = int(arr_date[0])
    month = int(arr_date[1])
    year = int(arr_date[2])
        
    # Validar la fecha proporcionada    
    if day <= 0 or day > 31:
        print("Invalid day")
        return
    
    if month <= 0 or month > 12:
        print("Invalid month")
        return
    
    if year < 1900:
        print("Invalid year")
        return
    
    # Obtener la fecha actual
    current_date = datetime.now()
    
    current_day = current_date.day
    current_month = current_date.month
    
    # Obtener la edad del usuario
    user_age = current_date.year - year
    # Aumentar un año, si ya ha pasado el cumpleaños del usuario
    if month >= current_month and day >= current_day:
        user_age += 1
       
    # Mostrar la edad 
    print(f"User age: {user_age} years old")
    
calculate_age()

"""  
En una escuela se quiere crear un sistema de evaluación para profesores
que permita la obtención de los alumnos aprobados y reprobados de
acuerdo a su historial académico, dicho sistema ayudará a dar de forma
rápida todos los datos del alumno, siguiendo las siguientes condiciones:
• Deberá pedir el número de alumnos y materias, pedir el nombre del
alumno, y su matrícula.
• El sistema debe evaluar, como condición de evaluación, que si es
una calificación mayor a 6, es aprobado y de lo contrario, reprobado.
• Validar que no se puede dejar información en blanco o campos
vacíos.
"""

# Funcion para verificar los datos del usuario
def verify_inputs(input1, input2):
    if not input1.strip() or not input2.strip():
        print("Please Insert Valid Inputs")
        return False
    else:
        return True 

# Function prnicipal
def grades_system():
    # Diccionario para almacenar la informacion de los estudiantes
    students = {}
    # Numero de estudiantes y materias
    students_input = input("Insert the students number: ")
    subjects_input = input("Insert the subjects number: ")
    print("\n")
    # Usar la function para verificar las entradas
    num_inputs = verify_inputs(students_input, subjects_input)
    # Comprobar que las entradas son validas
    if not num_inputs:
        return
    # Convertir las entradas a numeros enteros
    students_num = int(students_input)
    subjects_num = int(subjects_input)
    
    # Ciclo for para solicitar la information del numero de estudiantes antes proporcionado
    for i in range(students_num):
        # Nombres de los estudiantes y matricula
        student_name = input("Insert student name: ")
        student_tuition = input("Insert student tuition(###): ")
        print("\n")
        # Verificar las entradas
        student_inputs = verify_inputs(student_name, student_tuition)
        # Comprobar que las entradas son validas
        if not student_inputs:
            return
        # Crear una nueva entrada en el diccionario(la llave principal sera la matricula)
        students[student_tuition] = {
            "name": student_name,
            "subjects": {}
        }
        
        # Ciclo for aninado para pedir informarion sobre las materias y calificaciones
        for j in range(subjects_num):
            # Nombre de la materia y calificacion
            subject_name = input("Insert subject name: ")
            subject_input = input("Insert subject grade: ")
            print("\n")
            # Verificar las entradas
            subject_inputs = verify_inputs(subject_name, subject_input)
            # Comprobar si las entradas son validas
            if not subject_inputs:
                return
            # Convertir la calification a un numero flotante
            subject_grade = float(subject_input)
            # Determinar si el estudiante aprobo o reprobo la materia
            if subject_grade >= 6:
                subject_state = "Pass"
            else:
                subject_state = "Fail"
            # Crear una nueva entrada en el diccionario para cada materia
            students[student_tuition]["subjects"][subject_name] = {"grade": subject_grade, "state": subject_state}
    
    # Finalmente, imprimir el diccionario final
    print(students)

# Llamar a la function principal    
grades_system()