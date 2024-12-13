#asking the user for input
income = int(input("Enter your monthly income: "))
expenses = int(input ( "Enetr your total monthly expenses: "))
interest = 0.05

#calculations
savings = income - expenses
Projected_Savings = int(savings * 12 + (savings * 12 * 0.05))

print (f"Your monthly savings are ${savings}")
print (f"Projected savings after one year, with interest, is: {Projected_Savings}.")