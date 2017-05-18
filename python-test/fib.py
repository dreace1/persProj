#Die Summe der letzten beiden Elemente ergibt das naechste
a = 0
b = 1
while b < 10:
    print(b)
    a, b = b, a+b
