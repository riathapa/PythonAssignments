def computeMonthlyPayment(amt, rate, months):
    term1 = (1 + (rate/1200))**months
    numerator = rate*term1
    denominator = (1200*term1)-1
    finalTerm =  numerator/denominator
    monthlyPayment = finalTerm*amt
    print("Monthly Payment :: ", monthlyPayment)

amt = float(input("Enter amount :: "))
rate = float(input("Rate :: "))
months = float(input("Enter months :: "))
computeMonthlyPayment(amt, rate, months)