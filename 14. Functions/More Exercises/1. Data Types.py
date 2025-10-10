def data_types(func, num):
    if func == "int":
        return f"{int(num) * 2}"
    elif func == "real":
        return f"{float(num) * 1.5:.2f}"
    elif func == "string":
        return f"${num}$"

input_func = input()
input_num = input()
print(data_types(input_func, input_num))
