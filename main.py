# Importamos los módulos necesarios
from palabras import nivel_1
from palabras import nivel_2
from palabras import nivel_3
from palabras import nivel_4
import random


# Función menu que se mostrará al principio del juego

def menu_principal():
    print("\nBienvenido a Connections.")
    opcion = int(input("\nIntroduce un 1 para jugar: "))

    # Si se introduce cualquier otra cosa que no sea un 1 aparece un error y lo vuelve a pedir
    while opcion != 1:
        print("La opción introducida no es válida.")
        opcion = int(input("\nIntroduce un 1 para jugar: "))

    palabras_por_categoria = int(input("\nIntroduce el número de palabras por categorías que desees (entre 3 y 6): "))
    while palabras_por_categoria not in range(3, 7):
        print("\nEl valor introducido no es válido, debe estar entre 3 y 6 incluidos.")
        palabras_por_categoria = int(input("Introduce el número de palabras por categorías que desees (entre 3 y 6): "))

    numero_intentos = int(input("\nIntroduce el número de intentos deseado (entre 3 y 8): "))
    while numero_intentos not in range(3, 9):
         print("\nEl valor introducido no es válido, debe estar entre 3 y 8 incluidos.")
         numero_intentos = int(input("Introduce el número de intentos deseado (entre 3 y 8): "))

    print("\nNúmero de palabras de cada nivel:", palabras_por_categoria)
    print("Número de intentos:", numero_intentos)

    return palabras_por_categoria, numero_intentos

def menu_secundario(intentos):
    print("\nIntentos restantes:", intentos)
    print("----------------------------")
    print("Tienes las siguientes opciones disponibles")
    print("*- Escribe una palabra para seleccionarla o deseleccionarla")
    print("1- Revolver las palabras")
    print("2- Comprobar")
    print("3- Salir del juego")
    entrada = input()

    return entrada


# Funcion que obtiene la lista de la que se eligiran las cuatro palabras relacionas y esas cuatro palabras

def indices_aleatorios(palabras_por_categoria):
    lista = []
    lista.append(random.randint(0, 9))  # Indice correspondiente a la lista

    # Cuatro indices correspondientes a cuatro elementos aleatorios de esa lista
    # Todas las listas tienen 10 elementos, ya que el elemento onceavo es la tematica de esa lista

    while len(lista) < palabras_por_categoria + 1:
        numero = random.randint(0, 9)
        if numero not in lista:
            lista.append(numero)

    # El primer indice va a ser el indice de la lista, mientras que los otros cuatro van a ser los indices de las palabras de esa lista
    return lista


# Función que obtiened palabras aleatorias de cada nivel y las devuelve en una lista

def obtencion_palabras_mostradas(nivel_1, nivel_2, nivel_3, nivel_4, palabras_por_categoria):
    palabras_nivel_1 = []
    indices_nivel_1 = indices_aleatorios(palabras_por_categoria)
    tematica_1 = nivel_1[indices_nivel_1[0]][-1]

    for i in range(1, palabras_por_categoria + 1):
        palabras_nivel_1.append(nivel_1[indices_nivel_1[0]][indices_nivel_1[i]])

    palabras_nivel_2 = []
    indices_nivel_2 = indices_aleatorios(palabras_por_categoria)
    tematica_2 = nivel_2[indices_nivel_2[0]][-1]

    for i in range(1, palabras_por_categoria + 1):
       palabras_nivel_2.append(nivel_2[indices_nivel_2[0]][indices_nivel_2[i]])

    palabras_nivel_3 = []
    indices_nivel_3 = indices_aleatorios(palabras_por_categoria)
    tematica_3 = nivel_3[indices_nivel_3[0]][-1]

    for i in range(1, palabras_por_categoria + 1):
       palabras_nivel_3.append(nivel_3[indices_nivel_3[0]][indices_nivel_3[i]])

    palabras_nivel_4 = []
    indices_nivel_4 = indices_aleatorios(palabras_por_categoria)
    tematica_4 = nivel_4[indices_nivel_4[0]][-1]

    for i in range(1, palabras_por_categoria + 1):
       palabras_nivel_4.append(nivel_4[indices_nivel_4[0]][indices_nivel_4[i]])
    
    return palabras_nivel_1, palabras_nivel_2, palabras_nivel_3, palabras_nivel_4, tematica_1, tematica_2, tematica_3, tematica_4


# Funciñon que elige las palabras en una posicion aleatoria

