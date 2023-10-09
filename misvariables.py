BARCOS = {
    "barco_1_1": 1,
    "barco_1_2": 1,
    "barco_1_3": 1,
    "barco_1_4": 1,
    "barco_2_1": 2,
    "barco_2_2": 2,
    "barco_2_3": 2,
    "barco_3_1": 3,
    "barco_3_2": 3,
    "barco_4_1": 4,}

INTRO_INSTR = '''
     【ＪＵＥＧＯ　ＤＥ　ＬＯＳ　ＢＡＲＱＵＩＴＯＳ】 
      
      Se trata del juego Hundir la Flota

      Tendrás que ir introduciendo las casillas,
     donde disparar, segun el formato requerido,
      un entero entre 0 y 9, para las filas primero,
     y otro del mismo rango para las columna.
      
      Se irán mostrando tus disparos en un tablero
      vacio, con la incidencia de cada uno:
      '-':.......AGUA
      'X':.......TOCADO
      
      La máquina disparara aleatoriamente, y se mostraran
      igual que lo anterior, salvo que se mostraran
      los barcos también con una 'O', en cada posición,
      que ocupen.

      En ambos casos, si los disparos son sobre posiciones 
      ya impactadas, ya sea AGUA ó TOCADO, se pedirá,
      repetir disparos.

      Los barcos se introduciran aleatoriamente, para 
      cada contricante:
    - 1 portaaviones que suponen 4 vidas
    - 2 acorazados que suponen 3 vidas cada uno
    - 3 fragatas que suponen 2 vidas cada una
    - 4 submarinos que suponen 1 vida cada una.
      
      En total, 20 vidas cada contrincante, gana el 
      primero que deje a 0 las vidas del otro \n
    
      BUENA SUERTE MARINERO!!!!!'''