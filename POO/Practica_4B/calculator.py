# Clase Calculator
class Calculator:
    # Definir el metodo constructor
    def __init__(self):
        # Definir los valores privados
        self._numbers = []
        self._operators = []
        self._records = []
        self._total = 0
    # Asignar el primer valor, y agregarlo a la lista de numeros
    def assign_value(self, first_value):
        self._total = first_value
        self._numbers.append(first_value)
    # Metodo para registrar los numeros, y operaciones
    def register_calculation(self, operation, value):
        self._numbers.append(value)
        self._operators.append(operation)
    # Metodo para registrar las operaciones en el historial
    def register_operation(self):
        if len(self._operators) == 0:
            print('There are not operations')
            return
        operation = ''
        total_numbers = len(self._numbers)
        for i in range(total_numbers):
            if i == total_numbers - 1:
                operation += f' {self._numbers[total_numbers - 1]} = {self._total}'
            else:
                operation += f'{self._numbers[i]} {self._operators[i]} '
        # Agregar la operacion al historial
        self._records.append(operation)
    # Metodo para mostrar los valores del historial al usuario
    def look_records(self):
        print('these are your operations')
        for operation in self._records:
            print(operation)
    # Metodo para ejecutar la suma, y llamar al metodo 'register_calculation'
    def sum(self, value):
        self._total += value
        self.register_calculation('+', value)
        return self
    # Metodo para ejecutar la resta, y llamar al metodo 'register_calculation'
    def sub(self, value):
        self._total -= value
        self.register_calculation('-', value)
        return self
    # Metodo para ejecutar la multiplicacion, y llamar al metodo 'register_calculation'
    def multiply(self, value):
        self._total *= value
        self.register_calculation('*', value)
        return self
    # Metodo para ejecutar la division, y llamar al metodo 'register_calculation'
    def divide(self, value):
        if value == 0:
            raise ValueError('Cannot divide by zero')
        self._total /= value
        self.register_calculation('/', value)
        return self
    # Metodo para ejecutar la potencia, y llamar al metodo 'register_calculation'
    def power(self, value):
        self._total **= value
        self.register_calculation('^', value)
        return self
    # Obtener el total de la operacion
    def get_total(self):
        self.register_operation()
        return self._total
    # Limpiar los valores privados
    def clear(self):
        self._total = 0
        self._numbers = []
        self._operators = []
        return self
        