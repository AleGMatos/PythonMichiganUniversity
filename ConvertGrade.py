try:
    score = float(input ('What is the score (0.0 - 1):'))
except:
    print ('Please try again and insert a valid score')
    quit ()


if score > 1 or score < 0:
    print ('Score out of range, try again')
    quit ()


if score >= 0.9:
	grade = 'A'

elif score >= 0.8:
	grade ='B'

elif score >= 0.7:
	grade ='C'

elif score >= 0.6:
	grade ='D'

elif score < 0.6:
	grade ='F'

print (grade)