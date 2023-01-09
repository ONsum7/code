#W3T5
print("Account Interest Calculator")
print("---------------------------")
print()

#shortened variable names
StartBal = float(input("Please enter the starting balance> £"))
FinalBal = float(input("Please enter the final balance> £"))
IntRate = float(input("Please enter the interest rate> "))

CurrentBal = StartBal
month = 1

print("Month\tBalance (£)")

#added monthly counter
#divided IntRate by 100 to get percentage
#InterestBal to find interest each month to add to CurrentBal
while CurrentBal < FinalBal:
    
    InterestBal = (CurrentBal * (IntRate/100))
    CurrentBal = InterestBal + CurrentBal
    
    print(str(month) + "\t" + "{:.2f}".format(CurrentBal))
    month = month + 1    
        
print()
#month-1 to show how long it'll take not which month result will occur
print("It will take " + str(month-1) + " months to achieve the balance £" + "{:.2f}".format(FinalBal))
