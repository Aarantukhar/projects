#get user input
num = int(input("Enter a number: "))

#check num in range

if num <= 100:
    print("Number is in range")

#task 5

#get user input
num = int(input("Enter a number: "))

#check num in range

if num > 0 and num <= 100:
    print("Number is in range")

#task 6
password = input("Enter password: ")

#test for valid length
if len(password) < 8:
    print("Password too short")

elif len(password) >= 15:
    print("password too long")

else:
    print("password accepted")

#task 7

answer = 3
solved = False

#get user guess
guess = int(input("Enter your guess : "))

#selection to test for correct input
if guess == answer:
    solved == True
    print("Answer is correct")
else:
    print("Answer is incorrect")




#getting user input
age = int(input("Enter your age (expected range 11 - 21): "))
#output selection

if age < 11: 
    print("Out of range")
if age > 21:
    print("Out of range")

if age >= 18: 
    print("University ")

if age >= 16:
    print("Sixth Form")

else:
    print("High school")



