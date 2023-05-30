#trabajo de Braihan Gonzalez, Esteban Parra, Ignacion Ruiz

import random
numeros_sorteados = random.sample(range(1, 50), 5)
print("¡Bienvenido a la lotería!")
print("Elige 5 números del 1 al 49")
numeros_elegidos = []
for i in range(5):
    while True:
        try:
            numero = int(input("Ingresa el número {}: ".format(i+1)))#format(i+1) esto formatea la cadena y reemplaza {} con el valor de i+1.
            if numero < 1 or numero > 49:
                print("El número debe estar entre 1 y 49. Inténtalo de nuevo.")
            else:
                numeros_elegidos.append(numero)
                break
        except ValueError:
            print("Ingresa un número válido. Inténtalo de nuevo.")

print("Usted ingresó los siguientes números: ", numeros_elegidos)
print("Los números sorteados fueron:")
for numero in numeros_sorteados:
    print(numero)

aciertos = set(numeros_sorteados) & set(numeros_elegidos)#el "&"" devuelve un nuevo conjunto que contiene los elementos comunes entre ambos conjuntos.
num_aciertos = len(aciertos)

if num_aciertos == 5:
    print("¡Felicidades! Has ganado la lotería.")
else:
    print("Lo siento, no has ganado. Mejor suerte la próxima vez.")