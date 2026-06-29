#R>G G>B B>R
# def compare(a, b):
#     if a == b:
#         return 0
#     elif (a == 'R' > b == 'G'):
#         return 1
#     elif (a == 'G' > b == 'B'):
#         return 2
#     elif (a == 'B' > b == 'R'):
#         return 3
a = input("input candy line 1: ")
b = input("input candy line 2: ")

result = compare(a, b)
print(result)