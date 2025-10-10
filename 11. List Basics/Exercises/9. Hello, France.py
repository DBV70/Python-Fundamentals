items_list = list(input().split('|'))
budget = float(input())

max_prices = {
    "Clothes": 50.0,
    "Shoes": 35.00,
    "Accessories": 20.50
}
purchased_items = []
total_expenses = 0.0
total_sales = 0.0

for item in items_list:
    type_and_price = item.split('->')
    item_type, item_price = type_and_price
    item_price = float(item_price)
    if item_price <= max_prices.get(item_type, []) and item_price <= budget:
        purchased_items.append(item_price * 1.4)
        budget -= item_price
        total_expenses += item_price
        total_sales += item_price * 1.4

profit = total_expenses * 0.4
for item in purchased_items:
    print(f"{item:.2f}", end=" ")
print()
print(f'Profit: {profit:.2f}')
if budget + total_sales >= 150.0:
    print("Hello, France!")
else:
    print("Not enough money.")
