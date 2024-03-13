'''#opening for writing 
file_1 = open("pupils.txt", "w")

#adding names to name
for i in range(5):
    name = input("Enter name")
    file_1.write("\n" + name)

#opening for reading
file_1 = open("pupils.txt", "r")
file_2 = file_1.read()
#output
print(file_2)
file_1.close()'''
    


username = input("Enter username").upper()

leave = ""
first_check = ""
second_check = ""
correct = ""
while leave != "Q":
    while len(username)!= 6:
        username = input("Enter username: ").upper()

    while correct != "Y":
        correct == "N"
        for i in range(0,2):
            if ord(username[i]) >= 65 and ord(username[i]) <= 90:
                first_check = "Y"
                
        for i in range(2,6):
            if ord(username[i]) >= 48 and ord(username[i]) <= 57:
                second_check = "Y"
                

        if first_check == "Y" and second_check == "Y":
            print(username)
            leave = input("Username Valid, do you want to quit? Use Q: ")
            if leave != "Q":
                username = input("Enter username: ").upper()
                correct = "N"
                
            elif leave == "Q":
                correct = "Y"
                exit

        
        correct == "N"
        username = input("Enter username")
            
