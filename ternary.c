#include <stdio.h>
 
void main()
{
    long num, decimal_num, remainder, base = 1, binary = 0, no_of_1s = 0,remainders = 0,binary1s = 0;
 
    printf("Enter a decimal integer \n");
    scanf("%ld", &num);
    decimal_num = num;
    while (num > 0)
    {
        remainder = num % 3;
        /*  To count no.of 1s */
        if (remainder == 1)
        {
            no_of_1s++;
	    remainders =0;
        }
	else remainders = 1;
        binary = binary + remainder * base;
	binary1s = binary1s + remainders * base; 
        num = num / 3;
        base = base * 10;
    }
    printf("Input number is = %ld\n", decimal_num);
    printf("Its binary equivalent is = %ld\n", binary);
    printf("No.of 1's complement in the binary number is = %ld\n", binary1s);
}
