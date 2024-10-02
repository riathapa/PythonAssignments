def calculateTotalAmount(principal, months, rateOfInterest):
    totalAmount = principal*((1+(rateOfInterest/100))**(months/12))
    print("TotalAmount :: ", totalAmount)

principal = int(input("Enter the principal: "))
rateOfInterest = int(input("Enter the rate of interest: "))
months = int(input("Enter the number of months: "))

calculateTotalAmount(principal, months, rateOfInterest)