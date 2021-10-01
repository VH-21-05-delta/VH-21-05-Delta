#TEAM_DELTA_05
#Monthly expenses analysis from all types of bills.
User_Budget = float(input("Please Enter the Budget" + \
                    "for a month: \n"))

More_Expense = "y"
Total_Month_Expense = 0

while More_Expense == "y":
    User_Expense = float(input("Enter an Expense: \n"))
    Total_Month_Expense =+ User_Expense
    More_Expense = input("Do you have more Expense? Type 'y' for Yes," + \
                        "Any other key for No: \n")

if Total_Month_Expense > User_Budget:
	print("You were over your budget of",User_Budget,"by",Total_Month_Expense - User_Budget)
elif User_Budget > Total_Month_Expense:
    print("You were under your budget of",User_Budget,"by",User_Budget - Total_Month_Expense)
else:
    print("You used exactly your budget of",User_Budget,".")
