#Taking total amount as input from user
Amount =int(input("please Enter Amount for withdraw :"))

# Calculatingthe number of notes diffrent denominators
note_1 = Amount//50
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print(" notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)
