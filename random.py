#import module
import random
#intitialise vairiable
sum_1 = 0
count = 0
times = 0
x = 0
#repeat until sum is equal to 48
for i in range(5000):
    sum_1 = 0
    count = 0 
    while sum_1 != 48:
    #3 random numbers
      num1 = random.randint(0,50)
      num2 = random.randint(0,50)
      num3 = random.randint(0,50)
      sum_1 = num1 + num2 + num3
      #how many times it has to loop
      count = count + 1
    x = x + count
 

times = x / 5000
print("It took an average of " + str(times) + " times of generation to get a sum of 48.")
    
