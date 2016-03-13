#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
	{
		int comp=3,quotient,decimalNumber;
		int terNumber[10],i=1,j;
		
		printf("Enter a Decimal Number :");
		scanf("%d",&decimalNumber);
		quotient = abs(decimalNumber);
  
  for (j = 8; j >0 ; j--)
  {		
	  terNumber[j]=0;
	  if(decimalNumber <0)
	  terNumber[8]=1;
		
  }
  if(decimalNumber > 0)
	{
	  while(quotient!=0){
      terNumber[i++]= quotient % 3;
      quotient = quotient / 3;
  }

		}
	else
	{
	  while(quotient!=0){
		terNumber[i++]=comp - (quotient % 3);
		comp=2;
		quotient = quotient / 3;
	    }
		}
	printf("Equivalent Ternary value of decimal number %d:",decimalNumber);
	for(j = 8 ;j> 0;j--)
		printf("%d",terNumber[j]);
	printf("\n");
      return 0;
		}
