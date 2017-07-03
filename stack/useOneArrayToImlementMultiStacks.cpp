/*
Question:
Create a data structure kStacks that represents k stacks. 
Implementation of kStacks should use only one array, i.e., 
k stacks should use the same array for storing elements. 
Following functions must be supported by kStacks.

push(int x, int sn) –> pushes x to stack number ‘sn’ where sn is from 0 to k-1
pop(int sn) –> pops an element from stack number ‘sn’ where sn is from 0 to k-1

Algorithms:
The idea is to use two extra arrays for efficient implementation of k 
stacks in an array. This may not make much sense for integer stacks, but
 stack items can be large for example stacks of employees, students, etc 
where every item is of hundreds of bytes. For such large stacks, the extra 
space used is comparatively very less as we use two integer arrays as extra space.

Following are the two extra arrays are used:
1) top[]: This is of size k and stores indexes of top elements in all stacks.
2) next[]: This is of size n and stores indexes of next item for the items in array arr[].
 Here arr[] is actual array that stores k stacks.
Together with k stacks, a stack of free slots in arr[] is also maintained. The top of
 this stack is stored in a variable ‘free’.

All entries in top[] are initialized as -1 to indicate that all stacks are empty. All entries 
next[i] are initialized as i+1 because all slots are free initially and pointing to next slot. 
Top of free stack, ‘free’ is initialized as 0.

Time complexity:
push() and pop() is O(1).

Output:
Pop from stack 2 is 45
Pop from stack 1 is 39
Pop from stack 0 is 7
*/

#include <iostream>
#include <climits>
using namespace std;

// a class to represent k stacks in a single array of size n
class kStacks
{
    int *arr; // array of size n to store actual content to be stored in stacks
    int *top; // array of size k to store indexes of top elements of stacks
    int *next; // array of size n to store next entry in all stacks and free list
    int n, k;
    int free;  // store beginning index of free list
public:
    // constructor to create  stacks  in an array of size n
    kStacks(int k, int n);

    // A utility function to check there is apce availale
    bool isFull() {return (free == -1);}

    // Push an item in stack number sn where sn is from 0 to k-1
    void push(int item, int sn);

    // Pop an item from stack number sn where sn is from 0 to k-1
    int pop(int sn);

    // check whether stack number sn is empty or not
    bool isEmpty(int sn) {return (top[sn] == -1);}
};

// constructor to create k stacks in an array of size n
kStacks::kStacks(int k1, int n1)
{
    // Initialize n and k, and allocate memory for all arrays
    k = k1, n = n1;
    arr = new int[n];
    top = new int[k];
    next = new int[n];

    // Initialize stacks as empty
    for (int i=0; i < k; i++)
        top[i] = -1;

    // Initialize all spaces as free
    free = 0;
    for (int i=0; i<n-1; i++)
        next[i] = i+1;
    next[n-1]  = -1; // -1 is used to indicate end of free list
}

// push an item in stack number sn where sn is frm 0 to k-1
void kStacks::push(int item, int sn)
{
    // Overflow check
    if (isFull())
    {
        cout << "\nStack overflow\n";
        return;
    }

    int i = free; // Store index of first free slot

    // Update index of free slot to index of next slot in free list
    free = next[i];

    // Update next of top and then top for stack number sn
    next[i] = top[sn];
    top[sn] = i;

    // Put the item in array
    arr[i] = item;
}

// Pop an item from stack number sn where sn is from 0 to k-1
int kStacks::pop(int sn)
{
    // Underflow check
    if (isEmpty(sn))
    {
        cout << "\nStack Underflow\n";
        return INT_MAX;
    }

    // Find index of top item in stack number sn
    int i = top[sn];

    top[sn] = next[i];  // Change top to store next of previous top

    // Attach the previous top to the begining of free list
    next[i] = free;
    free = i;

    // Return the previous top item
    return arr[i];
}

// Driver program
int main()
{
    // create 3 stacks in an array of size 10
    int k = 3, n= 10;
    kStacks ks(k, n);

    // Let us put some items in stack number 2
    ks.push(15, 2);
    ks.push(45, 2);

    // Let us put some item in stack number 1
    ks.push(17, 1);
    ks.push(49, 1);
    ks.push(39, 1);

    // Let us put some items in stack number 0
    ks.push(11, 0);
    ks.push(9, 0);
    ks.push(7, 0);

    cout << "Pop from stack 2 is " << ks.pop(2) << endl;
    cout << "Pop from stack 1 is " << ks.pop(1) << endl;
    cout << "Pop from stack 0 is " << ks.pop(0) << endl;

    return 0;
}