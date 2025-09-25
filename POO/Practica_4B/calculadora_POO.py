from calculator import Calculator

"""
1. Crear un nuevo método llamado “potencia” dentro de la clase
Calculadora que eleve el primer número a la potencia del segundo
número.
2. Modificar la función interpretar_expresion, para que reconozca el
operador ^ como indicador de potencia.
3. Actualizar el diccionario de operaciones en el programa principal,
para incluir esta nueva funcionalidad. Asegúrate de que el sistema
registre adecuadamente estas operaciones en el historial con el
formato correcto.
4. Usar la modularidad para dividir en módulos la calculadora y
permitir que las clases tengan su propio archivo .py.
"""    
# Funcion para validar los numeros 
def validate_number(entry):
    try:
        number = float(entry)
        return number
    except ValueError:
        print('Error. Invalid number')
        return None
# Funcion para validar las operaciones
def validate_operation(entry):
    if entry in ['+', '-', '*', '/', '^', 'result']:
        return entry
    return None
    
# Clase principal para ejecutar el programa
def main():
    # Mensaje de presentacion
    print('Basic calculator. "Exit" to end the program, "records" to take a look at the previous operations')
    # Crear la instancia 'calc'
    calc = Calculator()
    # Bucle while para controlar las ejecuciones del programa
    while True:
        # Pedir la operacion a realizar
        entry = input('Insert an option (exit, records, operation):')
        # exit, salir del ciclo while, y terminar el programa
        if entry.strip().lower() == 'exit':
            print('See you later!')
            break
        # records, mostrar el historial
        if entry.strip().lower() == 'records':
            calc.look_records()
            continue
        # operation, realizar una operacion matematica
        if entry.strip().lower() == 'operation':
            # Pedir el primer numero
            num1_entry = input('Number: ')
            # Validar la entrada
            num1 = validate_number(num1_entry)
            if num1 is None:
                print('Invalid Number. Please insert a valid number')
                continue
            # Asignar el primer valor
            calc.assign_value(num1)
             # i, este valor sirve para saber el numero del ciclo
            i = 0
            # Ciclo para controlar el numero de operaciones
            while True:
                # Mensaje para mostrar las opciones
                message = 'Operation(+, -, *, /, ^) or result: '
                # Cambiar el mansaje en el primer ciclo
                if i == 0:
                    message = 'Operation(+, -, *, /, ^): '
                    i += 1
                # Pedir la operacion
                operation_entry = input(message)
                # Validar la operacion
                operation = validate_operation(operation_entry)
                if not operation:
                    print('Invalid operation. Please insert a valid operation')
                    continue
                 # result, mostrar el resultado de los calculos
                if operation.strip().lower() == 'result':
                    print(f'result: {calc.get_total()}\n')
                    calc.clear()
                    break
                # Pedir el segundo numero
                num2_entry = input('Number: ')
                # Validar las entrada
                num2 = validate_number(num2_entry)
                if not num2:
                    print('Invalid Number. Please insert a valid number')
                    continue
                # Realizar la operacion seleccionada
                if operation == '+':
                    calc.sum(num2)
                elif operation == '-':
                    calc.sub(num2)
                elif operation == '*':
                    calc.multiply(num2)
                elif operation == '/':
                    calc.divide(num2)
                elif operation == '^':
                    calc.power(num2)
        # si la opcion es diferente, pedir ingresar una opcion valida
        else:
            print('Invalid operation. Insert a valid one')
            continue

# Ejecucion de la funcion principal  
main()