S1 = int(input("please enter score 1(integer 0-10): ")) 
S2 = int(input("please enter score 2(integer 0-10): "))
S3 = int(input("please enter score 3(integer 0-10): "))
S4 = int(input("please enter score 4(integer 0-10): "))
S5 = int(input("please enter score 5(integer 0-10): "))
D = int(input("please enter difficulty level: "))
SF = ((S1 + S2 + S3 + S4 + S5) - min(S1, S2, S3, S4, S5) - max(S1, S2, S3, S4, S5)) * D
print("The final score is: ", SF)