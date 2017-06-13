/*
Prerequisite: 
Infix expression:The expression of the form a op b. 
When an operator is in-between every pair of operands.

Postfix expression:The expression of the form a b op. 
When an operator is followed for every pair of operands.

Algorithm:
1. Scan the infix expression from left to right.
2. If the scanned character is an operand, output it.
3. Else,
…..3.1 If the precedence of the scanned operator is greater than
    the precedence of the operator in the stack(or the stack is empty), push it.
…..3.2 Else, Pop the operator from the stack until the precedence of the 
    scanned operator is less-equal to the precedence of the operator residing on the 
    top of the stack. Push the scanned operator to the stack.
4. If the scanned character is an ‘(‘, push it to the stack.
5. If the scanned character is an ‘)’, pop and output from the stack until an ‘(‘ is encountered.
6. Repeat steps 2-6 until infix expression is scanned.
7. Pop and output from the stack until it is not empty.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Stack type
struct Stack 
{
    int top;
    unsigned capacity;
    int *array;
};

// Stack Operations
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

//A utility function to check if the given character is operand
int isOperand(char ch)
{
    return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z');
}

//A utility function to return precedence of a given operator
//Higher returned value means higher precedence
int Prec(char ch)
{
    switch (ch)
    {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
    }
    return -1;
}

//The main function that converts given infix expression
// to postfix expression
int infixToPostfix(char* exp)
{
    int i, k;

    //Create a stack of capacity equal to expression size
    struct Stack* stack = createStack(strlen(exp));
    if(!stack) // See if stack was created successfully
        return -1;

    for (i = 0, k = -1; exp[i]; ++i)
    {
        //If the scanned character is an operand, add it to output
        if (isOperand(exp[i]))
            exp[++k] = exp[i];

        //If the scanned character is an '(', push it to the stack
        else if (exp[i] == '(')
            push(stack, exp[i]);

        //If the scanned character is an ')', pop and output from the stack
        //until an '(' is encountered
        else if (exp[i] == ')')
        {
            while (!isEmpty(stack) && peek(stack) != '(')
                exp[++k] = pop(stack);
            if (!isEmpty(stack) && peek(stack) != '(')
                return -1; // invalid expression
            else
                pop(stack);
        }
        else // an operator is encountered
        {
            while (!isEmpty(stack) && Prec(exp[i]) <= Prec(peek(stack)))
                exp[++k] = pop(stack);
            push(stack, exp[i]);
        }
    }

    //pop all the operators from the stack
    while (!isEmpty(stack))
        exp[++k] = pop(stack);
    exp[++k] = '\0';
    printf("%s\n", exp);
}

//Driver program 
int main()
{
    char exp1[] = "a+b*(c^d-e)^(f+g*h)-i";
    infixToPostfix(exp1);

    char exp2[] = "A*(B+C)/D";
    infixToPostfix(exp2);

    return 0;
}

/*
abcd^e-fgh*+^*+i-
ABC+*D/
*/
