# Juego de los Barquitos

Juego de toda la vida, también es conocido como Hundir la Flota. Se ha generado con numpy. El reto es hundir los barcos de la máquina antes que ella hunda los tuyos.

**¡Pierde quien se quede sin vidas-barcos!**

## Instrucciones

* Se dispone de un tablero por cada jugador, de 10*10, 100 casillas o posiciones.
* Cada tablero contendra 10 barcos, que ocuparan 20 casillas, se representara cada casilla de barco con una 'O'

    * 1 portaaviones que ocupa 4 casillas
    * 2 acorazados que ocupan 3 casillas cada uno
    * 3 fragatas que ocupan 2 casillas cada una
    * 4 submarinos que ocupan 1 casilla cada uno
  
* Los barcos  se colocan aleatoriamente, para cada contricante, observando que no se pisen ni se salgan del tablero.
* Se dispara, el jugador a una casilla seleccionada por el mismo, y la maquina aleatoriamente. 
* Intentando que no se repita, pero si se repite el programa volvera a preguntar por nuevas casillas, o generara aleatoriamente en el caso de la maquina
  1) Si se acierta(se representara como una 'X') se repite,das a uno de los barcos del contrincante, te vuelve a tocar
  2) Si sen falla...agua(se representara como un guion '-')....., le toca disparar al otro contrincante
  

## Recursos utilizados
* Lenguaje utilizado: Python 3.11.5
  * Librerías: 
    * numpy 
    * random
    * time


Este proyecto ha sido elaborado por: Kino Galvez