"""  
En  una  empresa  se  quiere  crear  un  sistema  de  inicio  de  sesión  con  un número limitado de intentos. 
El sistema debe pedir al usuario su nombre de  usuario  y  contraseña.  Para  crear  dicho  sistema,  ten  en  cuenta  las 
siguientes condiciones:  
• Se permite un máximo de 3 intentos. 
• Mostrar  un  error  al  usuario  cuando  no  exista  uno  de  los  datos 
(usuario y contraseña). 
• Si  uno  de  los  campos  (usuario  y  contraseña)  está  vacío  deberá 
mostrar un error de autentificación. 
• Únicamente usar estructuras de control.
"""

# Credenciales validas
CORRECT_USER = "admin"
CORRECT_PASSWORD = "1234"
# Numero de intentos
ATTEMPS_LEFT = 3
# Variable para controlar el ciclo
VALID_CREDENTIALS = False

# Funcion para reducir el numero de intentos
def subtract_attemp():
    globals()['ATTEMPS_LEFT'] -= 1

# Menu principal
print("LOG IN PROGRAM")

# Ciclo while para iterar el numero de intentos
while not VALID_CREDENTIALS and ATTEMPS_LEFT > 0:
    # Mostrar intentos restantes
    print(f"Attempts left {ATTEMPS_LEFT}")
    # Entradas del usuario
    user = input("Insert the user name: ")
    password = input("Insert the password: ")
    # Validar ambas credenciales
    if user == CORRECT_USER and password == CORRECT_PASSWORD:
        VALID_CREDENTIALS = True
        print("Valid Credentials. You log in successfully")
    # Validar si las dos credenciales son erroneas
    elif user != CORRECT_USER and password != CORRECT_PASSWORD:
        subtract_attemp()
        print("Invalid Credentials (User and Password)")
    # Validar si el usuario es correcto
    elif user != CORRECT_USER:
        subtract_attemp()
        print("Invalid User")
    # Validar si la contrasena es correcto
    elif password != CORRECT_PASSWORD :
        subtract_attemp()
        print("Invalid Password")
    # Cualquier otro valor sera invalido
    else:
        subtract_attemp()
        print("Insert valid credentials")
