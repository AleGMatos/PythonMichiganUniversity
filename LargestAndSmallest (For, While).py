largest = - 1
smallest = None


while True:
    inumbers = input("Enter a number/done: ")
    if inumbers == "done":
        break
    try:
        numbers = float(inumbers)
    except:
        print('Invalid input')
        

    for number in [numbers]:
        if number > largest :
            largest = number
    
    for number in [numbers]:
        if smallest is None:
            smallest = number
        elif number < smallest:
            smallest = number

print('Maximum is', largest)
print('Minimum is', smallest)
