amount= (int(input("Enter your amount: ")))

note_100=(amount//100)
note_50=((amount%100)//50)
note_10=((amount%50)//10)
print("Number of 100 notes is:", note_100)
print("Number of 50 notes is:", note_50)
print("Number of 10 notes is:", note_10)
