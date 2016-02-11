#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int add(void);
int dec2ter(void);
int complement3s();
/*Main Function*/
int main()
{	int choice;
	
	printf("1. Decimal to Ternary Coversion\n");
	printf("2. Calculate 3's Complement Decimal Numeber\n");
	printf("3. Addition of Two ternary Number\n" );
	printf("4. Exit\n" );
	printf("\n\nYour choice :" );
	scanf("%d", &choice);
	
	switch (choice)
	{
		case 1:
			dec2ter();
			break;
		case 2:
			complement3s();
			break;
		case 3:
			add();
			break;
		case 4:
			printf("Thanks!\n");
			break;
		default:
			printf("Invalid Input...\n");
			break;
	}
	
	
	}
/*Addition of two ternary number function*/
int add( void)
{
	long int binary1,binary2;
    int i=0,remainder = 0,sum[20];
	printf("Enter any first binary number: ");
    scanf("%ld",&binary1);
    printf("Enter any second binary number: ");
    scanf("%ld",&binary2);
	printf("\n");
    while(binary1!=0||binary2!=0)
		{
			sum[i++] =  (binary1 %10 + binary2 %10 + remainder ) % 3;
			remainder = (binary1 %10 + binary2 %10 + remainder ) / 3;
			binary1 = binary1/10;
			binary2 = binary2/10;
		}

    if(remainder!=0)
         sum[i++] = remainder;

    --i;
    printf("Sum of two binary numbers: ");
    while(i>=0)
         printf("%d",sum[i--]);
	printf("\n");
   return 0;
	}
/*Decimal to Ternary*/
int dec2ter(void)
{
  long int decimalNumber,remainder,quotient;
  int octalNumber[10],i=1,j;

  printf("Enter any decimal number: ");
  scanf("%ld",&decimalNumber);

  quotient = abs(decimalNumber);
  for (j = 8; j >0 ; j--)
  {
	  if(decimalNumber >0)
		octalNumber[j]=0;
	  else
		octalNumber[j]=1;
  }
  

  while(quotient!=0){
      octalNumber[i++]= quotient % 2;
      quotient = quotient / 2;
  }

  printf("Equivalent Ternary value of decimal number %ld:",decimalNumber);
  for(j = 8 ;j> 0;j--)
      printf("%d",octalNumber[j]);
  printf("\n");
  return 0;  
}
/*Calculate 3's Complement Decimal Numeber*/
int complement3s(void)
{
  long int decimalNumber,remainder=3,quotient,logs;
  int octalNumber[100],i=1,j,k=1;

  printf("Enter any decimal number: ");
  scanf("%ld",&decimalNumber);

  quotient = decimalNumber;

  while(quotient!=0){
      octalNumber[i++]=remainder - (quotient % 3);
      remainder=2;
      quotient = quotient / 3;
  }
  printf("Equivalent 3's Ternary value of decimal number %ld: ",decimalNumber);
  for(j = i -1 ;j> 0;j--){
      printf("%d",octalNumber[j]);
  }
  printf("\n");
  return 0;
}

