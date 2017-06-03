
#include <stdio.h>
#include <stdlib.h>

/*
Question:
Add two numbers represented by linked lists

Example 1
Input:
  First List: 5->6->3  // represents number 365
  Second List: 8->4->2 //  represents number 248
Output
  Resultant list: 3->1->6  // represents number 613

Example 2
Input:
  First List: 7->5->9->4->6  // represents number 64957
  Second List: 8->4 //  represents number 48
Output
  Resultant list: 5->0->0->5->6  // represents number 65005

Solution:
Traverse both lists. One by one pick nodes of both lists and add the values. 
If sum is more than 10 then make carry as 1 and reduce sum.
If one list has more elements than the other then consider remaining values of this list as 0.

Refer:
http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
*/

/* Linked list node */
struct node
{
    int data;
    struct node *next;
};

/* Function to create a new node with given data*/
struct node *newNode(int data)
{
    struct node *new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

/* Function to insert a node at the beginning of the Linked list*/
void push(struct node** head_ref, int new_data)
{
    /*allocate node*/
    struct node* new_node = newNode(new_data);

    /*link the old list off the new node*/
    new_node->next = (*head_ref);

    /*move the head to point to the new node*/
    (*head_ref) = new_node;
}

// Free list
void freeList(struct node* head)
{
    struct node* tmp;

    while (head != NULL)
    {
        tmp = head;
        head = head->next;
        free(tmp);
    }
}

/* Adds contents of two linked lists and return the head node of the resulttant list*/
struct node* addTwoLists (struct node* first, struct node* second)
{
    struct node* res = NULL; // res is head node of the resultant list
    struct node* temp, *prev = NULL;
    int carry = 0, sum;

    while (first != NULL || second != NULL)
    {
        //Calculate vlaue of next digit in resultant list
        //The next digit is sum of following things
        //(i) Carray
        //(ii) Next digit of first list (if there is a next digit)
        //(ii) Next digit of second list (if there is a next digit)
        sum = carry + (first?first->data: 0) + (second?second->data:0);

        // update carry for next calculation
        carry = (sum >= 10)? 1: 0;

        //Update sum if it is greater than 10
        sum = sum % 10;

        //Create a new node with sum as data
        temp = newNode(sum);

        //if this is the first node then set it as head of the resultant list
        if (res == NULL)
            res = temp;
        else // If this is not the first node then connect it to the rest
            prev->next = temp;

        //Set prev for next insertion
        prev = temp;

        //Move first and second pointers to next nodes
        if (first) first = first->next;
        if (second) second = second->next;
    }

    if (carry > 0)
        temp->next = newNode(carry);

