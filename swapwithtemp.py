# Program for swapping two numbers with temporary variables

print('Enter two numbers')
a=input()
b=input()
print('Numbers before swapping are: '+a+' and '+b)
temp=a
a=b
b=temp
print('Numbers after swapping are: '+a+' and '+b)