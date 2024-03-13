#Aaran Tukhar

#simple print statements
print("Hello world")
print("  This is python")
print("We are learning\new\things")

#outputs sentence on multiple lines.
print("Hello World \n  This is python \nWe are learning\new\things")

#input from user
name = input("Enter your name: ")
#converts their input into integer
year = int(input("Enter your year of birth: "))
#adds 21 to the year of their birth
age = year + 21
#personalised statement, that utilises concatenation
print("Hi " + name + ", in the year " + str(age) + ", you will be 21 years old.")





#gets decimal number as input
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number : "))

#simple subtraction
#outputs
sub1 = num1 - num2
print("The answer to " + str(num1) + " - " + str(num2) + " = " + str(sub1))
sub2 = num2 - num1
print("The answer to " + str(num2) + " - " + str(num1) + " = " + str(sub2))

#simple division
#outputs
div = num1/num2
div2= num2/num1
print("The answer to " + str(num1) + " / " + str(num2)+ " = " + str(div))
print("The answer to " + str(num2) + " / " + str(num1)+ " = " + str(div2))

#multiplication
#output
mult = num1 * num2
print("The answer to " + str(num1) + " * " + str(num2)+ " = " + str(mult))

#add
#output
add = num1 + num2
print("The answer to " + str(num1) + " + " + str(num2)+ " = " + str(add))
