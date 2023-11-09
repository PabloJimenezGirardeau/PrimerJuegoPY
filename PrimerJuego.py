import random

def adivinar_numero():
    print("¡Adivina el número!")
    numero_secreto = random.randint(0, 99)
    contador = 0


    while True:
        intento = input("Ingresa un número entre 0 y 99: ")
        contador = contador + 1

        if (int(intento)<0) or (int(intento)>99):
           print("NÚMERO INTRODUCIDO FUERA DE RANGO (0,99)")
        else:
           if int(intento) == numero_secreto:
               print("¡Felicidades! ¡Has adivinado el número!")
               print("Número de intentos:", contador)
               #print(contador)
               break
           elif int(intento) < numero_secreto:
               print("Has fallado. El número secreto es mayor.")
           else:
               print("Has fallado. El número secreto es menor.")


adivinar_numero()
