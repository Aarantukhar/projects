#subroutine to make it lowercase
def lower_case(x):
   #getting ascii value 
   value = ord(x[0])
   #checks if it falls into a-z because it doesnt need to do anything
   if value >= 97 and value <= 122:
       return x
    #adds 32 to make it lower case
   value = value + 32
   #turns ascii value into character
   x = chr(value)
   return x 

#subroutine to make it upper case           
def upper_case(x):
   value = ord(x[0])
    #checks if it falls into A-Z because it doesnt need to do anything
   if value >= 65  and value <= 90:
       return x
    #subtracts 32 to its ascii value to make it uppercase
   value = value - 32
   #turns ascii value into character
   x = chr(value)
   return x 
            
#subroutine to make it alternate between upper and lower case
def wonky(word):
    out_word = ""
    #goes through all the characters
    for i in range(len(word)-1):
        if i % 2 == 0:
            #every 2 numbers in the string it will make it lowercase
            out_word + lower_case(word[i])

        else:
            #else it will make it up uppercase
            out_word + upper_case(word[i])

    return out_word
    print(out_word)
   
   
        
       


#user input

word = input("Enter a word : ")
word = wonky(word)

print(word)
