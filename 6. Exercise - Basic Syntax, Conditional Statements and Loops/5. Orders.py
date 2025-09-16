N = int(input())
total = 0.00

for i in range(N):
    price = float(input())
    days = int(input())
    capsules = int(input())

    if 0.01 > price or price > 100.00 or 1 > days or days > 31 or 1 > capsules or capsules > 2000:
        continue
    else:
        print(f'The price for the coffee is: ${(price * days * capsules):.2f}')
        total += price * days * capsules

print(f'Total: ${total:.2f}')
