from misfunciones import *
import numpy as np
import time
from misvariables import *


# Presentacion Instrucciones

print(INTRO_INSTR)
# Podría haber ampliado incluso poniendo un menu con salir, etc... pero .....tiempo para otras CLASES

time.sleep(2)



# Inicializa los tableros

tablero_maq_barcos_ocultos = np.full((10,10), " ")
tablero_maq = tablero_con_barcos_maq()
tablero_jugador = tablero_con_barcos_jug()

# Vidas de los jugadores, para acortar juego pongo 3, pero 
# realmente son 20 posiciones o vidas por contricante, al igual
# que casillas de cada una de las flotas

vidas_jugador = 20
vidas_maq = 20

    # Comenzar juego y gestion de turnos
while vidas_jugador > 0 and vidas_maq > 0: #mientras se cumpla esta condicion el juego estara on
    
    casilla = disparo_jugador(tablero_maq,tablero_maq_barcos_ocultos) #primer turno(jugador), y luego cada vez q falle maq, casilla donde dispara el jug
                                                                     #se chequea si el disparo es correcto, formato, o si es repetido
    check_disparo_jug(tablero_maq,tablero_maq_barcos_ocultos,casilla)# comprueba si es agua o es TOCADO

    if tablero_maq[casilla] == 'X':#si es tocada la maq
        vidas_maq -= 1 # se le quita una vida a la maq
        if vidas_maq == 0: # se comprueba si las vidas de la maq son 0 para parar juego y turnos
            print('Ganastes eres un auténtico bucanero')
            break # para juego y turnos
        print ('le quedan a la maq. aun',vidas_maq,' vidas\n') #dice las vidas q le van quedando a la maq
        
        
    elif tablero_maq[casilla] != 'X': # si el jugador no acierta, dispara la maquina
        casilla_maquina = disparo_maq(tablero_jugador) # genera casilla disparo maq y comprueba si es repetida
        time.sleep(3)
        check_disparo_maq(tablero_jugador,casilla_maquina)#comprueba si maq da en agua o TOCADO
        time.sleep(3)
        while tablero_jugador[casilla_maquina] == 'X' and vidas_jugador > 0: #si es TOCADO, while para repetir hasta q falle
            vidas_jugador -= 1 # se le quita una vida al jugador
            if vidas_jugador == 0: # se comprueba si las vidas del jugador son 0 para parar juego y turnos
                  print('Perdistes, la maquina te gano la partida') 
                  break # para juego y turnos
            print ('al jugador le quedan aun',vidas_jugador, 'vidas\n')
            print ('La maquina vuelve a disparar\n') #dice las vidas q le van quedando al jugador
            
            
            casilla_maquina = disparo_maq(tablero_jugador)#maq vuelve a disparar pq acerto y no ha ganado aun, comprueba si es repetida
            time.sleep(3)
            check_disparo_maq(tablero_jugador,casilla_maquina)#comprueba si maq da en agua o TOCADO
            time.sleep(3)
            # En cuanto termina este while sin haber ganado maq, sale al anterior while para volver
            # a jugar el jugador, e iniciar la ronda de turnos



    
