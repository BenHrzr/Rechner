import time
import tkinter as tk

max_run = 10            #DIESE VARIABLE FÜR DIE ANZAHL DER DURCHLÄUFE ÄNDERN (AKTUELL 10)
runs = 0


while runs < max_run:
    try: 

        ergebnis = 'Fehlerhafte Eingabe. Nur gültige Rechensymbole verwenden! [#0002]'
        

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
        
        time.sleep(0.4)

        ergebnis2 = 'Fehlerhafte Eingabe. Nur gültige Rechensymbole verwenden! [#0003]'

        abfrage = (input("Möchtest du eine dritte Zahl mit einrechnen ?"))
        rechenart2 = str(input('Welche Rechenart?'))
        zahl3 = int(input("Wie lauetet die dritte Zahl?"))

        if (abfrage == 'JA' or abfrage == 'Ja' or abfrage == 'ja'):
            if rechenart2 == '+':
                ergebnis2 = ergebnis + zahl3
            elif rechenart2 == '-':
                ergebnis2 = ergebnis-zahl3
            elif (rechenart2 == ':' or rechenart == '/'):
                ergebnis2 = ergebnis/zahl3
            elif (rechenart2 == 'x' or rechenart =='*'):
                 ergebnis2 = ergebnis*zahl3

            print(ergebnis2)         
        
    
    except ValueError: 
        print('Fehlerhafte Eingabe. Bitte stellen Sie sicher, dass Sie nur Zahlen eingeben. [#0001]')
   
   
    runs +=1
    time.sleep(1.3)


# To do:
#Beliebig viele Zahlen rechnen
