#open file
file_1 = open("poem_2.txt", "r")

#read the file
all_data = file_1.read()

#print what it has read
print(all_data)

#close file
file_1.close()

file_2 = open("poem.txt", "r")

#print through every line
for line in file_2:
    print(line)

#close file
file_2.close()

count = 0
#open file
file_3 = open("names.txt", "r")

for line in file_3:
    #counts for lisa
    if line == "Lisa":
        count = count + 1

file_3.close()
print(count)


file_4 = open("CS4Ever.txt", "w")

#writing to the file
file_4.write("Computer Science is great. If there were no programmers, there would be no video games!")

read_1 = file_4.read()
print(read_1)

file_4.close()



    


'''
#open file
my_file = open("example.txt", "w")

#loop to print alphabet
for i in range(65,91):
    my_file.write(chr(i) + "|")
    
#close file
my_file.close()
#append to a file
the_file = open("example.txt", "a")

#write to file
the_file.write("\nThis is the alphabet")
#close file
the_file.close()

#open file
file_1 = open("example.txt", "r")

#read the file
all_data = file_1.read()

#print what it has read
print(all_data)

#close
file_1.close()


file_2 = open("example.txt", "r")

for line in my_file:
    print(line)

my_file.close()'''
