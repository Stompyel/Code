def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

fah_input = float(input("enter temperature in fahrenheit:"))
celsius_output = fahrenheit_to_celsius(fah_input)
print (f"temperature in celsius is: {celsius_output:.2f}")
