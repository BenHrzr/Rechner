import time
i=0
ergebnis = 0

zahl1 = int(input('Was ist die erste Zahl?'))
rechenart = str(input('Welche Rechenart?'))
zahl2 = int(input('Was ist die zweite Zahl?'))
#zahl3 = int(input('Was ist die dritte Zahl'))

while i<= 10:

    if rechenart == '+':
        ergebnis = zahl1+zahl2
            #{zahl1} {rechenart} {zahl1) == {zahl1+zahl2}  <--- (ALTERNATIVE)
    elif rechenart == '-':
        ergebnis = zahl1-zahl2
    elif (rechenart == ':' or rechenart == '/'):
        ergebnis = zahl1/zahl2
    elif (rechenart == 'x' or rechenart =='*'):
        ergebnis = zahl1*zahl2
    else print('REchenfehler!')

    print(f'{ergebnis}')
    time.sleep(1.3)




# To do:
#nur zahlen angeben können
#neue rechnung?
#3, oder mehr zahlen
