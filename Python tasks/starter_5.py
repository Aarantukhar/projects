#aaran



#loops untill end goal is met
def alphabet(start):
    x = 0
    while x == 0:
        start = start + 1
    #for loop
        for i in range(start,122):
            print(end = " " + chr(i + 1))
        print("\n")
        if start == 123:
            x = 1



start = input("Enter start value a-z to start the count at : ")
start_i = ord(start)-1

alphabet(start_i)

down(start_i)


































