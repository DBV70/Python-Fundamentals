from math import ceil
number_of_people = int(input())
lift_capacity = int(input())

print(ceil(number_of_people / lift_capacity))