/*
 * ------------------------------------------------------
 * File Name	:factorial.c
 * Developer	:Victor Frankenstein (Banerjee)
 * Date & Time	:22.02.2016 19:00:142016-02-22 
 * Copyright 2016 Victor Frankenstein (Banerjee) <recervictory@gmail.com>
 * ------------------------------------------------------
 * Program to find factorial using recursion
 * ------------------------------------------------------
 */

#include <stdio.h>
int fact(int n);
void main()
	{
		int n,factorial;
		printf("Enter any number :");
		scanf("%d",&n);
		factorial=fact(n);
		printf("\nFactorial of %d number :%d\n",n,factorial);
		}

int fact(int n)
	{
		int res;
		if (n ==1)
			return (1);
		else 
			res=n*fact(n-1);
		return (res);
		}
