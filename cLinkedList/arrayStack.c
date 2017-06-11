/*
 * arrayStack.c
 *
 *  Created on: 2017年6月7日
 *      Author: baobao
 */

#include <stdio.h>
#include <stdlib.h> /* for dynamic allocation*/

#define MAXSIZE 100
struct ArrayStack{
    int top;
    int capacity;
    int *array;
};

struct ArrayStack *createStack() {
    struct ArrayStack *S = (struct ArrayStack *)malloc(sizeof(struct ArrayStack));
    if(!S)
        return NULL;
    S->capacity = MAXSIZE;
    S->top = -1;
    S->array = (int *)malloc(S->capacity * sizeof(int));
    if(!S->array)
        return NULL;
    return S;
}

int isEmptyStack(struct ArrayStack *S) {
    //if the condition is true then 1 is returned else 0 is returned
    return (S->top == -1);
}

int isFullStack(struct ArrayStack *S) {
    //if the condition is true then 1 is returned else 0 is returned
    return (S->top == S->capacity-1);
}

void push(struct ArrayStack *S, int data) {
    /* S->top == capacity -1 indicate that the stack is full*/
    if (isFullStack(S))
        printf("Stack Overflow");
    else  /*Increasing the top by 1 and storing the value at top position*/
        S->array[++S->top] = data;
        printf("%d pushed to stack\n", data);
}

int pop(struct ArrayStack *S) {
    /* S->top == -1 indicates empty stack*/
    if(isEmptyStack(S)) {
        printf("Stack is Empty");
        return -1;
    }
    else /* Removing element from top of the array and reducing top by 1*/
        return (S->array[S->top--]);
}

void deleteStack(struct ArrayStack *S) {
    if(S) {
        if(S->array)
            free(S->array);
        free(S);
    }
}

//Driver program to test above functions
/*
 the stack is empty?1
the stack is full?0
10 pushed to stack
20 pushed to stack
30 pushed to stack
30 poped from stack
the stack is empty?0
the stack is full?0
the top is 20
destroy stack
 */
int main()
{
    struct ArrayStack* stack = createStack();
    printf("the stack is empty?%d\n", isEmptyStack(stack));
    printf("the stack is full?%d\n", isFullStack(stack));

    push(stack, 10);
    push(stack, 20);
    push(stack, 30);

    printf("%d poped from stack\n", pop(stack));
    printf("the stack is empty?%d\n", isEmptyStack(stack));
    printf("the stack is full?%d\n", isFullStack(stack));
    printf("the top is %d\n", stack->array[stack->top]);

    printf("destroy stack\n");
    deleteStack(stack);

    return 0;
}
