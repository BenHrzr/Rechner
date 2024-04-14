import time
import tkinter as tk

max_run = 10            #DIESE VARIABLE FÜR DIE ANZAHL DER DURCHLÄUFE ÄNDERN (AKTUELL 10)
runs = 0


while runs < max_run:
    try: 

        ergebnis = 'Fehlerhafte Eingabe. Nur gültige Rechensymbole verwenden!'

        zahl1 = int(input("Was ist die erste Zahl?"))
        rechenart = str(input('Welche Rechenart?'))
        zahl2 = int(input("Was ist die zweite Zahl?"))

        

        if rechenart == '+':
            ergebnis = zahl1+zahl2
        elif rechenart == '-':
            ergebnis = zahl1-zahl2
        elif (rechenart == ':' or rechenart == '/'):
            ergebnis = zahl1/zahl2
        elif (rechenart == 'x' or rechenart =='*'):
            ergebnis = zahl1*zahl2
            
        print(ergebnis)
        
    except ValueError: 
        print('Fehlerhafte Eingabe. Bitte stellen Sie sicher, dass Sie nur Zahlen eingeben.')
    
    runs +=1
    time.sleep(1.3)


