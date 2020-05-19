//Program to swap 2 numbers without temporary variable

#include<stdio.h>
void main()
{
    int a,b;
    printf("Enter two Integers: \n");
    scanf("%d",&a);
    scanf("%d",&b);
    printf("Numbers before swapping are: %d and %d\n",a,b);
    a=a+b;    //logic
    b=a-b;    //logic
    a=a-b;    //logic
    printf("Numbers after swapping are: %d and %d",a,b);
}