import random

jugar = True

nombre = input("indica tu nombre: ") #Para personalizar el juego
nombre = nombre.upper() #Con upper deja todo en mayúsculas
print(f"Hola {nombre} bienvenido al juego piedra, papel o tijera") #con f => (f"Hola {nombre} bienvenido al juego piedra, papel o tijera") o f-string => ("Hola {} bienvenido al juego piedra, papel o tijera {}".format(nombre))

rondas = 3 #Se define un máximo de 3 rondas por juego. 

while jugar and rondas >= 3: #Entra todo en esta función. Hacer 3 rondas, 
    puntos_j1 = 0
    puntos_j2 = 0
    
    for ronda in range(1, rondas + 1):
        print(f"\nRonda {ronda}")
        j1 = input(f"{nombre} ¿Que eliges? ¿piedra, papel o tijera?: ").strip().lower()
        if j1.startswith("pi") :
            j1 = "piedra"
        elif j1.startswith("pa") :
            j1 = "papel" 
        elif j1.startswith("ti") :
            j1 = "tijera"
        else : 
            j1 = None
        
        print(f"\n{nombre}:" + j1.strip().lower())
        opciones = ["piedra", "papel" , "tijera"]
        j2 = random.choice(opciones)
        print("YO: " + j2)      
        
        if j1 == j2 :
            print("Es un empate")
            
        elif (j1 == "piedra" and j2 == "tijera") or (j1 == "papel" and j2 == "piedra") or (j1 == "tijera" and j2 == "papel"):
            print(f"Ha ganado {nombre}")
            puntos_j1 += 1 
        
        else:
            print("He ganado YO")
            puntos_j2 += 1 
        
    if rondas == 3 :
        jugar = False
        print("\nResultados")
        print(f"{nombre}: {puntos_j1} puntos")
        print(f"YO: {puntos_j2} puntos")
        
        if puntos_j1 > puntos_j2:
            print(f"Felicidades {nombre}, GANASTE")
        
        elif puntos_j2 > puntos_j1:
            print("GANÉ YO")
        
        else :
            print("Es un EMPATE")

        respuesta = input("\n¿Querés volver a jugar? (s/n): ")
        respuesta = respuesta.lower()
        if respuesta in ["s", "si", "sí"]:
            jugar = True
    


   

