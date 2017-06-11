#include <stdio.h>
#include <stdlib.h>

struct DynArrayStack {
    int top;
    int capacity;
    int *array;
};

struct DynArrayStack *CreateStack() {
    struct DynArrayStack *S = malloc(sizeof(struct DynArrayStack));
    if(!S)
        return NULL;
    S->capacity = 1;
    S->top = -1;
    S->array = malloc(S->capacity * sizeof(int)); //allocate an array of size 1 initially

    if(!S->array)
        return NULL;

    return S;
}

int IsFullStack(struct DynArrayStack *S) {
    return (S->top == S->capacity-1);
}

void DoubleStack(struct DynArrayStack *S) {
    S->capacity *= 2;
    S->array = realloc(S->array, S->capacity * sizeof(int));
}

void Push(struct DynArrayStack *S, int x) {
    //No overflow in this implementation
    if(IsFullStack(S))
    	DoubleStack(S);
    S->array[++S->top] = x;
}

int IsEmptyStack(struct DynArrayStack *S) {
    return S->top == -1;
}

int Top(struct DynArrayStack *S) {
    if(IsEmptyStack(S))
        return -1;

    return S->array[S->top];
}

int Pop(struct DynArrayStack *S) {
    if(IsEmptyStack(S))
        return -1;
    return S->array[S->top--];
}

void DeleteStack(struct DynArrayStack *S) {
    if(S) {
        if(S->array)
            free(S->array);

        free(S);
    }
}

/*
 the stack is empty?1
the stack is full?0
30 poped from stack
the stack is empty?0
the stack is full?0
the top is 20
destroy stack
 */
int main()
{
    struct DynArrayStack* stack = CreateStack();
    printf("the stack is empty?%d\n", IsEmptyStack(stack));
    printf("the stack is full?%d\n", IsFullStack(stack));

    Push(stack, 10);
    Push(stack, 20);
    Push(stack, 30);

    printf("%d poped from stack\n", Pop(stack));
    printf("the stack is empty?%d\n", IsEmptyStack(stack));
    printf("the stack is full?%d\n", IsFullStack(stack));
    printf("the top is %d\n", stack->array[stack->top]);

    printf("destroy stack\n");
    DeleteStack(stack);

    return 0;
}

/*
 Too many doublings may cause memory overflow exception
 */
