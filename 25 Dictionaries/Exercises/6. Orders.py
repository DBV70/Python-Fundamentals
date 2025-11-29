products = {}

while True:
    command = input()
    if command == "buy":
        break
    product, price, quantity = command.split()
    if product not in products:
        products[product] = [float(price), int(quantity)]
    else:
        products[product][0] = float(price)
        products[product][1] += int(quantity)

for product, price_quantity in products.items():
    price = price_quantity[0]
    quantity = price_quantity[1]
    print(f"{product} -> {price * quantity:.2f}")
