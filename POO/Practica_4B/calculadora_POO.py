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
# Funcion para verificar las entradas (numeros, y operacion)
def expressions(entry1, entry2, operation):
    # Asegurar que los numeros se puedan convertir a float
    try:
        num1 = float(entry1)
        num2 = float(entry2)
        # Verificar la operacio a realizar
        if operation in ['+', '-', '*', '/', '^']:
            # Si la operacion es '/', y el divisor es '0', mostrar un error
            if operation == '/' and num2 == 0:
                print('Error. Cannot divide by zero')
                return None
            # Si la operacion es '^', y la potencia es 'negativa', mostrar un error
            if operation == '^' and num2 < 0:
                print('Error. Cannot power by a negative number')
                return None
            # Si no hay errorres, retornar los numeros, y la operacion
            return num1, num2, operation
    # Mostrar un error al usuario, si las entradas no se pueden convertir
    except ValueError:
        print('Error. Please insert a valid number')
        return None

# Clase principal para ejecutar el programa
def main():
    # Mensaje de presentacion
    print('Basic calculator. "Exit" to end the program, "records" to take a look at the previous operations\n')
    # Crear una instancia de la clase Calculator
    calc = Calculator(0)
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
            calc.look_register()
            continue
        # operation, realizar una operacion matematica
        if entry.strip().lower() == 'operation':
            # Pedir el numero 1, numero 2, y la operacion a realizar
            num1 = input('First number: ')
            operation = input('Operation (+, -, *, /, ^): ')
            num2 = input('Second number: ')
            # Validar las entradas
            result = expressions(num1, num2, operation)
            # Si las entradas no son validas, salir del ciclo actual, e iniciar uno nuevo
            if not result:
                print('Invalid expression. Insert a valid operation (ex. 5 + 5)')
                continue
            # Obtener los valores ya validados
            num1, num2, op = result
            # Guardar los valores de los numeros en los atributos de la instancia 'calc'
            calc.num1 = num1
            calc.num2 = num2
            # Realizar la operacion seleccionada
            if op == '+':
                print('Result:', calc.sum())
            elif op == '-':
                print('Result:', calc.sub())
            elif op == '*':
                print('Result:', calc.mul())
            elif op == '/':
                print('Result:', calc.div())
            elif op == '^':
                print('Resutlt', calc.power())
        # si la opcion es diferente, pedir ingresar una opcion valida
        else:
            print('Invalid operation. Insert a valid one')
            continue

# Ejecucion de la funcion principal  
main()