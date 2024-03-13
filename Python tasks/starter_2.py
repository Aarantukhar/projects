#length of the string
#subroutine 
def length(word_1):
    count = 0
    #length
    length = len(word_1)
    #selection 
    if length <= 6:
        print(word_1)
    else:
        #for loop that checks every letter for an "a"
        for x in range(length):
            if word_1[x] == "a":
                #incrementing count
                count = count + 1
    #checking if there is an odd amount of "a"'s
    if count % 2 == 1:
        print(word_1 + "a")
            
#input from user
word = input("Enter anything : ")
num = int(input("How many a's do you want in your string? : "))
#calling subroutines
length(word)
