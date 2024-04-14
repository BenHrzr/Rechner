import time
i=0


while i<= 10:
    try: 

        ergebnis = 'Fehlerhafte Eingabe'

        zahl1 = int(input("Was ist die erste Zahl?"))
        rechenart = str(input('Welche Rechenart?'))
        zahl2 = int(input("Was ist die zweite Zahl?"))

        

        if rechenart == '+':
            ergebnis = zahl1+zahl2
                #{zahl1} {rechenart} {zahl1) == {zahl1+zahl2}  <--- (ALTERNATIVE)
        elif rechenart == '-':
            ergebnis = zahl1-zahl2
        elif (rechenart == ':' or rechenart == '/'):
            ergebnis = zahl1/zahl2
        elif (rechenart == 'x' or rechenart =='*'):
            ergebnis = zahl1*zahl2
            
        print(ergebnis)
        
    except ValueError: 
        print('Fehlerhafte Eingabe. Bitte stellen Sie sicher, dass Sie nur Zahlen eingeben.')
    
    time.sleep(1.3)


