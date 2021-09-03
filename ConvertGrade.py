# A program that'll convert numbers scores into grades
# 0.9 - 1.0 = A
# 0.8 - 0.89 = B
# 0.7 - 0.79 = C
# 0.6 - 0.69 = D
# 0.0 - 0.59 = F

try:                                                                     # 'Try' and 'except' to receive and validate the scores
    score = float(input ('What is the score (0.0 - 1):'))                # Any invalid score will show the error message and quit the program
except:
    print ('Please try again and insert a valid score')
    quit ()


if score > 1 or score < 0:                                               # 'If' to certify that the user entered a score between 0.0 - 1
    print ('Score out of range, try again')                              # If not the program will show the error message and quit
    quit ()


if score >= 0.9:                                                           
	grade = 'A'

elif score >= 0.8:
	grade ='B'                                                          # Ifs and elifs to convert scores into grades

elif score >= 0.7:
	grade ='C'

elif score >= 0.6:
	grade ='D'

elif score < 0.6:
	grade ='F'

print (grade)                                                          # Show the final grade