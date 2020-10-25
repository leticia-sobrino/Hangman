# Hangman
## Índice:
  ### 1. DEFINICION DEL JUEGO
  ### 2. PERSONALIZADO
  ### 3. REGLAS
  ### 4. NO ME VAS A PILAR 😉
  ### 5. PASOS PARA PICAR CÓDIGO
  ### 6. ¿PREGUNTAS?
  ### 7. SE ACEPTAN TIPS Y ADVICES :blush:
  ### 8. ¡A JUGAR Y MUCHA SUERTE! :crossed_fingers:


# 1. DEFINICION DEL JUEGO
    El mítico juego del “Ahorcado” es un juego de adivinanzas de lápiz y papel para dos o más jugadores. Un jugador piensa una palabra y el otro trata de adivinarla según la longitud de la palabra que se representa con guiones. 


# 2. PERSONALIZADO
    En nuestro caso, ¡vamos a digitalizar este juego! El fin del juego será exactamente el mismo que el juego tradicional pero lo único que va a cambiar es el número de jugadores. Solo va a poder jugar un jugador en cada ronda y, jugará contra el ordenador. ¿Asombroso no?
    El ordenador elegirá una palabra al azar de una lista que le ha sido proporcionada y el jugador, es decir TU, vas a tener que adivinarla! Se te dará el topic de la lista para que te puedas poner en contexto del juego y de el tipo de palabra que vas a tener que adivinar. En este caso nuestro topic será LOS NOMBRES DE NUESTRA CLASE DE IRONHACK!!.
    Para hacerlo un poco más entretenido no solamente hay nombres propios, sino que también te puedes encontrar con apodos, apellidos o mezclas de nombres y apellidos. La gracias también es poder diferenciar a cada persona de la clase y como ya sabéis que en nuestra clase se repite algún que otro nombre, vamos a tener que darle más al coco. 

# 3. REGLAS
    Vamos a establecer unas reglas del juego por si las moscas... :
        -	Intentar adivinar la palabra introduciendo una letra (vocal o consonante) cuando el ordenador te lo pida.
        -	Fíjate en los guiones! Te dará alguna pista para adivinarla
        -	Diviértete y entretente un rato con el ordenador!
        -	Y la última y más importante no cabrearse si pierdes!!! Ajjajaa te recuerdo que es un ordenador!! No lo tires por la        ventana que tienes que acabar el Bootcamp 😉

# 4. NO ME VAS A PILAR 😉
        -	Las letras que introduzcas me da igual que sean minúsculas o mayúsculas
        -	Si le das a “enter” sin haber metido ninguna letra el ordenador te va a volver a pedir que introduzcas una letra
        -	Si metes algún número o algún carácter especial no me la vas a jugar… te van a volver a pedir una letra!

# 5. PASOS PARA PICAR CÓDIGO
        1º Importar las siguientes dos funciones:
            - "import random": Para que el ordenador obtenga una palabra aleatoria de la lista que le he proporcionado y que el usuario va a tener que adivinar.
            - "import os": Es una función que nos permite limpiar la pantalla, es decir cada vez que juegues se te limpiará la pantalla de las partidas anteriores. Para poner un poquito de orden y limpieza! :blush:
        2º Crear una lista (en este caso llamada "names") que contenga todos los nombres con los que vamos a jugar.

        3º Importar la funcion random con nuestra lista de nombres para que el ordenador escoja al azar en cada partida un nombre diferente de la lista. La sintaxis de la función es la siguiente : name = random.choice(names)

        4º. Mediante cadenas de caracteres definimos los dibujos que van a ir saliendo por las veces que se va fallando. Si llegas a este último PIERDES!! CUIDADO!!
                              
           _ _
          |   o
          |  /|/
          |  / /
        __|__
        
        5º Asignamos variables

        6º Creamos nuestro bucle principal del juego. He escogido utilizar el "while loop" porque toda letra que se introduzca se va a determinar si es Verdadera o Falsa.
        Dentro de este bucle nos vamos a encontrar:
            - Una función que vaya imprimiento a medida que vaya habiendo algun fallo el dibujo correspondiente.
            - Una función que muestre las letras acertadas y guiones bajos en las letras que aun no se hayan acertado (aparece debajo del dibujo porque llamos a la función después)
            - Una funcion que indique si el resultado de las letras que has ido introduciendo es igual al nombre de la lista, entonces te dirá si has ganado o perdido la partida. 
            - Una función con las condiciones de las letras que el jugador va a introducir durante su partida.
            - Y, una última funcion que vaya contando el numero de fallos y aciertos del jugador para que así pueda volver a la primera función que determinamos y pueda imprimir el dibujo correspondiente si es necesario. 


# 6. ¿PREGUNTAS?
    Puedes preguntar si tienes alguna duda!! Intentaré resolvértela de la mejor manera posible :) ¡PARA ESO ESTAMOS!

# 7. SE ACEPTAN TIPS Y ADVICES :blush:
    Toda crítica constructiva es bienvenida!!! Estamos aquí para eso! :)
    Me encantará escucharte!!!

# 8. ¡A JUGAR Y MUCHA SUERTE! :crossed_fingers:
    ¡Espero que os haya gustado! 

