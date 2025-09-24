# Clase Calculator
class Calculator:
    # Definir el metodo constructor
    def __init__(self, init_value):
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
    # Metodo para ejecutar la potencia, y llamar al metodo '_register'
    def power(self):
        result = pow(self._num1, self._num2)
        self._register('^', result)
        return result