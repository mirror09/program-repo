#include <stdio.h>
int add(int dec1);
void complement3s()
{
    printf( "Calculate 3's Complement Decimal Numeber\n" );
}
void dec2ter()
{
    printf( "Decimal to Ternary Coversion\n" );
}
int main()
{	int choice;
	
	printf("1. Decimal to Ternary Coversion\n");
	printf("2. Calculate 3's Complement Decimal Numeber\n");
	printf("3. Addition of Two ternary Number\n" );
	printf("4. Exit\n" );
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
int add(long int dec1,dec2)
{
	 long int binary1,binary2;
    int i=0,remainder = 0,sum[20];

    printf("Enter any first binary number: ");
    scanf("%ld",&binary1);
    printf("Enter any second binary number: ");
    scanf("%ld",&binary2);

    while(binary1!=0||binary2!=0)
		{
			sum[i++] =  (binary1 %10 + binary2 %10 + remainder ) % 8;
			printf("bin1:%ld bin2:%ld\n",binary1 %10,binary2 %10)
			remainder = (binary1 %10 + binary2 %10 + remainder ) / 8;
			binary1 = binary1/10;
			binary2 = binary2/10;
		}

    if(remainder!=0)
         sum[i++] = remainder;

    --i;
    printf("Sum of two binary numbers: ");
    while(i>=0)
         printf("%d",sum[i--]);

   return 0;
	}
