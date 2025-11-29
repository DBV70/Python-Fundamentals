import re
pattern = r"%([A-Z][a-z]+)%[^%$.\|]*<(\w+)>[^%$.\|]*\|(\d+)\|[^%$.\|]*?([0-9]+(?:\.[0-9]+)?)\$"
total_income = 0.0

while True:
    line = input()
    if line == 'end of shift':
        break

    match = re.search(pattern, line)
    if match:
        customer, product, count, price = match.groups()
        total = float(count) * float(price)
        total_income += total
        print(f"{customer}: {product} - {total:.2f}")

print(f"Total income: {total_income:.2f}")
