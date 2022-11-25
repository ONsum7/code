#W2T4 Monthly earnings
print("Sales Report")
print("")

Year = int(input("Enter the year "))
print("")

JanuaryS = int(input("Enter January's sales amount "))
FeburaryS = int(input("Enter Feburary's sales amount "))
MarchS = int(input("Enter March's sales amount "))
AprilS = int(input("Enter April's sales amount "))
MayS = int(input("Enter May's sales amount "))
JuneS = int(input("Enter June's sales amount "))
JulyS = int(input("Enter July's sales amount "))
AugustS = int(input("Enter August's sales amount "))
SeptemberS = int(input("Enter September's sales amount "))
OctoberS = int(input("Enter October's sales amount "))
NovemberS = int(input("Enter November's sales amount "))
DecemberS = int(input("Enter December's sales amount "))
print("")

TotalS = JanuaryS + FeburaryS + MarchS + AprilS+ MayS + JuneS + JulyS + AugustS + SeptemberS + OctoberS + NovemberS + DecemberS
print("total sales for", Year, "are",TotalS)
AverageS = TotalS/12
print("The average monthly sales for", Year, "was", AverageS)

