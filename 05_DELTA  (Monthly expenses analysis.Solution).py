#DELTA_05
#Analysis of monthly expenses from all types of bills.
#Tech stack - PYTHON (3.9.7)

User_Budget = float(input("Please Enter the Budget for a month: \n"))

Total_Month_Expense = 0

Bills_Amount = {}

Bills = int(input("How many bills do you have to add to your Expenses? \n"))

#syntax for Bill name and Bill amount.

for x in range(Bills):
    Name = input("Enter Bill Name : ")#Bill name refers to e.g. Groceries,Essential & non-Essential and many more.
    User_Expense = float(input("Enter an Bill Amount: \n")) #Bill amount should be an numeric value.
    Bills_Amount.update({Name : User_Expense})
    Total_Month_Expense = Total_Month_Expense + User_Expense
    
#Condition statement for total expenses.
    
if Total_Month_Expense > User_Budget:
	print("You Were Over Your Budget of", User_Budget,"by",Total_Month_Expense - User_Budget) #condition for surplus expenditure
elif User_Budget > Total_Month_Expense:
    print("You Were Under Your Budget of", User_Budget,"by",User_Budget - Total_Month_Expense)#condition for deficit expenditure
elif User_Budget == Total_Month_Expense:
    print("You Used Exactly Your Budget of", User_Budget,".")#condition for moderate expenditure

print("The Bills : ", Bills_Amount)
print("Total Budget : ", User_Budget)
print("Total Expenses : ", Total_Month_Expense)
