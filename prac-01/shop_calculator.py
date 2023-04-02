# loop as long item count is negative or 0
item_count = int(input('Number of items: '))
while item_count < 0:
    print('Invalid number of items!')
    item_count = int(input('Number of items: '))

total_price = 0
for item in range(item_count):
    price = float(input('Price of item: '))
    total_price += price
discount = 0
# If the total price is over $100, then a 10% discount is applied to
# that total before the amount is displayed on the screen.
if total_price > 100:
    discount = total_price * 0.10
# subtract the discount
total_price = total_price - discount

print(f'Total price for {item_count} is ${total_price:,.2f}')