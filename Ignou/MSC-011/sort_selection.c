/*
 * ------------------------------------------------------
 * File Name	:sort_selection.c
 * Developer	:Victor Frankenstein (Banerjee)
 * Date & Time	:2016-02-24 & {time}
 * Copyright 2016 Victor Frankenstein (Banerjee) <recervictory@gmail.com>
 * ------------------------------------------------------
 * Sorting list of numbers using selection sort method
 * ------------------------------------------------------
 */
#include <stdio.h>
#define SIZE 5

void main()
	{
		int j,min_pos,temp;
		int i;
		int a[SIZE];
		
		for (i = 0; i < SIZE; i++)
		{
			printf("Element No :%d -",i+1);
			printf("Value of the Element: ");
			scanf("%d",&a[i]);
		}
		/* Sorting by descending order*/
		for (i = 0; i < SIZE; i++)
		{
			min_pos=i;
			for (j = i+1; j < SIZE; j++)
			{
				if (a[j] <a[min_pos])
				{
					min_pos=j;
				}
				
			}
			temp=a[i];
			a[i]=a[min_pos];
			a[min_pos]=temp;
		}
		/* print the result */
		printf("\nThe array after sorting:\n");
		for(i=0;i<SIZE;i++)
			printf("%d\n",a[i]);
		}
