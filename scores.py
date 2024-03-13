# get input from the user for six scores
scores = []
for i in range(6):
    score = float(input("enter score out of 10: "))
    scores.append(score)

# eliminate the lowest and highest scores
scores.sort()
trimmed_scores = scores[1:-1]

# calculate and print the final score
final_score = sum(trimmed_scores)
print("final score of the gymnast: " + str(final_score))
