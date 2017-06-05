#include <stdio.h>
#include <stdlib.h>

/* Link list node*/
struct node
{
    int data;
    struct node* next;
};

void push(struct node** heaf_ref, int new_data);

/* 
This solution uses the temporary dummy to build up the result list

Method 1 (Using Dummy Node)
The strategy here uses a temporary dummy node as the start of the result list.
The pointer tail always points to the last node in the result list, so appending
new nodes is easy. The dummy node gives tail something to point to initially when
the result list is empty. This dummy node is efficient, since it is only temporary,
and it is allocated in the stack. The loop proceeds, removing one node from either a or b 
and adding it to tail. When we are done, the result is in dummy.next.

Time Complexity: 
 O(m+n)
*/
struct node* sortedIntersect(struct node* a, struct node* b)
{
    struct node dummy;
    struct node* tail = &dummy;
    dummy.next = NULL;

    /* Once one or the other list runs out -- we're done */
    while (a != NULL && b != NULL)
    {
        if (a->data == b->data)
        {
            push((&tail->next), a->data);
            tail = tail->next;
            a = a->next;
            b = b->next;
        }
        else if (a->data < b->data) /* advance the smaller list*/
            a = a->next;
        else
            b = b->next;
    }
    return (dummy.next);
}

/*
Method 2 (Using Local References)
This solution is structurally very similar to the above, but is avoids using 
a dummy node instead, it maintains a struct node** pointer, lastPtrRef,
that always points to the last  pointer of the result list.
This solves the same case that the dummy node did - dealing with the reslt list
when it is empty. If you are trying to build up a list at its tail, either
the dummy node or the struct node** reference strategy can be used

Time complexity:
 O(m+n)
*/
struct node* sortedIntersectLocalRef(struct node* a, struct node* b)
{
    struct node* result = NULL;
    struct node** lastPtrRef = &result;

    /* Advance comparing the first nodes in both lists.
    when one or the other list runs out, we're done.*/
    while (a != NULL && b != NULL)
    {
        if (a->data == b->data)
        {
            /* found a node for the intersection*/
            push(lastPtrRef, a->data);
            lastPtrRef = &((*lastPtrRef)->next);
            a = a->next;
            b = b->next;
        }    
        else if (a->data < b->data)
            a = a->next;
        else
            b = b->next;
    }
    return result;
}

/*
Method 3 (Recursive)

Recursive implementation of sortedIntersect

Time Complexity:
  O(m+n)
*/
struct node* sortedIntersectRec(struct node* a, struct node* b)
{
    /* base case */
    if (a == NULL || b == NULL)
        return NULL;
 
    /* If both lists are non-empty */
 
    /* advance the smaller list and call recursively */
    if (a->data < b->data)
        return sortedIntersectRec(a->next, b);
 
    if (a->data > b->data)
        return sortedIntersectRec(a, b->next);
 
    // Below lines are executed only when a->data == b->data
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = a->data;
 
    /* advance both lists and call recursively */
    temp->next = sortedIntersectRec(a->next, b->next);
    return temp;
}

/* function to insert a node at the beginning of the linked list*/
void  push(struct node** head_ref, int new_data)
{
    /* allocate node*/
    struct node* new_node = 
          (struct node*)malloc(sizeof(struct node));

    /* put in the data*/
    new_node->data = new_data;

    /* link the old list off the new node*/
    new_node->next = (*head_ref);

    /* move the head to point to the new node*/
    (*head_ref) = new_node;
}

/* to print nodes in a given linked list*/
void printList(struct node *node)
{
    while (node != NULL)
    {
        printf("%d ", node->data);
        node = node->next;
    }

    printf("\r");
}

/* Driver program */
int main()
{
    /* Start with the empty lists*/
    struct node* a = NULL;
    struct node* b = NULL;
    struct node* intersect = NULL;
    struct node* intersectLocalRef = NULL;
    struct node* intersectRec = NULL;

    int aList[] = {6, 5, 4, 3, 2, 1};
    int bList[] = {8, 6, 4, 2};
    int i;

    /* Create the first sorted linked list*/
    for (i = 0; i < sizeof(aList)/sizeof(aList[0]); i++)
    { 
        push(&a, aList[i]);
    }

    /* Create the second sorted linkd list*/
    for (i = 0; i < sizeof(bList)/sizeof(bList[0]); i++)
    {
        push(&b, bList[i]);
    }

    /* Find the intersection two linked lists*/
    intersect = sortedIntersect(a, b);
    intersectLocalRef = sortedIntersectLocalRef(a, b);
    intersectRec = sortedIntersectRec(a, b);

    printf("\nLinked list containing common item of a & b\n");
    printList(intersect);
    printList(intersectLocalRef);
    printList(intersectRec);

    return 0;   
}
