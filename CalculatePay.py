hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    h = - 1

if h > 0 :
    print ('Nice work')
else:
    print ('Not a number')
    quit()


rate = input("Enter pay rate:")
try:
    r = float(rate)
except:
    r = - 1
    

if r > 0 :
    print ('Nice work')
    if h <= 40:
        pay = h * r
        print (pay)
    else:
        pay = (40 * r + (h-40)*1.5*r)
        print (pay)
        

else:
    print ('Not a number')
    print ('Could not calculate the pay')

