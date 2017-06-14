/*
Algorithms:
1) Create a stack to store operands (or values).
2) Scan the given expression and do following for every scanned element.
…..a) If the element is a number, push it into the stack
…..b) If the element is a operator, pop operands for the operator from stack. 
Evaluate the operator and push the result back to the stack
3) When the expression is ended, the number in the stack is the final answer

Time complexity:
O(n) where n is number of characters in input expression.
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

//Stack type
struct Stack
{
    int top;
    unsigned capacity;
    int* array;
};

//Stack Operations
struct Stack* createStack(unsigned capacity)
{
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));

    if (!stack) 
        return NULL;

    stack->top = -1;
    stack->capacity = capacity;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
   
    if (!stack->array)
        return NULL;

    return stack;
}

int isEmpty(struct Stack* stack)
{
    return stack->top == -1;
}

char peek(struct Stack* stack)
{
    return stack->array[stack->top];
}

char pop(struct Stack* stack)
{
    if (!isEmpty(stack))
        return stack->array[stack->top--];

    return '$';
}

void push(struct Stack* stack, char op)
{
    stack->array[++stack->top] = op;
}

int evaluatePostfix(char* exp)
{
    //Create a stack of capacity equal to expression size
    struct Stack* stack = createStack(strlen(exp));
    int i;

    //See if stack was created successfully
    if (!stack)
        return -1;

    //Scan all characters one by one
    for (i = 0; exp[i]; ++i)
    {
        //Current token is a whitespace skip it
        if (exp[i] == ' ')
            continue;

        //If the scanned character is an operand (number here),
        //push it to the stack
        if (isdigit(exp[i]))
            push(stack, exp[i] - '0');
        //If the scannd character is an operator, pop two
        //elements from stack apply the operator
        else
        {
            int val1 = pop(stack);
            int val2 = pop(stack);
            switch (exp[i])
            {
                case '+': push(stack, val2 + val1); break;
                case '-': push(stack, val2 - val1); break;
                case '*': push(stack, val2 * val1); break;
                case '/': push(stack, val2 / val1); break;
            }
        }
    }

    return pop(stack);
}

//Driver program 
int main()
{
    char exp[] = "2 3 1 * + 9 -";
    printf("Value of %s is %d", exp, evaluatePostfix(exp));
    return 0;
}

/*
Output:
Value of 2 3 1 * + 9 - is -4
*/
