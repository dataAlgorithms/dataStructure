/*
Question:
Design a stack with operations on middle element
How to implement a stack which will support following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations.

The important question is, whether to use a linked list or array for implementation of stack?

Algorithms:
Please note that, we need to find and delete middle element.
Deleting an element from middle is not O(1) for array.
Also, we may need to move the middle pointer up when we push an element
and move down when we pop(). In singly linked list, moving middle pointer
in both directions is not possible.

The idea is to use Doubly Linked List (DLL). We can delete middle element in O(1) time
by maintaining mid pointer. We can move mid pointer in both directions using previous and next pointers.

Following is C implementation of push(), pop() and findMiddle() operations.
Implementation of deleteMiddle() is left as an exercise.
If there are even elements in stack, findMiddle() returns the first middle element. For example,
if stack contains {1, 2, 3, 4}, then findMiddle() would return 2.

Time Complexity:
O(1)

Output:
Stack is empty.
Middle element: -2147483648

5 pushed to stack.
10 pushed to stack.
15 pushed to stack.

Stack:
15 10 5

Middle element: 10

Deleting middle:

Stack:
15 5

15 popped from stack.

Stack:
5

Middle element: 5

Deleting middle:

Stack:


Stack underflow.
Top element in stack is -2147483648.

15 pushed to stack.

Top element in stack is 15.

Stack:
15

Middle element: 15
*/

#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
 
typedef struct StackNode {
	int data;
	struct StackNode *next;
	struct StackNode *prev;
}Node;
 
typedef struct stack {
	Node *top;
	Node *mid;
	int count;
}Stack;
 
Stack *createStack() {
	Stack *stack = (Stack *) malloc(sizeof(Stack));
	stack->top = NULL;
	stack->mid = NULL;
	stack->count = 0;
	return stack;
}
 
Node* newNode(int data) {
	Node *node = (Node *) malloc(sizeof(Node));
	node->data = data;
	node->next = NULL;
	node->prev = NULL;
	return node;
}
 
int isEmpty(Stack *stack) {
	return !(stack->top);
}
 
void push(Stack *stack, int item) {
	Node *node = newNode(item);
	if(node == NULL) {
		printf("Stack overflow");
		return;
	}
 
	node->next = stack->top;
	stack->top = node;
	stack->count++;
 
	if(stack->count == 1) {
		node->prev = NULL;
		stack->mid = node;
	}
	else {
		node->next->prev = node;
		if((stack->count) & 1)
			stack->mid = stack->mid->prev;
	}
 
	printf("%d pushed to stack.\n",item);
}
 
int pop(Stack *stack) {
	if(isEmpty(stack)) {
		printf("Stack underflow.\n");
		return INT_MIN;
	}
	Node *temp = stack->top;
	stack->top = stack->top->next;
	int popped = temp->data;
	free(temp);
 
	if(!isEmpty(stack))
		stack->top->prev= NULL;
 
	stack->count--;
 
	if(!((stack->count) & 1))
		stack->mid = stack->mid->next;
 
	return popped;
}
 
int peek(Stack *stack) {
	if(isEmpty(stack)) {
		printf("Stack underflow.\n");
		return INT_MIN;
	}
 
	return stack->top->data;
}
 
void printStack(Stack *stack) {
	Node *node = stack->top;
	while(node) {
		printf("%d ",node->data);
		node = node->next; 
		if(node == stack->top)
			break;
	}
 
	printf("\n");
}
 
int findMiddle(Stack *stack) {
	if(isEmpty(stack)) {
		printf("Stack is empty.\n");
		return INT_MIN;
	}
	return stack->mid->data;
}
 
void deleteMiddle(Stack *stack) {
	if(isEmpty(stack)) {
		printf("Stack is empty.\n");
		return;
	}
 
	Node *temp = stack->mid;
 
	if(stack->mid->prev)
		stack->mid->prev->next = stack->mid->next;
	if(stack->mid->next)
		stack->mid->next->prev = stack->mid->prev;
 
	stack->count--;
 
	if(stack->count == 0)
		stack->top = NULL;
 
	if((stack->count) & 1)
		stack->mid = stack->mid->prev;
	else
		stack->mid = stack->mid->next;
 
	free(temp);
}
 
int main() {
	Stack *stack = createStack();
 
	printf("Stack:\n");
	printStack(stack);
	printf("\n");
 
	printf("Middle element: %d\n",findMiddle(stack));
	printf("\n");
 
	push(stack,5);
	push(stack,10);
	push(stack,15);
	printf("\n");
 
	printf("Stack:\n");
	printStack(stack);
	printf("\n");
 
	printf("Middle element: %d\n",findMiddle(stack));
	printf("\n");
 
	printf("Deleting middle:\n");
	deleteMiddle(stack);
	printf("\n");
 
	printf("Stack:\n");
	printStack(stack);
	printf("\n");
 
	printf("%d popped from stack.\n",pop(stack));
	printf("\n");
 
	printf("Stack:\n");
	printStack(stack);
	printf("\n");
 
	printf("Middle element: %d\n",findMiddle(stack));
	printf("\n");
 
	printf("Deleting middle:\n");
	deleteMiddle(stack);
	printf("\n");
 
	printf("Stack:\n");
	printStack(stack);
	printf("\n");
 
	printf("Top element in stack is %d.\n",peek(stack));
	printf("\n");
 
 
	push(stack,15);
	printf("\n");
 
	printf("Top element in stack is %d.\n",peek(stack));
	printf("\n");
 
	printf("Stack:\n");
	printStack(stack);
	printf("\n");
 
	printf("Middle element: %d\n",findMiddle(stack));
 
	return 0;
}
