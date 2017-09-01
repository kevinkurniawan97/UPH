money = float(input("What is the amount of US Dollars you wish to convert? "))
rate = float(input("What is the current exchange rate (1 $US Dollar equals what in the Foreign Currency)? "))
answer = money * rate
print ("The amount in the Foreign Currency is $%1.2f"%(answer))
