"""

La calculadora debe cumplir los siguientes requisitos:

- Debe manejar las cuatro operaciones aritméticas fundamentales: suma, resta, multiplicación y división.

- El sistema debe leer las expresiones matemáticas en formato de texto, interpretar correctamente los números y operadores,

- validar que los datos ingresados sean correctos, ejecutar el cálculo correspondiente y mostrar el resultado inmediatamente al usuario.

- Debe incluir funcionalidades de historial, que permitan al usuario visualizar todas las operaciones realizadas durante la sesión.

- Debe ejecutarse en un bucle continuo, hasta que el usuario decida salir, mediante un comando especial.

- El programa debe manejar la interacción con el usuario con mensajes claros, procesar comandos especiales y gestionar errores (división entre cero, entradas no válidas, etc.).

"""
# Clase Calculator
class Calculator:
    # Definir el metodo constructor
    def __init__(self):
        # numero 1, numero 2, historial
        self._records = []
        self._num1 = 0
        self._num2 = 0
    # Getters, obtener el valor de los atributos protegidos
    @property
    def num1(self):
            return self._num1
    
    @property
    def num2(self):
            return self._num2
    # Setters, cambiar el valor de los atributos protegidos
    @num1.setter   
    def num1(self, new_num1):
        # Verificar que los valores sean de tipo int, o float
        if type(new_num1) in (int, float):
            self._num1 = new_num1
        else:
            raise ValueError('Insert a valid number')
        
    @num2.setter   
    def num2(self, new_num2):
        if type(new_num2) in (int, float):
            self._num2 = new_num2
        else:
            raise ValueError('Insert a valid number')
    # Metodo para registrar las operaciones en el historial
    def _register(self, operation, value):
        result = {f'{self._num1} {operation} {self._num2}': value}
        self._records.append(result)
    # Metodo para mostrar los valores del historial al usuario
    def look_register(self):
        if not self._records:
            print('There are not operations')
            return
        else:
            print('Operation Records')
            i = 1
            for op in self._records:
                print(f'Operarion number {i} --> {op}')
                i += 1
    # Metodo para ejecutar la suma, y llamar al metodo '_register'
    def sum(self):
        result = self._num1 + self._num2
        self._register('+', result)
        return result
    # Metodo para ejecutar la resta, y llamar al metodo '_register'
    def sub(self):
        result = self._num1 - self._num2
        self._register('-', result)
        return result
    # Metodo para ejecutar la multiplicacion, y llamar al metodo '_register'
    def mul(self):
        result = self._num1 * self._num2
        self._register('*', result)
        return result
    # Metodo para ejecutar la division, y llamar al metodo '_register'
    def div(self):
        result = self._num1 / self._num2
        self._register('/', result)
        return result
# Funcion para verificar las entradas (numeros, y operacion)
def expressions(entry1, entry2, operation):
    # Asegurar que los numeros se puedan convertir a float
    try:
        num1 = float(entry1)
        num2 = float(entry2)
        # Verificar la operacio a realizar
        if operation in ['+', '-', '*', '/']:
            # Si la operacion es '/', y el divisor es '0', mostrar un error
            if operation == '/' and num2 == 0:
                print('Error. Cannot divide by zero')
                return None
            # Si no hay errorres, retornar los numeros, y la operacion
            return num1, num2, operation
    # Mostrar un error al usuario, si las entradas no se pueden convertir
    except ValueError:
        print('Error. Please insert a valid number')
        return None

# Clase principal para ejecutar el programa
def main():
    # Crear una instancia de la clase Calculator
    calc = Calculator()
    # Mensaje de presentacion
    print('Basic calculator. "Exit" to end the program, "records" to take a look at the previous operations\n')
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
            operation = input('Operation (+, -, *, /): ')
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
        # si la opcion es diferente, pedir ingresar una opcion valida
        else:
            print('Invalid operation. Insert a valid one')
            continue

# Ejecucion de la funcion principal  
main()