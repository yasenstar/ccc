B = int(input("please enter # tickets Besa wants to buy: "))
T = int(input("please enter total # tickets for the concert: "))
P = int(input("please enter # tickets other people have purchased: "))
if P > T:
    print("Error: The number of tickets purchased by others cannot exceed the total number of tickets.")
elif B > (T - P):
    print("N")
else:
    print("Y", T-P-B)

