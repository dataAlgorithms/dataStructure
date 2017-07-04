/*
Question:
 Given an array, print the Next Greater Element (NGE) for every element. 
The Next greater Element for an element x is the first greater element
 on the right side of x in array. Elements for which no greater element 
exist, consider next greater element as -1.

Algorithms:
1) Push the first element to stack.
2) Pick rest of the elements one by one and follow following steps in loop.
….a) Mark the current element as next.
….b) If stack is not empty, then pop an element from stack and compare it with next.
….c) If next is greater than the popped element, then next is the next 
greater element for the popped element.
….d) Keep popping from the stack while the popped element is smaller than next. 
next becomes the next greater element for all such popped elements
….g) If next is smaller than the popped element, then push the popped element back.
3) After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.

Time complexity:
O(n). The worst case occurs when all elements are sorted
 in decreasing order. If elements are sorted in decreasing order, 
then every element is processed at most 4 times.
a) Initially pushed to the stack.
b) Popped from the stack when next element is being processed.
c) Pushed back to the stack because next element is smaller.
d) Popped from the stack in step 3 of algo.

Output:

 11 --> 13
 13 --> 21
 3 -- -1
 21 -- -1


 4 --> 5
 2 --> 25
 5 --> 25
 25 -- -1


 6 --> 12
 7 --> 12
 12 -- -1
 13 -- -1


 8 --> 58
 58 --> 71
 18 --> 31
 31 --> 32
 32 --> 63
 63 --> 92
 71 --> 92
 3 --> 91
 43 --> 91
 91 --> 93
 92 --> 93
 25 --> 80
 28 -- -1
 80 -- -1
 93 -- -1
*/

#include <stdio.h>
#include <stdlib.h>
#define STACKSIZE 100

// stack structure
struct stack
{
    int top;
    int items[STACKSIZE];
};

// push for stack
void push(struct stack *ps, int x)
{
    if (ps->top == STACKSIZE-1)
    {
        printf("Error: stack overflow\n");
        exit(0);
    }
    else
    {
        ps->top += 1;
        int top = ps->top;
        ps->items[top] = x;
    }
}

bool isEmpty(struct stack *ps)
{
    return (ps->top == -1)? true: false;
}

int pop(struct stack *ps)
{
    int temp;
    if (ps->top == -1)
    {
        printf("Error: stack underflow\n");
        exit(0);
    }
    else
    {
        int top = ps->top;
        temp = ps->items[top];
        ps->top -= 1;
        return temp;
    }
}

// print element and NGE pair for all elements of arr of size n
void printNGE(int arr[], int n)
{
    int i = 0;
    struct stack s;
    s.top = -1;
    int element, next;

    // push the first element to stack
    push(&s, arr[0]);

    // iterate for rest of the elements
    for (i=1; i<n; i++)
    {
        next = arr[i];

        if (isEmpty(&s) == false)
        {
            // if stack is not empty, then pop an element from stack
            element = pop(&s);

            /* if the popped element is smaller than next, then
             a) print the pair
             b) keep popping while elements are smaller and stack is not empty
            */
            while (element < next)
            {
                printf("\n %d --> %d", element, next);
                if(isEmpty(&s) == true)
                    break;
                element = pop(&s);
            }         

            /* If element is greater than next, then
               push the element back */
            if (element > next)
                push(&s, element);
        }

        /* push next to stack so that we can find next greater for it*/
        push(&s, next);     
    }

    /* after iterating over the loop, the remaining element
       in stack do no have the next greater elements
       so print -1 for them*/
    while (isEmpty(&s) == false)
    { 
        element = pop(&s);
        next = -1;
        printf("\n %d -- %d", element, next);
    }

    printf("\n\n");
}

// Driver program 
int main()
{
    int arr[] = {11, 13, 21, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    printNGE(arr, n);

    int arr1[] = {4, 5, 2, 25};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    printNGE(arr1, n1);

    int arr2[] = {13, 7, 6, 12};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    printNGE(arr2, n2);

    int arr3[] = {8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28};
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    printNGE(arr3, n3);

    return 0;
}

附1：
replace-every-element-with-the-greatest-on-right-side/
 http://www.geeksforgeeks.org/replace-every-element-with-the-greatest-on-right-side/

附2：
replace-every-element-with-the-least-greater-element-on-its-right/
 http://www.geeksforgeeks.org/replace-every-element-with-the-least-greater-element-on-its-right/
