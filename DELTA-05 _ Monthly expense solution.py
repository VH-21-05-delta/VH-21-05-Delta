User_Budget = float(input("Please Enter the Budget" + \
                    "for a month: \n"))

Total_Month_Expense = 0

Bills_Amount = {}

Bills = int(input("How many bills do you have to add to your Expenses?? ( Enter a Number ): "))

for x in range(Bills):
    Name = input("Enter bill name (eg : shoppings, grocery, food, gaming etc): ")
    User_Expense = float(input("Enter an Bill Amount: \n"))
    Bills_Amount.update({Name : User_Expense})
    Total_Month_Expense = Total_Month_Expense + User_Expense

if Total_Month_Expense > User_Budget:
	print("You Were Over Your Budget Of", User_Budget,"By",Total_Month_Expense - User_Budget)
elif User_Budget > Total_Month_Expense:
    print("You Were Under Your Budget Of", User_Budget,"By",User_Budget - Total_Month_Expense)
elif User_Budget == Total_Month_Expense:
    print("You Used Exactly Your Budget Of", User_Budget,".")

print("The Bills = ", Bills_Amount)
print("Total Budget", User_Budget)
print("Total Expenses = ", Total_Month_Expense)
