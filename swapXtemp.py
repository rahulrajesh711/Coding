# Program to swap two numbers without temporary variable

print('Enter two Integers:')
a=input()
b=input()
print('Numbers before swapping are: '+a+' and '+b)
a=int(a)+int(b)                                         #int convert need 
b=int(a)-int(b)
a=int(a)-int(b)
print('Numbers after swapping are: '+str(a)+' and '+str(b)) #str convert needed for concatnation