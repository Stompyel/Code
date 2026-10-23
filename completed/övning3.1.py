antal_minuter=int(input("Hur många minuter ringer du varje månad?"))
if antal_minuter < 33:
    print("Välj abonnemang kontant")
elif antal_minuter > 66:
    print("Välj abonnemang normal")
else:
    print("Välj abonnemang plus")