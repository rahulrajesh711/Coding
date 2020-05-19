// Program to swap two numbers with temporary variable

#include<stdio.h>
void main()
{
    int a,b,temp;  //extra variable for swapping
    printf("Enter two integers: \n");
    scanf("%d",&a);
    scanf("%d",&b);
    printf("The numbers before swapping are: %d and %d\n",a,b);
    temp=a;   //logic
    a=b;      //logic
    b=temp;   //logic
    printf("The numbers after swapping are: %d and %d\n",a,b);
}