def palabras_posicion_aleatoria(longitud_palabras_mostradas):
    numeros_elegidos = []

    # Coloca los numeros del 0 al 15 (correspondientes a los indices de las palabras mostradas) de forma aleatoria
    while len(numeros_elegidos) < longitud_palabras_mostradas:
        numero = random.randint(0, longitud_palabras_mostradas - 1)
        if numero not in numeros_elegidos: # Comprueba que no se haya añadido ya ese número a la lista
            numeros_elegidos.append(numero)

    return numeros_elegidos


# Función que imprime las palabras en su posicion correspondiente y que nos permite marcar y desmarcar palabras

def imprimir_palabras(palabras_mostradas, numeros_elegidos, palabras_por_categoria, lista_palabras_marcadas, lista_niveles_completados, palabras_nivel_1, palabras_nivel_2, palabras_nivel_3, palabras_nivel_4, tematica_1, tematica_2, tematica_3, tematica_4):
    # Imprime los numeros en una matriz 4 x 4 
    fila = 0

    for i in range(0, 4):
        print()
        # Si la fila está en la de niveles completados se imprimen las palabras de ese nivel
        if i in lista_niveles_completados:
            if i == 0:
                print() #Línea en blanco
                for elemento in palabras_nivel_1:
                    print(f"{elemento:10}", end ="\t\t")
                print("Nivel 1:", tematica_1)
            elif i == 1:
                print() #Línea en blanco
                for elemento in palabras_nivel_2:
                    print(f"{elemento:10}", end ="\t\t")
                print("Nivel 2:", tematica_2)
            elif i == 2:
                print() #Línea en blanco
                for elemento in palabras_nivel_3:
                    print(f"{elemento:10}", end ="\t\t")
                print("Nivel 3:", tematica_3)
            else:
                print() #Línea en blanco
                for elemento in palabras_nivel_4:
                    print(f"{elemento:10}", end ="\t\t")
                print("Nivel 4:", tematica_4)

        else:
            for n in range(palabras_por_categoria * fila, palabras_por_categoria * fila + palabras_por_categoria):
                if palabras_mostradas[numeros_elegidos[n]] in lista_palabras_marcadas:
                    print(f"** {palabras_mostradas[numeros_elegidos[n]]:10}", end="\t\t")
                else:
                    print(f"{palabras_mostradas[numeros_elegidos[n]]:10}", end="\t\t")
            fila += 1

    print() # Para que salte de linea
    # QUITAR COMENTARIO PARA MOSTRAR LA SOLUCION print(numeros_solucion)


# Función que recibe dos listas y comprueba si tiene los mismo elemntos
def comprobar_listas(lista_1, lista_2):
    contador = 0 # Cuenta el numero de elementos de una lista que se encuetran también en la otra

    for elemento in lista_1:
        if elemento in lista_2:
            contador += 1
    
    return contador

