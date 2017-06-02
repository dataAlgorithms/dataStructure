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
