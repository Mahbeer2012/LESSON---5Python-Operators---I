# take marks as input form user
print("Enter marks Obtained in 4 Subjects : ")
computer = int(input("computer :"))
science = int(input("science"))
english = int(input("english :"))
geography = int(input("geography :"))

#Lets calculate the percentage of marks
sum = computer+science+english+geography
print("sum of computer,science,english,geography ")

percentage = (sum/400)*100

print(end="percentage marks = ")
print(percentage)
