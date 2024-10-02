def calculateCelsius(degree):
    print("Celsius temperature :: ", (degree - 32 ) * 5/9)

degree = float(input("Temperature in Fahrenheit: "))
calculateCelsius(degree)