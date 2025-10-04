print("Average percentage of marks:")
Maths=int(input("Enter your math marks:"))
Physics=int(input("Enter your physics marks:"))
Chemistry=int(input("Enter your chemistry marks:"))
English=int(input("Enter your english marks:"))
Biology=int(input("Enter your biology marks:"))

sum=Maths+Physics+Chemistry+English+Biology
percentage=(sum/500)*100

print("The average percentage is:", percentage, "%")
