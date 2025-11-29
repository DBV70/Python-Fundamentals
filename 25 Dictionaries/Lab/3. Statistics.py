products = {}

while True:
    command = input()
    if command == "statistics":
        break
    product, quantity = command.split(": ")
    if product not in products:
        products[product] = int(quantity)
    else:
        products[product] += int(quantity)

product_count = len(products)
total_quantity = sum(products.values())

print(f"Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {product_count}")
print(f"Total Quantity: {total_quantity}")