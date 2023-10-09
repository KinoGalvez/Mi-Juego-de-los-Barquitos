import numpy as np
from misvariables import BARCOS
import random

def posicionar_barco_jug (long,tablero_jug):#generar posiciones de un barco para jugador

    
    i = False # Mientras sea False se ejecuta, hasta que posicione un
              # barco de eslora ,long en el tablero del jugador
    while i == False:
        # Genera los punto de inicio de los barcos aleatoriamente
        fila_ini = random.randint(0,9)
        colum_ini = random.randint(0,9)
        orientacion = random.randint(0,3) # 0=N, 1=S, 2=E Y 3=O
        
        if orientacion == 0 and (fila_ini - long) >= 0: # orientax N y entra dentro del marco
            
            if 'O' in tablero_jug[fila_ini:fila_ini-long:-1, colum_ini:colum_ini+1]:#comprobar si se cruza con otro barco
                                                                                    
                i = False # sigue ejecutandose al haberse cruzado las posiciones con otro barco
            else:
                tablero_jug[fila_ini:fila_ini-long:-1, colum_ini:colum_ini+1] = 'O'
                i= True # Ya pinta el barco, en posiciones no ocupadas y para el bucle
                return tablero_jug # Pinta el barco en el tablero
                
        elif orientacion == 1 and (fila_ini + long) < 9: # orientax S y entra dentro del marco
            if 'O' in tablero_jug[fila_ini:fila_ini+long:+1, colum_ini:colum_ini+1]:#comprobar si se cruza con otro barco
                
                i = False # sigue ejecutandose al haberse cruzado las posiciones con otro barco
            else:
                tablero_jug [fila_ini:fila_ini+long:+1, colum_ini:colum_ini+1] = 'O'
                i = True # Ya pinta el barco, en posiciones no ocupadas y para el bucle
                return tablero_jug # Pinta el barco en el tablero
                

        elif orientacion == 2 and (colum_ini + long) < 9: # orientax E y entra dentro del marco
            if 'O' in tablero_jug[fila_ini:fila_ini+1, colum_ini:colum_ini+long]:#comprobar si se cruza con otro barco
                
                i = False # sigue ejecutandose al haberse cruzado las posiciones con otro barco
            else:
                tablero_jug [fila_ini:fila_ini+1, colum_ini:colum_ini+long] = 'O'
                i = True  # Ya pinta el barco, en posiciones no ocupadas y para el bucle
                return tablero_jug # Pinta el barco en el tablero
                
            
        elif orientacion == 3 and (colum_ini - long) >= 0: # orientax O y entra dentro del marco
            if 'O' in tablero_jug[fila_ini:fila_ini+1, colum_ini:colum_ini-long:-1]:#comprobar si se cruza con otro barco
                
                i = False # sigue ejecutandose al haberse cruzado las posiciones con otro barco
            else:    
                tablero_jug [fila_ini:fila_ini+1, colum_ini:colum_ini-long:-1] = 'O'
                i = True # Ya pinta el barco, en posiciones no ocupadas y para el bucle
                return tablero_jug # Pinta el barco en el tablero
        


