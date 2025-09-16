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