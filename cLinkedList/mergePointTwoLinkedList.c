/*
Question:
 Get the merging point of two linked list

Algorithms:
1) Get count of the nodes in first list, let count be c1.
2) Get count of the nodes in second list, let count be c2.
3) Get the difference of counts d = abs(c1 – c2)
4) Now traverse the bigger list from the first node till d nodes 
so that from here onwards both the lists have equal no of nodes.
5) Then we can traverse both the lists in parallel till we come 
across a common node. (Note that getting a common node is done 
by comparing the address of the nodes)

Time Complexity: O(m+n)
Auxiliary Space: O(1)
*/

#include <stdio.h>
#include <stdlib.h>

/* link list node */
struct Node
{
    int data;
    struct Node* next;
};

/* get the counts of node in a linked list */
int getCounts(struct Node* head);

/* get the intersection point of two linked lists
head1 and head2 wherre head1 has d more nodes than head2*/
int _getIntersectionNode(int d, struct Node* head1, struct Node* head2);

/* get the intersection point of two linked lists head1 and head2 */
int getIntersectionNode(struct Node *head1, struct Node *head2)
{
    int c1 = getCounts(head1);
    int c2 = getCounts(head2);
    int d;

    if (c1 > c2)
    {
        d = c1 - c2;
        return _getIntersectionNode(d, head1,  head2);
    }
    else
    {
        d = c2 - c1;
        return _getIntersectionNode(d, head2, head1);
    }
}

/* get the intersection point of two linked lists
head1 and head2 where head1 has d more nodes than head2 */
int _getIntersectionNode(int d, struct Node* head1, struct Node* head2)
{
    int i;
    struct Node* current1 = head1;
    struct Node* current2 = head2;

    for (i = 0; i < d; i++)
    {
        if (current1 == NULL)
        {
            return -1;
        }

        current1 = current1->next;
    }

    while (current1 != NULL && current2 != NULL)
    {
        if (current1 == current2)
            return current1->data;

        current1 = current1->next;
        current2 = current2->next;
    }

    return -1;
}

// get the count of nodes in the list
int getCounts(struct Node* head)
{
    struct Node* current = head;
    int count = 0;

    while (current != NULL)
    {
        count += 1;
        current = current->next;
    }

    return count;
}

// Driver program
int main()
{
    /* 
    Create two linked lists

    lst 3->6->9->15->30
    2nd 10->15->30

    15 is the intersection point
    */

    struct Node* newNode;
    struct Node* head1 = 
        (struct Node*)malloc(sizeof(struct Node));
    head1->data = 10;

    struct Node* head2 = 
        (struct Node*)malloc(sizeof(struct Node));
    head2->data = 3;

    newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = 6;
    head2->next = newNode;

    newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = 9;
    head2->next->next = newNode;

    newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = 15;
    head1->next = newNode;
    head2->next->next->next = newNode;

    newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = 30;
    head1->next->next = newNode;

    head1->next->next->next = NULL;

    printf("\n Intersection node is %d \n", 
                getIntersectionNode(head1, head2));

    return 0;
}
