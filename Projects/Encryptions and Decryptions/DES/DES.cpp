#include<stdio.h>
int main()
{
 int i, cnt=0, p8[8]={6,7,8,9,1,2,3,4};
 int p10[10]={6,7,8,9,10,1,2,3,4,5}; // Keys Already Declared
 
 char input[11], k1[10], k2[10], temp[11];
 char LS1[5], LS2[5];
 //k1, k2 are for storing interim keys
 //p8 and p10 are for storing permutation key
 
 //Read 10-bit from user...
 printf("Enter 10-bit input: ");
 scanf("%s",input); 
 input[10]='\0';
 
 //Applying permutation...
 for(i=0; i<10; i++)
 {
  cnt = p10[i];
  temp[i] = input[cnt-1];
 }
 temp[i]='\0';
 printf("\nYour 10 Rounds keys are: ");
 for(i=0; i<10; i++)
 { printf("%d,",p10[i]); }
 
 printf("\nBits after Round-10: ");
 puts(temp);
 //Performing Linear Shift on first half of temp
 for(i=0; i<5; i++)
 {
  if(i==4)
   temp[i]=temp[0];
  else
   temp[i]=temp[i+1];   
 }
 //Performing Liner Shift on second half of temp
 for(i=5; i<10; i++)
 {
  if(i==9)
   temp[i]=temp[5];
  else
   temp[i]=temp[i+1];   
 }
 printf("Output: ");
 puts(temp);
}

