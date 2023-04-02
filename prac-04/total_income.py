""" CP1404/CP5632 Practical Starter code for cumulative total income program """


def main():
    """Display income report for incomes over a given number of months."""
    # This list is to store incomes which are user enter.
    incomes = []
    # This variable stores the number of months entered by the user.
    numOfMonths = int(input("How many months? "))
    # Printing the blank line for good looking output.
    print('')
    # Loop from month=1 to month=numOfMonths
    for month in range(1, numOfMonths + 1):
        # This variable stores the income entered by the user.
        income = float(input(f"Enter income for month {month}: "))
        # Collecting user entered income into incomes list.
        incomes.append(income)
    # Calling the function to display the report.
    display_Report(numOfMonths, incomes)


def display_Report(monthsCount, incomesList):
    """This function will print the report in tabular format"""
    # Printing the title of the report
    print("\nIncome Report\n-------------")
    # This variable stores the cumulative income. Initially set to 0
    total = 0
    # Loop from month=1 to month=monthsCount
    for month in range(1, monthsCount + 1):
        # Getting income value that present at current month index in incomesList.
        income = incomesList[month - 1]
        # Adding the current income to the total cumulative income.
        total += income
        # Printing
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


# Calling the main function
main()