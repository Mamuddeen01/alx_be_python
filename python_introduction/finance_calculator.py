M_I = int(input("Enter your monthly income:"))
T_M_I = int(input("Enter your total monthly expenses"))
savings = M_I - T_M_I
P_Sav = savings * 12 + (savings * 12 * 0.05)
print("Your monthly savings are $", savings)
print("Projected savings after one year, with interest is $", P_Sav)
