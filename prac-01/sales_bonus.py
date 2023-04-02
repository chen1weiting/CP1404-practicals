"""
get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.1
    else
        bonus = sales * 0.15
    display bonus
    get sales
"""
NUMBER_OF_SALES = 1000
BONUS_UNDER_1000 = 0.1
BONUS_ABOVE_1000 = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < NUMBER_OF_SALES:
        bonus = sales * BONUS_UNDER_1000
    else:
        bonus = sales * BONUS_ABOVE_1000
    print(f"Your bonus is {bonus}")
sales = float(input("Enter sales: $"))