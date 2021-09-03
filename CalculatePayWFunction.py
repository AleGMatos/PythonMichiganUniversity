def computepay(hrs, hrate):
    calculate = (40 * hrate + (hrs-40) * 1.5* hrate)
    return calculate

try:
    hrs = float(input("Enter Hours:"))
except:
    hrs = - 1
 

if hrs >= 40 :
    pass
else:
    print ('Invalid or not a number')
    quit()


try:
    hrate = float(input("Enter hourly rate:"))
except:
    hrate = - 1

if hrate >= 7.25 :
    pass
else:
    print ('Invalid or not a number')
    quit()


pay = computepay(hrs, hrate)
print("Pay", pay)