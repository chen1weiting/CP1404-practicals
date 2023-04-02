score = float(input('Enter score: ')) # input a score
if score > 100 or score < 0: # check if the score is valid
    print('Invalid score')
elif score >= 90: # if the score is greater than or equal to 90
    print('Excellent')
elif score >= 50: # if the score is greater than or equal to 50
    print('Passable')
else: # if the score is less than 50
    print('Bad')