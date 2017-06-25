/*
Question:
Implement two stacks in an array
Create a data structure twoStacks that represents two stacks. Implementation of
 twoStacks should use only one array, i.e., both stacks should use the same array for
 storing elements. Following functions must be supported by twoStacks.

push1(int x) –> pushes x to first stack
push2(int x) –> pushes x to second stack

pop1() –> pops an element from first stack and return the popped element
pop2() –> pops an element from second stack and return the popped element

Algorithm:
start two stacks from two extreme corners of arr[]. stack1 starts from the leftmost element, 
the first element in stack1 is pushed at index 0. The stack2 starts from the rightmost corner,
 the first element in stack2 is pushed at index (n-1). Both stacks grow (or shrink) in opposite 
direction. To check for overflow, all we need to check is for space between top elements of both stacks. 

Output:
Stack1 is >>
5
11
Stack2 is >>
10
15
7
Poped element from stack1 is 11
Poped element from stack2 is 40
*/


#include <iostream>
#include <stdlib.h>

using namespace std;

class twoStacks
{
    int *arr;
    int size;
    int top1, top2;

public:
    twoStacks(int n)
    {
        size = n;
        arr = new int[n];
        top1 = -1;
        top2 = size;
    }

    // Method to push an element x to stack1
    void push1(int x)
    {
        // There is at least empty space for new element
        if (top1 < top2 - 1)
        {
            top1++;
            arr[top1] = x;
        }
        else
        {
            cout << "Stack overflow";
            exit(1);
        }
    }

    // Method to push an element x to stack2
    void push2(int x)
    {
        // There is at least one empty space for new element
        if (top1 < top2 - 1)
        {
            top2--;
            arr[top2] = x;
        }
        else
        {
            cout << "Stack overflow";
            exit(1);
        }
    }

    // Method to pop an element from first stack
    int pop1()
    {
        if (top1 >= 0)
        {
            int x = arr[top1];
            top1--;
            return x;
        }
        else
        {
            cout << "Stack UnderFlow";
            exit(1);
        }
    }

    // Method to pop an element from second stack
    int pop2()
    {
        if (top2 < size)
        {
            int x = arr[top2];
            top2++;
            return x;
        }
        else
        {
            cout << "Stack Underflow";
            exit(1);
        }
    }

    void displayStack1()
    {
		int i;
        if (top1 == -1)
        {
            cout << "Stack1 is empty\n";
        }
        else
        {
            cout << "Stack1 is >>\n";
            for (i=0; i<= top1; i++)
            {
                cout << arr[i];
                cout << "\n";
            }
        }
    }

    void displayStack2()
    {
		int i;
		
        if (top2 == size)
            cout << "Stack2 is empty\n";
        else
        {
            cout << "Stack2 is >>\n";
            for (i=size-1;i >= top2; i--)
            {
                cout << arr[i];
                cout << "\n";
            }
        }
    }
};

// Driver program
int main()
{
    twoStacks ts(5);
    ts.push1(5);
    ts.push2(10);
    ts.push2(15);
    ts.push1(11);
    ts.push2(7);
    ts.displayStack1();
    ts.displayStack2();
    cout << "Poped element from stack1 is " << ts.pop1();
    ts.push2(40);
    cout << "\nPoped element from stack2 is " << ts.pop2();
    return 0;
}