    //return head of the resultant list
    return res;
}

// A utility function to print a linked list
void printList(struct node *node)
{
    while(node != NULL)
    {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

/* Driver program to test above function*/
int main(void)
{
    struct node* res = NULL;   
    struct node* first = NULL;
    struct node* second = NULL;

    //Create first list 7->5->9->4->6
    push(&first, 6);
    push(&first, 4);
    push(&first, 9);
    push(&first, 5);
    push(&first, 7);
    printf("First list is ");
    printList(first);

    //Create second list 8->4
    push(&second, 4);
    push(&second, 8);
    printf("Second list is ");
    printList(second);

    //Add the two lists and see result
    res = addTwoLists(first, second);
    printf("Resultant list is ");
    printList(res);

    freeList(first);
    freeList(second);
    freeList(res);

    res = NULL;   
    first = NULL;
    second = NULL;

    //Create first list 5->6->3
    push(&first, 3);
    push(&first, 6);
    push(&first, 5);
    printf("First list is ");
    printList(first);

    //Create second list 2->4->8
    push(&second, 2);
    push(&second, 4);
    push(&second, 8);
    printf("Second list is ");
    printList(second);

    //Add the two lists and see result
    res = addTwoLists(first, second);
    printf("Resultant list is ");
    printList(res);

    freeList(first);
    freeList(second);
    freeList(res);

    return 0;
}

/*
Result is as follow:

First list is 7 5 9 4 6 
Second list is 8 4 
Resultant list is 5 0 0 5 6 
First list is 5 6 3 
Second list is 8 4 2 
Resultant list is 3 1 6 
*/




/*
Given two numbers represented by two linked lists, 
write a function that returns sum list. The sum list is linked list representation of
 addition of two input numbers. It is not allowed to modify the lists. 
Also, not allowed to use explicit extra space 
(Hint: Use Recursion).

Example

Input:
  First List: 5->6->3  // represents number 563
  Second List: 8->4->2 //  represents number 842
Output
  Resultant list: 1->4->0->5  // represents number 1405

Following are the steps.
1) Calculate sizes of given two linked lists.
2) If sizes are same, then calculate sum using recursion. Hold all nodes in 
recursion call stack till the rightmost node, calculate sum of rightmost nodes and forward carry to left side.
3) If size is not same, then follow below steps:
….a) Calculate difference of sizes of two linked lists. Let the difference be diff
….b) Move diff nodes ahead in the bigger linked list. Now use step 2 to calculate sum
 of smaller list and right sub-list (of same size) of larger list. Also, store the carry of this sum.
….c) Calculate sum of the carry (calculated in previous step) with the remaining left sub-list 
of larger list. Nodes of this sum are added at the beginning of sum list obtained previous step.

*/
// A recursive program to add two linked lists
#include <stdio.h>
#include <stdlib.h>

// A linked list Node
struct node
{
    int data;
    struct node* next;
};

typedef struct node node;

/* A utility function to insert a node at the 
beginning of linked list*/
void push(struct node** head_ref, int new_data)
{
    /*allocate node*/
    struct node* new_node = (struct node*)malloc(sizeof(struct node));

    /*put in the data*/
    new_node->data = new_data;

    /*link the old list off the new node*/
    new_node->next = (*head_ref);

    /*move the head to point to the new node*/
    (*head_ref) = new_node;
}

/* A utility function to print linked list*/
void printList(struct node *node)
{
    while (node != NULL)
    {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

/* A utility function to swap two  pointers*/
void swapPointer(node** a, node **b)
{
    node *t = *a;
    *a = *b;
    *b = t;
}

/* A utility function to get size of linked list*/
int getSize(struct node *node)
{
    int size = 0;
    while (node != NULL)
    {
        node = node->next;
        size++;
    }
    return size;
}

/* Adds two linked lists of same size represented by head1 and 
head2 and returns head of the resultant linked list.
Carry is propagated while returning from the recursion
*/
node* addSameSize(node* head1, node* head2, int* carry)
{
    /* Since the function assumes linked list are of same size
       check any of the two head pointers
    */
    if (head1 == NULL)
        return NULL;

    int sum;

    // Allocate memory for sum node of current two nodes
    node* result = (node *)malloc(sizeof(node));

    // Recursively add remaining nodes and get the carry
    result->next = addSameSize(head1->next, head2->next, carry);

    // add digits of current nodes and propagated carry
    sum = head1->data + head2->data + *carry;
    *carry = sum / 10;
    sum = sum % 10;

    //Assign the sum to current node of resultant list
    result->data = sum;

    return result;
}

/* This function is called after the smaller list is added to the bigger
lists's sublist of same size. Once the right sublist is added, the carry
must be added to left size of larger list to get the final result
*/
void addCarryToRemaining(node* head1, node* cur,  int* carry, node** result)
{
    int sum;

    // If diff, number of nodes are not traversed, add carry
    if (head1 != cur)
    {
        addCarryToRemaining(head1->next, cur, carry, result);
        sum = head1->data + *carry;
        *carry = sum /10;
        sum %= 10;

        //add this node to the front of the result
        push(result, sum);
    }
}

/* The main function that adds two lined lists represented by head1 and head2
the sum of two lists is stored in a list referred by result
*/
void addList(node* head1, node* head2, node** result)
{
    node *cur;

    //first list is empty
    if (head1 == NULL)
    {
        *result = head2;
        return;
    }

    //second list is empty
    else if (head2 == NULL)
    {
        *result = head1;
        return;
    }

    int size1 = getSize(head1);
    int size2 = getSize(head2);
    int carry = 0;

    //Add same size lists
    if (size1 == size2)
        *result = addSameSize(head1, head2, &carry);
    else
    {
        int diff = abs(size1 - size2);

        /* First list should always be larget than second list
        if not , swap pointers
        */
        if (size1 < size2)
            swapPointer(&head1, &head2);

        //Move diff, number of nodes in first list
        for (cur = head1; diff--; cur = cur->next);

        //get addition of same size lists
        *result = addSameSize(cur, head2, &carry);

        //get addition of remaining first list and carry
        addCarryToRemaining(head1, cur, &carry, result);
    }

    //If some is still there, add a new node to the front of
    // the result list
    if (carry)
        push(result, carry);
}

//Diver program
int main()
{
    node *head1 = NULL, *head2 = NULL, *result = NULL;

    int arr1[] = {9, 9, 9};
    int arr2[] = {1, 8};

    int size1 = sizeof(arr1) / sizeof(arr1[0]);
    int size2 = sizeof(arr2) / sizeof(arr2[0]);

    // Create first list 
    int i;
    for (i = size1-1; i >= 0; --i)
        push(&head1, arr1[i]);

    // Create second list
    for (i = size2-1; i >= 0; --i)
        push(&head2, arr2[i]);

    addList(head1, head2, &result);

    printList(result);

    int arr3[] = {5, 6, 3};
    int arr4[] = {8, 4, 2};
    head1 = NULL;
    head2 = NULL;
    result = NULL;

    size1 = sizeof(arr3) / sizeof(arr3[0]);
    size2 = sizeof(arr4) / sizeof(arr4[0]);

    // Create first list 
    for (i = size1-1; i >= 0; --i)
        push(&head1, arr3[i]);

    // Create second list
    for (i = size2-1; i >= 0; --i)
        push(&head2, arr4[i]);

    addList(head1, head2, &result);

    printList(result);

    return 0;
} 

/*
Output:

1  0  1  7
1 4 0 5
Time Complexity: O(m+n) where m and n are the sizes of given two linked lists.
*/
