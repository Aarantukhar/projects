#task 1
#define variable
i = 1
#iteration to print up to 10 on seperate lines
for i in range (1,11):
    print(i)
    #increment i
    i = i + 1


#tasl 2
#define variable
i = 1
#iteration to print up to 10 on same lines
for i in range (1,11):
    print(i, end = ' ')
    #increment i
    i = i + 1

#task 3
#getting input from user
# new line to stop it from going on the same line as the output above
x = int(input("\nEnter a start number: "))
y = int(input("Enter a stop number : "))
#add 1 to it
z = y + 1
#prevent error

if y > x :
    print("Unacceptable")

#iteration to print 
for x in range (x,z):
    print(x)
    #increment x by 1
    x = x + 1

#task 4
'''for loop that only prints out numbers between 1 and 1000, that are divisible by
3 and 17'''
for y in range(1,1001):
    #checks if the remainder is 0
    if y % 3 != 0:
        print("")
    #checks if the remainder is 0
    elif y % 17 != 0:
        print("")
    else:
        print(y)
        y = y + 1


#task 5
#defining password
password = "password"
#making a variable, assigning its value as essentially nothing for now
guess = ""
#setting the start value for i
i = 0
#allows user to guess password 10 times unless it is correct
while password != guess and i < 10:
    if i == 9:
        print("This is your last password attempt")
    else:
        pass
    #increment i
    i = i + 1
    #allows user to guess again
    guess = input("What is the password? : ")

#output selection
if guess == password:
    print("Password is correct")
elif i == 10 and guess != password:
    print("You do not have anymore attempts")


#task 6
#get the user's full name
full_name = input("Enter your full name: ")

#convert the input to uppercase
full_name_upper = full_name.upper()

#empty string
name_without_vowels = ""

#going through each character
for char in full_name_upper:
    #check if characters are vowels
    if char not in "AEIOU":
        #adding the characters that arent vowels to the empty string  
        name_without_vowels = name_without_vowels + char

#output
print("Your name without vowels: " + name_without_vowels)

