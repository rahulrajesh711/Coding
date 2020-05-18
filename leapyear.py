#Program for detecting a leapyear.


# Rules for checking Leapyear:
#        1.If centuary year and divisible by 400=Leapyear
#        2.If not centuary year but divisible by 4=Leapyear
a=input('Enter a Year: ')
if (int(a)%100==0):        #To check centuary year or not
    if (int(a)%400==0):    #Neasted if condition to check divisibility by 4 
        print('The year '+a+' is a Leap Year')
    else:
        print('The year '+a+' is Not a Leap Year')    
elif (int(a)%4==0):        #else condition to check divisibility by 4
    print('The year '+a+' is a Leap Year')
else:
    print('The year '+a+' is Not a Leap Year') 


