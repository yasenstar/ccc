B = int(input("Please input number of tickets Besa wants to buy (positive integer): "))
T = int(input("Please input the total number of tickets for the concert (positive integer): "))
P = int(input("Please input the number of ticket other people have purchaseed (positive integer, less than total): "))

remain = T - P - B

if remain > 0:
    print(f"Y {remain}")
else:
    print("N")