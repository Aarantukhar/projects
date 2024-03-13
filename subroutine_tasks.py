'''
#task 1
string = input("Enter anything: ")

#subroutine
def reverser(x):
    #placeholder
    reverse = ""
    word = x
    #for loop to add the last character of the string to the placeholder
    for i in range (0,len(word)):
        reverse = word[i] + reverse
    #output
    print(reverse)

#calling subroutine
reverser(string)




#task 2

#subroutine
def grade(x,y,z):
    #total
    total = x + y + z
    #selection
    if total >= 80 and total <= 100:
        print("Grade A")
    if total >= 70 and total <= 79:
        print("Grade B")
    if total >= 60 and total <= 69:
        print("Grade C")
    if total >=50 and total <= 59:
        print("Grade D")
    if total >= 60 and total <= 69:
        print("Grade E")
    if total >= 0 and total <= 39:
        print("Grade U")

#getting score input
score_1 = int(input("What was the first exam score? : "))
score_2 = int(input("What was the second exam score? : "))
score_3 = int(input("What was the third exam score? : "))

#calling subroutine, inputting these into it
grade(score_1,score_2,score_3)

#importing math library
import math

#defining subroutine
def triangle_area(x):
    #able to square root
    area = (math.sqrt(3)/4)*(x**2)
    #output
    print(area)

#getting input
side_length= int(input("What is the length of the side of your equilateral triangle?: "))
#calling subroutine
triangle_area(side_length)

#square area
def square_area(x):
    area = x*x
    print(area)
square_length= int(input("What is the length of the side of your square? : "))

square_area(square_length)

#finding largest number
def largest(x,y,z):
    if x >= y and x >= z:
        print(str(x)+ " is the largest")
    if y >= x and y >= z:
        print(str(y) + " is the largest")
    if z >= x and z >= y:
        print(str(z) + " is the largest")
    else:
        print("Error")



#getting input
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

#calling subroutine
big = largest(num1,num2,num3)
#output
print(big)

#subroutine
def absolute(value):
    if value <0:
        print(value * -1) 
    print(value)

#getting input
num_4 = int(input("Enter a number: "))

#output
print(absolute(num_4))

#task 7
#getting a power
def biggest_power(n):
    power = 0
    while 2 ** power <=n:
        power = power + 1
    power = power -1
    print(2 ** power)

num_5 = int(input("Enter a number: "))
print(biggest_power(num_5))



#task 8

def prime(n):
    if n < 2:
        for i in range (2, n-1):
            if n % i == 0:
                return False
    return True

num_6 = int(input("Enter a number: "))

print(prime(num_6))'''







