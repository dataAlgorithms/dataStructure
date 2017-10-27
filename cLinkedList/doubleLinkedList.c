#include <stdio.h>
#include <stdlib.h>

struct DLLNode {
    int data;
    struct DLLNode *next;
    struct DLLNode *prev;
};

//Double Linked list insert
/*
Time Complexity: O(n). In the worst case, we may need to 
               insert the node at the end of the list.
Space Complexity: O(1), for creating one temporary variable.
*/
void DLLInsert(struct DLLNode **head, int data, int position) {
    int k = 1;
    struct DLLNode *temp, *newNode;

    newNode = (struct DLLNode *)malloc(sizeof(struct DLLNode));
    if (!newNode) {
        printf("Memory Error");
        return;
    }

    newNode->data = data;
    //insert a node at the beginning
    if (position == 1) {
        newNode->next = *head;
        newNode->prev = NULL;

        if (*head)
            (*head)->prev = newNode;

        *head = newNode;
        return;
    }

    temp = *head;
    while ((k < position-1) && temp->next != NULL) {
        temp = temp->next;
        k++;
    }

    if (k != position) {
        printf("Desired position does not exist\n");
    }

    newNode->next = temp->next;
    newNode->prev = temp;

    if (temp->next)
        temp->next->prev=newNode;

    temp->next = newNode;
    return;
}

//Double linked list deletion
/*
Time Complexity: O(n), for scanning the complete list of size n.
Space Complexity: O(1), for creating one temporary variable.
*/
void DLLDelete(struct DLLNode **head, int position) {
    struct DLLNode *temp=*head, *temp2;
    int k = 1;

    if (*head == NULL) {
        printf("List is empty");
        return;
    }

    if (position == 1) {
        *head = (*head)->next;

        if (*head != NULL)
            (*head)->prev = NULL;
            free(temp);
            return;
    }

    while((k < position) && temp->next != NULL) {
        temp = temp->next;
        k++;
    }

    if (k != position-1) {
        printf("Desired position does not exist\n");
    }

    temp2 = temp->prev;
    temp2->next = temp->next;

    //Deletion from intermediate node
    if (temp->next)
        temp->next->prev = temp2;
    free(temp);
    return;
}
