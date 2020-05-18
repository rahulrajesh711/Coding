//Program for detecting a leapyear.


// Rules for checking Leapyear:
//        1.If centuary year and divisible by 400=Leapyear
//        2.If not centuary year but divisible by 4=Leapyear
#include<stdio.h>
void main()
{
    int a;
    printf("Enter a Year: ");
    scanf("%d",&a);
    if (a%100==0)               //To check centuary year or not
    {
        if(a%400==0)            //Neasted if condition to check divisibility by 4 
        {
            printf("The year %d is a Leap Year.",a);
        }
        else
        {
            printf("The year %d is Not a Leap Year",a);
        }
        
    }
    else if (a%4==0)            //else condition to check divisibility by 4
    {
        printf("The year %d is a Leap Year",a);
    }
    else
    {
        printf("The year %d is Not a Leap Year",a);
    }
    
    
}