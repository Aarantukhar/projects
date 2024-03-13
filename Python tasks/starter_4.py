#aaran
#import modules
import random
times = 0


def random_letter():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    word = "dog"
    guess = ""
    count = 0 
    #randomly choose a letter from all the ascii_letters
    while guess != word:
        for i in range(3):
            random_num = random.randint(0,25)
            random_letter = letters[random_num]
            guess = guess + random_letter
            if len(guess) == 3 and guess != word:
                guess = ""
                count = count + 1

    print("It took " + str(count) + " amount of tries to get the word Dog")


random_letter()












































