                        # Thats a program to receive a random amount of numbers from a user and print out the smallst and largest between those numbers


largest = - 1                                                     # Just variables
smallest = None

while True:                                                       # A while to keep receiving the amount of the numbers that the user wants
    inumbers = input('Enter a number/done: ')                     # Receive the numbers and the word ('done') to stop the user from inserting numbers
    if inumbers == 'done':                                        
        break

    try:                                                          # 'Try' and 'except' to make sure that the user is inserting only numbers
        numbers = float(inumbers)                                 # If the user inserts something that isn't a number the program will show the message 'Invalid input' until a valid number is inserted
        for number in [numbers]:                                  # 'For' loop to check which of the numbers are the largest and smallest
            if number > largest :
                largest = number
        
        for number in [numbers]:
            if smallest is None:
                smallest = number
            elif number < smallest:
                smallest = number
                
    except:
        print('Invalid Input')


print('Maximum is', largest)                                      # Print out the largest and smallest number that has been inserted
print('Minimum is', smallest)                                     
