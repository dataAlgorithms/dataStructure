#include <stdio.h>
#include <stdlib.h>

/* 
linked list node of integer 
*/
struct ListNode {
    int data;
    struct ListNode *next;
};

// basic operation on a list

/* 
traversing the list
 Time: O(n) 
 Space: O(1)
*/
void listTraverse(struct ListNode *head) {

    struct ListNode *current = head;
    
    while (current != NULL) {
        print("%d ", current->data);
        current = current->next;
    }
    
}

/*
 get the length of the list
 Time: O(n) 
 Space: O(1)
*/
int listLength(struct ListNode *head) {
    struct ListNode *current = head;
    int count = 0;

    while (current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}

/* 
insert an item in the list

Time: O(n)
Space: O(1)
*/
void insertLinkedList(struct ListNode **head, int data, int position) {
    int k=1;
    struct ListNode *p, *q, *newNode;

    newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
    if (!newNode) {
        printf("Memory Error");
        return;
    }

    newNode->data = data;
    p=*head;

    // Insert at the beginning
    if(position == 1) {
        newNode->next = p;
        *head = newNode;
    }
    else {
        //Traverse the list until the position where we want to insert
        while((p!=NULL) && (k<position)) {
            k++;
            q=p;
            p=p->next;
        }
        q->next=newNode;
        newNode->next=p;
    }
}

/*
 delete an item from the list

Time: O(n)
Space: O(1)
*/
void deleteNodeFromLinkedList(struct ListNode **head, int position) {
    int k = 1;
    struct ListNode *p, *q;
    if(*head == NULL) {
        printf("List Empty");
        return;
    }

    p = *head;
    //from the beginning
    if (position == 1) {
        *head = (*head)->next;
        free(p);
        return;
    }
    else {
        //Traverse the list until arriving at the 
        // position from which we want to delete
        while ((p != NULL) && (k < position)) {
            k++;
            q = p;
            p = p->next;
        }
        if (p == NULL) // At the end
            printf("Positioin does not exist.");
        else {  //from the middle
            q->next = p->next;
            free(p);
        }
    }
}

/*
delete the linked list

Time: O(n)
Space: O(1)
*/
void deleteLinkedList(struct ListNode **head) {
    struct ListNode *auxilaryNode, *iterator;
    iterator = *head;
    while (iterator) {
        auxilaryNode = iterator->next;
        free(iterator);
        iterator = auxilaryNode;
    }
    *head = NULL;
}
