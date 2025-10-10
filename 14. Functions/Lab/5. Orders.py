def calculate_price(article, qty: int):
    prices = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00,
    }
    return prices[article] * qty

article = input()
qty = int(input())
price = calculate_price(article, qty)
print(f'{price:.2f}')