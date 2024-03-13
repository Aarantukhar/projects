#getting an integer input from user
num = int(input("Enter a number : " ))

#example of selection
#checks if number is below 100 hundred
if num <= 100 and num >= 0 :
    print("number in range")

else:
    print("not in range")



#gets input from user
password = input("Enter password: ")
#length of password
password_length = len(password)

#selection to see if it is between 8 and 15 characters
#has to be above 8 characters
if password_length < 8:
    print("Password to short")
#cannot be 15 characters or more
if password_length >= 15:
    print("Password too long")

elif password_length < 8 and <= 15:
    print("Password accepted")



#defining constant
answer = 3
#defining variable
solved = False
#getting guess from user
guess = int(input("Guess a number : "))


#selection statements to decide if guess was right
if guess == answer:
    solved == True

if solved == True:
    print("You guessed correct")

else:
    print("Answer was incorrect")



#getting user input
age = int(input("Enter your age (expected range 11 - 21): "))


if age >= 11 and age < 16 :
    print("High School")

if age >= 16 and age < 18:
    print("Sixth Form")

if age >= 18 and age < 21:
    print("University")

else:
    print("Value out of range")
    



