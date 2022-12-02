#W2T4 Monthly earnings
print("Sales Report")
print("")

Year = int(input("Enter the year "))
print("")


JanuaryS = float(input("Enter January's sales amount £"))
FeburaryS = float(input("Enter Feburary's sales amount £"))
MarchS = float(input("Enter March's sales amount £"))
AprilS = float(input("Enter April's sales amount £"))
MayS = float(input("Enter May's sales amount £"))
JuneS = float(input("Enter June's sales amount £"))
JulyS = float(input("Enter July's sales amount £"))
AugustS = float(input("Enter August's sales amount £"))
SeptemberS = float(input("Enter September's sales amount £"))
OctoberS = float(input("Enter October's sales amount £"))
NovemberS = float(input("Enter November's sales amount £"))
DecemberS = float(input("Enter December's sales amount £"))
print("")

TotalS = JanuaryS + FeburaryS + MarchS + AprilS+ MayS + JuneS + JulyS + AugustS + SeptemberS + OctoberS + NovemberS + DecemberS
AverageS = TotalS/12
print("total sales for", Year, "are £","{:.2f}".format(TotalS))
print("The average monthly sales for", Year, "was £", "{:.2f}".format(AverageS))

