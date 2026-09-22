import math
radius = float(input("ange radie"))

volume = (4/3) * math.pi * radius**3
surface_area = 4 * math.pi * radius**2

print (f"volymen är: {volume:.2f}") 
print (f"ytan är: {surface_area:.2f}")