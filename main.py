# para que el ordeandor pueda obtener una palabra aleatoria de la lista que le voy a proporcionar
import random
import os

names = ["RAS", "ANA", "ADRIANA", "LAZARO", "DELGADO", "FELIPE", "FER", "IGANACIO", "JMANUEL", "CALCEDO", "JAVIER", "JESUS", "JOSEGOMEZ", "JUANB", "JUANM", "JUANPE", "VAZQUEZ", "LUCIANA", "MARIANA", "MARIO", "MARTA", "NURIA", "PATRICIA", "TREVIÑO", "RAFA", "SANTIAGO", "SERGIO", "SERGIOGON", "SHERIFF", "SONIA", "LETI"]
name = random.choice(names)

# Mediante cadenas de caracteres hacemos los dibujos que van a ir saliendo por las veces que se va fallando
fallo_0 = '''
           _ _
          |   
          |  
          | 
        __|__
'''

fallo_1 = '''
           _ _
          |   o
          |  
          |  
        __|__
'''

fallo_2 = '''
           _ _
          |   o
          |   |
          |   
        __|__
'''

fallo_3 = '''
           _ _
          |   o
          |  /|
          |  
        __|__
'''

fallo_4 = '''
           _ _
          |   o
          |  /|\
          |   
        __|__
'''
fallo_5 = '''
           _ _
          |   o
          |  /|\
          |  / 
        __|__
'''

fallo_6 = '''
           _ _
          |   o
          |  /|\
          |  / \
        __|__
'''

#VARIABLES
correct_letter = ""
all_letters = ""
fallos = 0

# Bucle principal
while True:

    os.system("cls")

    print("Hangman game")
    
    # Para ir imprimiento a medida que vaya habiendo algun fallo el dibujo correspondiente
    if fallos == 0:
        print(fallo_0)
    elif fallos == 1:
        print(fallo_1)
    elif fallos == 2:
        print(fall0_2)
    elif fallos == 3:
        print(fallo_3)
    elif fallos == 4:
        print(fallo_4)
    elif fallos == 5:
        print(fallo_5)
    else:
        print(fallo_6)
    
    print()

    # Mostras letras acertadas y giones bajos en las letras que aun no se hayan acertado
    result = ""

    for letter in name:
        if letter in correct_letter:
            result += letter
        else:
            result += " _ "
    
    print("     {}".format(result))
    
    print()
    print()

    if result = name:
        print("YOU WON!! CONGRATS!! :) ")
        break
    if fallos > 5:
        print("OOOH SORRY YOU LOST :( , The word was: ", name)
        break
    
    while True:
        letra_usuario_sin_formato = input("Dime una letra: ")
        letra_usuario = letra_usuario_sin_formato.upper()

        if len(letra_usuario) < 1 o len(letra_usuario) > 1:
            print("Introduce una letra por favor: ")
        elif letra_usuario in all_letters:
            print("Esa letra ya la has dicho!")
        elif letra_usuario not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            print("No vale un carater, introduce letra: ")
        else:
            all_letters += letra_usuario
            break

        if letra_usuario not in name:
            fallos += 1
        else:
            correct_letter += letra_usuario
            
        

    




