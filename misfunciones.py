import numpy as np
from misvariables import BARCOS

tablero_jug = np.full((10,10), " ")
tablero_maq = np.full((10,10), " ")
tablero_maq_barcos_ocultos = np.full((10,10), " ")

def posicionar_barco_jug (long,tablero_jug):#generar posiciones de un barco

    import random
    i = False
    while i == False:
        fila_ini = random.randint(0,9)
        colum_ini = random.randint(0,9)
        orientacion = random.randint(0,3) # 0=N, 1=S, 2=E Y 3=O
        #print(fila_ini)
        #print(colum_ini)
        #print(orientacion)
        if orientacion == 0 and (fila_ini - long) >= 0:
            # for i in tablero[fila_ini:fila_ini-long:-1]:
                # print (i)
            if 'O' in tablero_jug[fila_ini:fila_ini-long:-1, colum_ini:colum_ini+1]:
                #print('Barco en la ubicación, pedir nueva ubicación')
                i = False
            else:
                tablero_jug[fila_ini:fila_ini-long:-1, colum_ini:colum_ini+1] = 'O'
                i= True 
                return tablero_jug
                
        elif orientacion == 1 and (fila_ini + long) < 9:
            if 'O' in tablero_jug[fila_ini:fila_ini+long:+1, colum_ini:colum_ini+1]:
                #print('Barco en la ubicación, pedir nueva ubicación')
                i = False
            else:
                tablero_jug [fila_ini:fila_ini+long:+1, colum_ini:colum_ini+1] = 'O'
                i = True
                return tablero_jug
                

        elif orientacion == 2 and (colum_ini + long) < 9:
            if 'O' in tablero_jug[fila_ini:fila_ini+1, colum_ini:colum_ini+long]:
                #print('Barco en la ubicación, pedir nueva ubicación')
                i = False 
            else:
                tablero_jug [fila_ini:fila_ini+1, colum_ini:colum_ini+long] = 'O'
                i = True
                return tablero_jug
                
            
        elif orientacion == 3 and (colum_ini - long) >= 0:
            if 'O' in tablero_jug[fila_ini:fila_ini+1, colum_ini:colum_ini-long:-1]:
                #print('Barco en la ubicación, pedir nueva ubicación')
                i = False 
            else:    
                tablero_jug [fila_ini:fila_ini+1, colum_ini:colum_ini-long:-1] = 'O'
                i = True
                return tablero_jug
                
        else:
            i = False
            #print('Barco se sale del marco, pedir nueva ubicación')


def posicionar_barco_maq(long,tablero_maq):#generar posiciones de un barco

    import random
    i = False
    while i == False:
        fila_ini = random.randint(0,9)
        colum_ini = random.randint(0,9)
        orientacion = random.randint(0,3) # 0=N, 1=S, 2=E Y 3=O
        #print(fila_ini)
        #print(colum_ini)
        #print(orientacion)
        if orientacion == 0 and (fila_ini - long) >= 0:
            # for i in tablero[fila_ini:fila_ini-long:-1]:
                # print (i)
            if 'O' in tablero_maq[fila_ini:fila_ini-long:-1, colum_ini:colum_ini+1]:
                #print('Barco en la ubicación, pedir nueva ubicación')
                i = False
            else:
                tablero_maq[fila_ini:fila_ini-long:-1, colum_ini:colum_ini+1] = 'O'
                i= True 
                return tablero_maq
                
        elif orientacion == 1 and (fila_ini + long) < 9:
            if 'O' in tablero_maq[fila_ini:fila_ini+long:+1, colum_ini:colum_ini+1]:
                #print('Barco en la ubicación, pedir nueva ubicación')
                i = False
            else:
                tablero_maq [fila_ini:fila_ini+long:+1, colum_ini:colum_ini+1] = 'O'
                i = True
                return tablero_maq
                

        elif orientacion == 2 and (colum_ini + long) < 9:
            if 'O' in tablero_maq[fila_ini:fila_ini+1, colum_ini:colum_ini+long]:
                #print('Barco en la ubicación, pedir nueva ubicación')
                i = False 
            else:
                tablero_maq [fila_ini:fila_ini+1, colum_ini:colum_ini+long] = 'O'
                i = True
                return tablero_maq
                
            
        elif orientacion == 3 and (colum_ini - long) >= 0:
            if 'O' in tablero_maq[fila_ini:fila_ini+1, colum_ini:colum_ini-long:-1]:
                #print('Barco en la ubicación, pedir nueva ubicación')
                i = False 
            else:    
                tablero_maq [fila_ini:fila_ini+1, colum_ini:colum_ini-long:-1] = 'O'
                i = True
                return tablero_maq
                
        else:
            i = False
            #print('Barco se sale del marco, pedir nueva ubicación')

