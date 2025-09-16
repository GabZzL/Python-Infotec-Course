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

def grades_system():
    students = {}
    
    students_input = input("Insert the students number: ")
    subjects_input = input("Insert the subjects number: ")
    
    students_num = int(students_input)
    subjects_num = int(subjects_input)
    
    for i in range(students_num):
        student_name = input("Insert student name: ")
        student_tuition = input("Insert student tuition: ")
        
        students[student_tuition] = {
            "name": student_name,
            "subjects": {}
        }
        
        for j in range(subjects_num):
            subject_name = input("Insert subject name: ")
            subject_input = input("Insert subject grade: ")
            
            subject_grade = float(subject_input)
            
            if subject_grade >= 6:
                subject_state = "Pass"
            else:
                subject_state = "Fail"
            
            students[student_tuition]["subjects"][subject_name] = {"grade": subject_grade, "state": subject_state}
            
    print(students)
        
grades_system()