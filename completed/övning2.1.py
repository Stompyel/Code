mätarställning_idag=int(input("Mätarställningen idag?"))
mätarställning_1år=int(input("Mätarställning 1 år sedan?"))
körda_mil=mätarställning_idag-mätarställning_1år
print(körda_mil)
print("Antal körda mil?" , körda_mil , "mil")
liter_bensin=int(input("Liter bensin idag?"))
bensin_förbrukning=liter_bensin/körda_mil
print("bensin_förbrukning" , bensin_förbrukning)
