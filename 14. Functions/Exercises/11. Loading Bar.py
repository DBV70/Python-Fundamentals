def loading_bar(number: int):
    load = number // 10
    bar = ['.' for _ in range(10)]
    for i in range(load):
        bar[i] = '%'
    if number == 100:
        print("100% Complete!")
        print(f"[{''.join(bar)}]")
    else:
        print(f"{number}% [{''.join(bar)}]")
        print("Still loading...")

input_number = int(input())
loading_bar(input_number)
