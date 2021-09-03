# Program to calculate pay while using a function 'computepay'


def computepay(hrs, hrate):                                             # Function ('computepay') that'll calculate the pay 
    calculate = (40 * hrate + (hrs-40) * 1.5* hrate)
    return calculate

try:                                                                    # 'try' and 'except' to receive the hours and verify if the numbers are valid
    hrs = float(input("Enter Hours: "))
except:
    hrs = - 1
 

if hrs >= 0 :                                                           # 'if' to validate the hours and show a error message if the numbers weren't valid
    print ('Valid number :)')                                   
else:
    print ('Invalid or not a number')
    quit()


try:                                                                    # 'try' and 'except' to receive the payrate/h and verify if the numbers are valid
    hrate = float(input("Enter hourly rate: "))
except:
    hrate = - 1

if hrate >= 0 :                                                         # 'if' to validate the hours and show a error message if the numbers weren't valid
    print ('Valid number :)')
else:
    print ('Invalid or not a number')
    quit()


pay = computepay(hrs, hrate)                                            # Calling the function that'll calculate the pay and after print out the final pay
print("Pay", pay)