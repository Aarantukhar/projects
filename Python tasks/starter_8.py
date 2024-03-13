import random

#intialising variables
white = 23
black = 34
beans = 57



#untill the beans have ran out
while beans != 0:
    #random number between 0 and 1
    monkey = random.randint(0,1)

    #selection if they pick white or black
    if monkey ==  0:
        black = black - 1
        beans = beans -1
        print("The monkey picked a black bean")

    if monkey == 1:
        white = white - 1
        beans = beans - 1
        print("The monkey picked a white bean")
        
    #deciding what colour the bean was
    if beans == 0 and monkey == 1:
        print("The last bean was white")

    if beans == 0 and monkey == 0:
        print("The last bean was black")
