largest=0
smallest=0
while True:
    try:
        num=input('Enter a number: ')
        if num=='done':
            break
        if largest==0:
            largest=int(num)
        if smallest==0:
            smallest=int(num)
        if int(num)>largest:
            largest=int(num)
        if int(num)<smallest:
            smallest=int(num)
    except:
        print('Ignored')
        continue
print('Maximum: '+str(largest))
print('Minimum: '+str(smallest))    