def posicionar_barco_maq(long,tablero_maq):#generar posiciones de un barco para maquina


    import random
    i = False# Mientras sea False se ejecuta, hasta que posicione un
              # barco de eslora ,long en el tablero del maquina

    while i == False:
        # Genera los punto de inicio de los barcos aleatoriamente
        fila_ini = random.randint(0,9)
        colum_ini = random.randint(0,9)
        orientacion = random.randint(0,3) # 0=N, 1=S, 2=E Y 3=O
       
        if orientacion == 0 and (fila_ini - long) >= 0:# orientax N y entra dentro del marco
            
            if 'O' in tablero_maq[fila_ini:fila_ini-long:-1, colum_ini:colum_ini+1]:#comprobar si se cruza con otro barco
                
                i = False# sigue ejecutandose al haberse cruzado las posiciones con otro barco
            else:
                tablero_maq[fila_ini:fila_ini-long:-1, colum_ini:colum_ini+1] = 'O'
                i= True # Ya pinta el barco, en posiciones no ocupadas y para el bucle
                return tablero_maq# Pinta el barco en el tablero
                
        elif orientacion == 1 and (fila_ini + long) < 9:# orientax S y entra dentro del marco
            if 'O' in tablero_maq[fila_ini:fila_ini+long:+1, colum_ini:colum_ini+1]:#comprobar si se cruza con otro barco
                
                i = False# sigue ejecutandose al haberse cruzado las posiciones con otro barco
            else:
                tablero_maq [fila_ini:fila_ini+long:+1, colum_ini:colum_ini+1] = 'O'
                i = True # Ya pinta el barco, en posiciones no ocupadas y para el bucle
                return tablero_maq # Pinta el barco en el tablero
                

        elif orientacion == 2 and (colum_ini + long) < 9:# orientax E y entra dentro del marco
            if 'O' in tablero_maq[fila_ini:fila_ini+1, colum_ini:colum_ini+long]:#comprobar si se cruza con otro barco
                
                i = False # sigue ejecutandose al haberse cruzado las posiciones con otro barco
            else:
                tablero_maq [fila_ini:fila_ini+1, colum_ini:colum_ini+long] = 'O'
                i = True # Ya pinta el barco, en posiciones no ocupadas y para el bucle
                return tablero_maq # Pinta el barco en el tablero
                
            
        elif orientacion == 3 and (colum_ini - long) >= 0:
            if 'O' in tablero_maq[fila_ini:fila_ini+1, colum_ini:colum_ini-long:-1]:
                
                i = False # sigue ejecutandose al haberse cruzado las posiciones con otro barco
            else:    
                tablero_maq [fila_ini:fila_ini+1, colum_ini:colum_ini-long:-1] = 'O'
                i = True# Ya pinta el barco, en posiciones no ocupadas y para el bucle
                return tablero_maq # Pinta el barco en el tablero
                          

def tablero_con_barcos_jug():#pinta todos los barcos del tablero del jugador
                             #inicialmente trayendolo
                             #del diccionario BARCOS del archivo VARIABLES
                             #pasandolos por el for y ejecutando la funcion 
                             #posicionar barco para el JUGADOR
    tablero_jug = np.full((10,10), " ")
    for i in BARCOS.values():
        posicionar_barco_jug(i,tablero_jug)
    
    return tablero_jug


def tablero_con_barcos_maq():#pinta todos los barcos del tablero del MAQUINA
                             #inicialmente trayendolo
                             #del diccionario BARCOS del archivo VARIABLES
                             #pasandolos por el for y ejecutando la funcion 
                             #posicionar barco para la MAQUINA
    tablero_maq = np.full((10,10), " ")
    for i in BARCOS.values():
        posicionar_barco_maq(i,tablero_maq)
    
    return tablero_maq


def check_disparo_maq(tablero_jug,casilla_maquina):#comprueba los disparos de la MAQUINA
                                              #en el tablero del jugador,AGUA o TOCADO  
        
    if tablero_jug[casilla_maquina] == ' ':  # comprueba si es agua, la casilla del disparo 
        print("Agua......glugluglu")         # ojo coordenadas casillas fuera del marco, no esta fuera pq he acotado el random
        tablero_jug[casilla_maquina] = "-"   # pinta en tablero jugador el simbolo de agua
        return print('TABLERO JUG donde TE HAN disparado \n',tablero_jug)   # y pinta el tablero jugador con el nuevo impacto(agua)
    
    else:
        print("Tocado, te han dado")         # si no es agua es tocado ya que no puede disparar fuera al haberse acotado el random
        tablero_jug[casilla_maquina] = "X"  #pinta en el tablero jugador el simbolo tocado
    return print('TABLERO JUG donde TE HAN disparado\n',tablero_jug) # y pinta el tablero jugador con el nuevo impacto(tocado)
    
