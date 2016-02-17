/*
 * Program Name	: stack.c
 * Aurthor		: Victor Banerjee
 * 
 * Implementation of Stack Using Arrays
 * A stack is generally implemented with two basic operations – push and pop.
 * Push means to insert an item on to stack. tos is a pointer which denotes the position of top most item in the stack. 
 * Stack is represented by the array arr and MAXSTACK represents the maximum possible number of elements in the stack.
 * 					----------------------------------------
 * 					Algorithm to push an item onto the stack
 * 					----------------------------------------
 * Step 1: 	[Check for stack overflow]
 * 			if tos >=MAXSTACK
 * 			print “Stack overflow” and exit
 * Step 2: 	[Increment the pointer value by one]
 * 			tos=tos+1
 * Step 3:	[Insert the item]
 * 			arr[tos]=value
 * Step 4: Exit
 * 					----------------------------------------
 * 					Algorithm to POP an item onto the stack
 * 					----------------------------------------
 * Step 1: [Check whether the stack is empty]
 * 			if tos = 0
 * 			print “Stack underflow” and exit
 * Step 2: [Remove the top most item]
 * 			value=arr[tos]
 * 			tos=tos-1
 * Step 3: [Return the item of the stack]
 * 			return(value)
 */


#include <stdio.h>

int choice,stack[10],top,element;

void menu();
void pop();
void push();
void showelements();

void main()
	{
		choice=element=1;
		top=0;
		menu();
		}
void menu()
	{
		printf("\n\nEnter the following options:\n");
		printf("\n 1.PUSH\n 2.POP\n 3.SHOW ELEMENTS\n 4. EXIT\n\n Your Choice : ");
		scanf("%d",&choice);
		
		if (choice==1)
		{
			push();
			menu();
		}
		if (choice==2)
		{
			pop();
			menu();
		}
		if (choice==3)
		{
			showelements();
			menu();
		}
		
		}

void push()
{
	if (top<=9)
	{
		printf("Enter the element to be pushed to stack : ");
		scanf("%d",&element);
		printf("\nElement Added !!");
		stack[top]=element;
		++top;
	}
	else 
		printf("\nStack is Full\n");
		return;
	}

void pop()
{
	if (top>0)
	{
		--top;
		element==stack[top];
		printf("\nPopped Element: %d\n",element);
	}
	else
		printf("Stack is Empty%d\n",element);
	return;
	}
	
void showelements()
{
	if (top <= 0)
		printf("Stack is empty\n");
	else
		printf("Elements in the Stack:");
		for (int i = 0; i < top; i++)
		{
			printf("\n%d", stack[i]);
		}
		
	}
