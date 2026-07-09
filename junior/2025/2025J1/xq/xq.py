n = int(input("Your place in line: "))
c = int(input("Number of car the train has: "))
p = int(input("Number of people a single car holdes: "))

if n <= c * p:
    print("yes")
else:
    print("no")