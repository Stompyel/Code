import time
import math

x = 1
#utskrift av alla tal mellan 1 och 10
while x <= 10:
    print(x)
    x = x + 1
    
#Utskrift av jämna tal
k = 2
while k < 10:
    print(k)
    k = k + 2
    if k % 2 == 0: 
        print(k)
    
#Beräkning av summan 1 + 2 + 3 + ..+n
while True:
    n = int(input('n?, skriv ett tal mindre än eller lika med 0 för att avsluta:'))
    start = time.time()
    if n <= 0:
        break
    summa = 0
    k = 1
    while k <= n:
        summa = summa + k
        k = k + 1
    slut = time.time()
    print ('summan blir', summa,'. det tog', round(slut - start), 'sekunder att räkna ut.')