def tablero_con_barcos_jug():
    for i in BARCOS.values():
        posicionar_barco_jug(i,tablero_jug)
    # print('Mi tablero \n',tablero_jug)
    return tablero_jug
def tablero_con_barcos_maq():
    for i in BARCOS.values():
        posicionar_barco_maq(i,tablero_maq)
    # print('Tablero Maq \n',tablero_maq_barcos_ocultos)
    return tablero_maq


def disparar_maq(casilla_maquina):
    import random
    # fshotmaq = random.randint(0,9)
    # cshotmaq = random.randint(0,9)
    # #orientacion = random.randint(0,3) # 0=N, 1=S, 2=E Y 3=O
    # casilla = (fshotmaq,cshotmaq)
    # print(casilla)

    if tablero_jug[casilla_maquina] == ' ':
        print("Agua......glugluglu")         # ojo coordenadas casillas fuera del marco, no esta fuera pq he acotado el random
        tablero_jug[casilla_maquina] = "-"
        return print('TABLERO JUG \n',tablero_jug)   
    # elif (tablero_jug[casilla_maquina] == 'X') | (tablero_jug[casilla_maquina] == '-'):
    #      print('tengo q volver a ejecutar la funcion')#tiene q tirar otra vez, por repeticion, lo hare con un while para que vuelva
    #      return disparar_maq()
    else:
        print("Tocado, te han dado")         # ojo coordenadas repetidas ya disparadas, ya tenido en cuenta en el tablero[casilla] == 'X' or '-'
        tablero_jug[casilla_maquina] = "X"
    return print('TABLERO JUG \n',tablero_jug) # disparar_maq()
    
def disparar_jug(casilla):#no es disparar es comprobar
    # coordenadas = input('¿Donde quieres disparar? (Formato:1.7)')
    # fshotjug = int(coordenadas[0])
    # cshotjug = int(coordenadas[2])
    # casilla = (fshotjug,cshotjug)
    print(casilla)
    if tablero_maq[casilla] == ' ':
        print("Agua...glu...glugluglu")         # ojo coordenadas casillas fuera del marco, no esta fuera pq he acotado el random
        tablero_maq[casilla] = "-"
        tablero_maq_barcos_ocultos[casilla] = "-"
        return print('TABLERO MAQUINA\n',tablero_maq_barcos_ocultos)   
    # elif (tablero_maq[casilla] == 'X') | (tablero_maq[casilla] == '-'):
    #      print('ha disparado a una casilla ya usada, repetir disparo')#tiene q tirar otra vez, por repeticion, lo hare con un while para que vuelva
    #      return disparo_jugador()
    else:
                 # ojo coordenadas repetidas ya disparadas, ya tenido en cuenta en el tablero[casilla] == 'X' or '-'
        tablero_maq[casilla] = "X"
        tablero_maq_barcos_ocultos[casilla] = "X"
        y = 'BOOOOOOM :::Vuelve a disparar'
        print(y)
    return print('TABLERO MAQUINA\n',tablero_maq_barcos_ocultos)#, disparar_jug()

def disparo_jugador():
    # try:
    #     coordenadas = input('¿Donde quieres disparar? (Formato:1.7)')
    # except (ValueError, IndexError):
    #     print ('Formato incorrecto, inténtalo de nuevo')
    print('TU TURNO, abajo el tablero del contrincante')
    print(tablero_maq_barcos_ocultos)
    i = 0 # Ponia True y el if ponia q no se iba a ejecutar
    while i == 0:
        fshotjug = (input('¿Fila donde quieres disparar?, introduce un numero entre 0 y 9: \t')).strip() #por si pongo espacios delante
        cshotjug = (input('¿Columna donde quieres disparar?, introduce un numero entre 0 y 9: \t')).strip()
        if  fshotjug.isdigit() and cshotjug.isdigit() and 0 <= int(fshotjug) <= 9 and 0 <= int(cshotjug) <= 9 : 
            casilla = (int(fshotjug),int(cshotjug))
            i = 1
        else:
            print ('Formato incorrecto, inténtalo de nuevo')
    
    if (tablero_maq[casilla] == 'X') | (tablero_maq[casilla] == '-'):
        print('Casilla ya usada, intentalo de nuevo')
        return disparo_jugador()
    return casilla


def disparo_maq():
    import random
    fshotmaq = random.randint(0,9)
    cshotmaq = random.randint(0,9)
    #orientacion = random.randint(0,3) # 0=N, 1=S, 2=E Y 3=O
    casilla_maq = (fshotmaq,cshotmaq)
    if (tablero_jug[casilla_maq] == 'X') | (tablero_jug[casilla_maq] == '-'):
         print ('he vuelto a repetir casilla aleatoria', casilla_maq)
         print('tengo q volver a ejecutar la funcion')#tiene q tirar otra vez, por repeticion, lo hare con un while para que vuelva
         return disparo_maq()
    print(casilla_maq)
    return casilla_maq