def check_disparo_jug(tablero_maq,tablero_maq_barcos_ocultos,casilla):#comprueba los disparos del jugador(introducidos en casilla)
                                                                      # en el tablero maq, y pinta en el tablero maq barcos ocultos
    
    print('Mi disparo es en la casilla:  ',casilla) #Pinta donde he disparado
    if tablero_maq[casilla] == ' ':    #comprueba si es agua
        print("Agua...glu...glugluglu")     
        tablero_maq[casilla] = "-"      #señala en el tablero maquina el simbolo de agua
        tablero_maq_barcos_ocultos[casilla] = "-" #señala en el tablero maquina QUE NOS MUESTRA SIN BARCOS el simbolo de agua
        return print('TABLERO MAQUINA, donde has disparado\n',tablero_maq_barcos_ocultos)   
    
    else: # si no es agua es TOCADO, porque ya en el disparar comprobo si ya habia sido disparada
                 
        tablero_maq[casilla] = "X" # asigna el simbolo de TOCADO a la casilla disparada del tablero de la maquina
        tablero_maq_barcos_ocultos[casilla] = "X" #asigna el simbolo TOCADO donde se disparo en el tablero de barcos ocultos que es el q muestra
        print('BOOOOOOM :::Vuelve a disparar')
        
    return print('TABLERO MAQUINA, donde has disparado\n',tablero_maq_barcos_ocultos)#muestra tablero maq sin barcos con el impacto nuestro nuevo

def disparo_jugador(tablero_maq,tablero_maq_barcos_ocultos):#funcion de disparo jugador, requiere los tableros de la maq, con y sin barcos
    
    print('TU TURNO, abajo el tablero del contrincante')
    print(tablero_maq_barcos_ocultos) #muestra tablero con los impactos mios y sin barcos
    i = 0 # Ponia True y el if ponia q no se iba a ejecutar
    while i == 0: # se ejecute mientras no tengo un formato de entrada de casilla correcto o sea entero entre 0 y 9 para fila y columna
        fshotjug = (input('¿Fila donde quieres disparar?, introduce un numero entre 0 y 9: \t')).strip() #por si pongo espacios delante
        cshotjug = (input('¿Columna donde quieres disparar?, introduce un numero entre 0 y 9: \t')).strip()
        if  fshotjug.isdigit() and cshotjug.isdigit() and 0 <= int(fshotjug) <= 9 and 0 <= int(cshotjug) <= 9 : # comprueba si son digitos y son enteros de una cifra entre 0 y 9
            casilla = (int(fshotjug),int(cshotjug))
            i = 1 #cierra bucle de solicitud de casilla de disparo, dando formato como bueno
        else:
            print ('Formato incorrecto, inténtalo de nuevo') #formato incorrecto se vuelve a ejecutar, vuelve a pedir nuevos fila y columna
    
    if (tablero_maq[casilla] == 'X') | (tablero_maq[casilla] == '-'): #comprueba si la casilla disparo jugador ya habia sido utilizada anteriormente
        print('Casilla ya usada, intentalo de nuevo')
        return disparo_jugador(tablero_maq,tablero_maq_barcos_ocultos) # si es asi se vuelve a llamar a esta misma funcion para que pida nuevas coordenadas
    return casilla # todo bien devuelve casilla de disparo del jugador


def disparo_maq(tablero_jug): #funcion de disparo jugador, requiere el tablero del jugador
    # Obtiene fila y columna aleatoriamente
    fshotmaq = random.randint(0,9)
    cshotmaq = random.randint(0,9)
    
    casilla_maq = (fshotmaq,cshotmaq)
    # comprueba si ha disparado ya en esas casillas, 
    if (tablero_jug[casilla_maq] == 'X') | (tablero_jug[casilla_maq] == '-'):
         print ('he vuelto a repetir casilla aleatoria', casilla_maq)
         print('tengo q volver a ejecutar la funcion')
         return disparo_maq(tablero_jug) # vuelve a ejecutarse la funcion al haber disparado en casilla repetida
    print('Turno Contricante, su disparo es:',casilla_maq) # devuelve la casilla correcta donde la maquina dispara
    return casilla_maq