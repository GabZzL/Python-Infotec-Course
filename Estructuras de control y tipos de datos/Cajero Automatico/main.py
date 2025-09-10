"""  
Has sido contratado por un banco que está en proceso de actualizar el
software de sus cajeros automáticos. Tu tarea es desarrollar un algoritmo
básico que simule el funcionamiento de un cajero automático, tomando
como referencia las siguientes condiciones:

* Entregar siempre la menor cantidad de billetes posible.
* Mantener un inventario que indique cuál es la cantidad de billetes
disponible por cada denominación.
* Las denominaciones disponibles son: 50, 100, 200, 500 y 1000.
* Si el inventario no cuenta con una combinación de billetes
suficientes para satisfacer el importe solicitado, no dispensará
ningún billete. 
* Siempre que inicie el algoritmo, deberá haber en inventario 10
billetes de cada denominación.
"""

# Variables para contar billetes
FIFTY_BILL = 10
ONE_HUNDRED_BILL = 10
TWO_HUNDRED_BILL = 10
FIVE_HUNDRED_BILL = 10
THOUSAND_BILL = 10

# Variables para entregar billetes
FIFTY_BILL_COUNT = 0
ONE_HUNDRED_BILL_COUNT = 0
TWO_HUNDRED_BILL_COUNT = 0
FIVE_HUNDRED_BILL_COUNT = 0
THOUSAND_BILL_COUNT = 0

IS_RUNNING = True

def calculate(amount):  
    # Use a dictionary to map denominations to their variable names
    denominations = {
        1000: 'THOUSAND_BILL',
        500: 'FIVE_HUNDRED_BILL',
        200: 'TWO_HUNDRED_BILL',
        100: 'ONE_HUNDRED_BILL',
        50: 'FIFTY_BILL'
    }

    # Iterar en los valores en orden decendente
    for bill, var_name in denominations.items():
        if amount >= bill and globals()[var_name] > 0:
            amount -= bill
            # globals() para modificar las variables globales
            globals()[var_name] -= 1
            globals()[var_name + "_COUNT"] += 1
            return amount

# Inicio del programa
# Pedir un monto al usuario
answer = input("Insert the total amount (0 to close the program): ")
# Transformar la entrada a un numero entero
amount = int(answer)

# Loop principal
# se ejecutara hasta que el monto sea menor que el valor del billete con menos valor 
while IS_RUNNING:
    if amount >= 50:
        amount = calculate(amount)
    else:
        IS_RUNNING = False

print(f"Here's your change {amount}")
print("YOUR BILLS:")
print(f"THOUSAND_BILL: {THOUSAND_BILL_COUNT}")
print(f"FIVE HUNDRED BILL: {FIVE_HUNDRED_BILL_COUNT}")
print(f"TWO HUNDRED BILL: {TWO_HUNDRED_BILL_COUNT}")
print(f"ONE HUNDRED BILL: {ONE_HUNDRED_BILL_COUNT}")
print(f"FYFTY BILL: {FIFTY_BILL_COUNT}")