def main():
    palabras_por_categoria, intentos = menu_principal()
    lista_palabras_marcadas = []
    lista_niveles_completados = []

    print("Palabras por categoria:", palabras_por_categoria)

    # Otenemos las palabras aleatorias de los cuatro niveles
    palabras_nivel_1, palabras_nivel_2, palabras_nivel_3, palabras_nivel_4, tematica_1, tematica_2, tematica_3, tematica_4= obtencion_palabras_mostradas(nivel_1, nivel_2, nivel_3, nivel_4, palabras_por_categoria)
    palabras_mostradas = palabras_nivel_1 + palabras_nivel_2 + palabras_nivel_3 + palabras_nivel_4

    # Obtenemos la posicion aleatoria que ocuparan esas palabras
    numeros_elegidos = palabras_posicion_aleatoria(len(palabras_mostradas))

    while intentos > 0:
        # Mostramos las palabras en pantalla
        imprimir_palabras(palabras_mostradas, numeros_elegidos, palabras_por_categoria, lista_palabras_marcadas, lista_niveles_completados, palabras_nivel_1, palabras_nivel_2, palabras_nivel_3, palabras_nivel_4, tematica_1, tematica_2, tematica_3, tematica_4)
        # Solicitamos una entrada al usuario
        entrada = menu_secundario(intentos).capitalize() # Pone la primera con mayúscula solamente

        if entrada.isdigit() and int(entrada) == 3:
            print("\nGracias por jugar a Connections.")
            return 0 # Se cierra el programa
        
        elif entrada.isdigit() and int(entrada) == 1:
            numeros_elegidos = palabras_posicion_aleatoria(len(palabras_mostradas))

        elif entrada.isdigit() and int(entrada) == 2:
            if len(lista_palabras_marcadas) != palabras_por_categoria:
                print(f"\nPara poder comprobar un conjunto de palabras debes seleccionar {palabras_por_categoria} palabras")
           
            else:
                if comprobar_listas(lista_palabras_marcadas, palabras_nivel_1) == palabras_por_categoria:
                    # Elimina las palabras de ese nivel de la lista de palabras mostradas
                    for elemento in palabras_nivel_1:
                        palabras_mostradas.remove(elemento)

                    # Genera nuevas posciones aleatorias de las palbaras restantes
                    numeros_elegidos = palabras_posicion_aleatoria(len(palabras_mostradas))

                    # Añadimos el nivel a la lista de niveles completados
                    lista_niveles_completados.append(0)

                    # Vaciamos la lista de palabras marcadas
                    lista_palabras_marcadas.clear()

                elif comprobar_listas(lista_palabras_marcadas, palabras_nivel_2) == palabras_por_categoria:
                    # Elimina las palabras de ese nivel de la lista de palabras mostradas
                    for elemento in palabras_nivel_2:
                        palabras_mostradas.remove(elemento)

                    # Genera nuevas posciones aleatorias de las palbaras restantes
                    numeros_elegidos = palabras_posicion_aleatoria(len(palabras_mostradas))

                    # Añadimos el nivel a la lista de niveles completados
                    lista_niveles_completados.append(1)

                    # Vaciamos la lista de palabras marcadas
                    lista_palabras_marcadas.clear()

                elif comprobar_listas(lista_palabras_marcadas, palabras_nivel_3) == palabras_por_categoria:
                    # Elimina las palabras de ese nivel de la lista de palabras mostradas
                    for elemento in palabras_nivel_3:
                        palabras_mostradas.remove(elemento)

                    # Genera nuevas posciones aleatorias de las palbaras restantes
                    numeros_elegidos = palabras_posicion_aleatoria(len(palabras_mostradas))

                    # Añadimos el nivel a la lista de niveles completados
                    lista_niveles_completados.append(2)

                    # Vaciamos la lista de palabras marcadas
                    lista_palabras_marcadas.clear()

                elif comprobar_listas(lista_palabras_marcadas, palabras_nivel_4) == palabras_por_categoria:
                    # Elimina las palabras de ese nivel de la lista de palabras mostradas
                    for elemento in palabras_nivel_4:
                        palabras_mostradas.remove(elemento)
                    
                    # Genera nuevas posciones aleatorias de las palbaras restantes
                    numeros_elegidos = palabras_posicion_aleatoria(len(palabras_mostradas))

                    # Añadimos el nivel a la lista de niveles completados
                    lista_niveles_completados.append(3)

                    # Vaciamos la lista de palabras marcadas
                    lista_palabras_marcadas.clear()
                
                # Si se han acertado todas menos una (da igual el nivel que sea) se imprimer one way
                elif comprobar_listas(lista_palabras_marcadas, palabras_nivel_1) == palabras_por_categoria - 1 or comprobar_listas(lista_palabras_marcadas, palabras_nivel_2) == palabras_por_categoria - 1 or comprobar_listas(lista_palabras_marcadas, palabras_nivel_3) == palabras_por_categoria - 1 or comprobar_listas(lista_palabras_marcadas, palabras_nivel_4) == palabras_por_categoria - 1:
                    print("\nOne way.")
                    intentos -= 1
                
                else:
                    print("\nIncorrecto!")
                    intentos -= 1
            
        # Añadimos o quitamos (dependiendo de si ya está o no) la palabra introducida a la lista_palabras_marcads, simepre y cuando sea una de las que se muestran
        elif entrada in palabras_mostradas:
            if entrada not in lista_palabras_marcadas:
                lista_palabras_marcadas.append(entrada)
            else:
                lista_palabras_marcadas.remove(entrada)

        else:
            print("\nLa opción introducida no es válida")

        # Comprobamos si ya no quedan palabras mostradas, es decir, se han acertado todas, y mostramos el mensaje de la victoria

        if len(palabras_mostradas) == 0:
            print("\n¡Enhorabuena, has ganado!")
            print("\n------------------------------")
            print()
            for elemento in palabras_nivel_1:
                print(f"{elemento:10}", end="\t\t")
            print("Nivel 1:", tematica_1)
            print()
            for elemento in palabras_nivel_2:
                print(f"{elemento:10}", end="\t\t")
            print("Nivel 2:", tematica_2)
            print()
            for elemento in palabras_nivel_3:
                print(f"{elemento:10}", end="\t\t")
            print("Nivel 3:", tematica_3)
            print()
            for elemento in palabras_nivel_4:
                print(f"{elemento:10}", end="\t\t")
            print("Nivel 4:", tematica_4)
            print()
            return 0

    print("\nLo siento, no te quedan más intentos, has perdido :(")

if __name__ == "__main__":
    main()
