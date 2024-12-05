import random

print("Hola")
nombre = input("INGRESA TU NOMBRE: ")

print(f"Que tal {nombre}, bienvenido al juego mas divertido donde intentaras adivinar el numero que estoy pensando")

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0



    while True:
        try:
        
            numero_jugador = int(input("INGRESA TU NUMERO: "))
            intentos += 1
        
            if numero_secreto == numero_jugador:
                print(f"Bien! acertaste el numero en {intentos} intentos")
                break
            else: 
                print("Chale numero incorrecto, intenta de nuevo")
                if numero_secreto < numero_jugador:
                    print("El numero es mas bajo")
                else: 
                    print("El numero es mas alto")
        except ValueError:
            print("Ingresa un numero valido")
    
    jugar_otra_vez()

def jugar_otra_vez():
    while True:

        respuesta = input("¿Deseas jugar nuevamente?(Si o No): ").lower()
    
        if respuesta == ("si"):
            print("Excelente juguemos de nuevo!")
            jugar()
        elif respuesta == ("no"):
            print("Bueno, nos vemos la proxima!")
            break
        else:
            print("Respuesta no valida, intenta de nuevo")


jugar()