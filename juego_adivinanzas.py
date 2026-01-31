import random

jugar = True

nombre = input("indica tu nombre: ")
nombre = nombre.upper()
print(f"Hola {nombre} bienvenido al juego del número secreto")

while jugar : 
    numero_secreto = random.randint(1,100)
    cant_intentos = 0
    cant_max_intentos = 5 
    adivinado = False
    
    while not adivinado :
        if not cant_intentos < cant_max_intentos :
            print("GAME OVER")
            print(f"El número secreto era {numero_secreto}")
            respuesta = input("¿Querés volver a jugar? (s/n): ")
            respuesta = respuesta.lower()
            break
        
        entrada = input("Introduce un número del 1 al 99: ")
        numero = int(entrada) 
        cant_intentos += 1
        quedan =  cant_max_intentos - cant_intentos

        if numero == numero_secreto :
            print(f"Felicidades {nombre} has adivinado")
            respuesta = input("¿Querés volver a jugar? (s/n): ")
            respuesta = respuesta.lower()
            adivinado = True
            
        elif numero < numero_secreto :
            print("El número es mayor al ingresado")
            print(f"Te quedan {quedan} intentos")
        
        else :
            print("El número es menor al ingresado")
            print(f"Te quedan {quedan} intentos")
        
    if respuesta in ["s", "si", "sí"]:
        jugar = True
    else :
        jugar = False

print(f"Gracias por jugar {nombre}")