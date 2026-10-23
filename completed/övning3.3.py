poäng=int(input("Hur många poäng fick eleven?"))
if poäng < 25:
    print("F")
elif poäng >= 25 and poäng < 30:
    print("E")
elif poäng >= 30 and poäng < 35:
    print("D")
elif poäng >= 35 and poäng < 40:
    print("C")
elif poäng >= 40 and poäng < 45:
    print("B")
elif poäng >= 45 and poäng <= 50:
    print("A")