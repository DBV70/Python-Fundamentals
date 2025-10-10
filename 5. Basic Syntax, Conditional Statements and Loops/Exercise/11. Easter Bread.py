budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price

loaf_price = flour_price + eggs_price + milk_price * 0.25
loaves = int(budget // loaf_price)
colored_eggs = 0

for i in range(1, loaves +1):
    colored_eggs += 3
    if i % 3 == 0:
        colored_eggs -= i - 2

money_left = budget - loaves * loaf_price
print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')