def calculateVolume(diameter, height):
    print("Volume of Cylinder :: ", 3.14*((diameter*diameter)/4)*height)

diameter = float(input("Enter the diameter of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

calculateVolume(diameter, height)