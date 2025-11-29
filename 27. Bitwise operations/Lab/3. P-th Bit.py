n = int(input())
p = int(input())

bitAtPositionP = (n >> p) & 1
print(bitAtPositionP)
