#include<stdio.h>
int main(){
   int i, j, count, temp, number[25];

   printf("How many numbers u are going to enter?: ");
   scanf("%d",&count);
printf("Enter %d elements: ", count);
   // This loop would store the input numbers in array
   for(i=0;i<count;i++)
      scanf("%d",&number[i]);
