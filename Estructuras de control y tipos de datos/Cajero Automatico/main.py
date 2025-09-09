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

fithty_bill = 10
hundred_bill = 10
two_hundred_bill = 10
five_hundred_bill = 10
thousand_bill = 10
6
def atm(amount):
    global fithty_bill, hundred_bill, two_hundred_bill, five_hundred_bill, thousand_bill

    if (amount > 0):
        print("yes")
    else:
        print("no")

answer = input("Insert the total amount (0 to close the program): ")
amount = int(answer)

atm(amount)
