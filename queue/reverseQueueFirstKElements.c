/*
Given an integer k and a queue of integers, how do you reverse the order of the first k
elements of the queue, leaving the other elements in the same relative order? 
For example, if k=4 and queue has the elements [10, 20, 30, 40, 50, 60, 70, 80, 90]; 
the output should be [40, 30, 20, 10, 50, 60, 70, 80, 90].

Time Complexity: 	
O(n)	

Space Complexity: 	
O(n)
*/

#include <stdio.h>
#include <stdlib.h>
#define bool int

/* ------------------------Stack Implemention-------------- */
// structure of a stack node
struct sNode
{
    char data;
    struct sNode *next;
};

// Function prototypes
void push(struct sNode** top_ref, int new_data);
int pop(struct sNode** top_ref);
bool isEmptyStack(struct sNode* top);
void printStack(struct sNode* top);

// Check the stack is empty or not
bool isEmptyStack(struct sNode* top)
{
    return (top == NULL) ? 1: 0;
}

// Push an item to stack
void push(struct sNode** top_ref, int new_data)
{
    // allocate node
    struct sNode* new_node = 
       (struct sNode*) malloc(sizeof(struct sNode));

    if (new_node == NULL)
    {
         printf("Stack overflow\n");
         exit(0);
    }

    // put in the data
    new_node->data = new_data;

    //link the old list off the new node
    new_node->next = (*top_ref);

    //move the head to point to the new node
    (*top_ref) = new_node;
}

// Pop an item from stack
int pop(struct sNode** top_ref)
{
    char res;
    struct sNode *top;

    // If stack is empty then error
    if (*top_ref == NULL)
    {
        printf("Stack overflow\n");
        exit(0);
    }
    else
    {
        top = *top_ref;
        res = top->data;
        *top_ref = top->next;
        free(top);
        return res;
    }
}

// Print a linked list
void printStack(struct sNode* top)
{
    printf("\n");
	struct sNode* head = top;
    while (head != NULL)
    {
        printf(" %d ", head->data);
        head = head->next;
    }
}

/* ---------------------Queue Implementation----------------------*/
// A C program to demonstrate linked list based implementation of queue
 
// A linked list (LL) node to store a queue entry
struct QNode
{
    int key;
    struct QNode *next;
};
 
// The queue, front stores the front node of LL and rear stores ths
// last node of LL
struct Queue
{
    struct QNode *front, *rear;
};
 
// A utility function to create a new linked list node.
struct QNode* newNode(int k)
{
    struct QNode *temp = (struct QNode*)malloc(sizeof(struct QNode));
    temp->key = k;
    temp->next = NULL;
    return temp; 
}
 
// A utility function to create an empty queue
struct Queue *createQueue()
{
    struct Queue *q = (struct Queue*)malloc(sizeof(struct Queue));
    q->front = q->rear = NULL;
    return q;
}
 
// The function to add a key k to q
void enQueue(struct Queue *q, int k)
{
    // Create a new LL node
    struct QNode *temp = newNode(k);
 
    // If queue is empty, then new node is front and rear both
    if (q->rear == NULL)
    {
       q->front = q->rear = temp;
       return;
    }
 
    // Add the new node at the end of queue and change rear
    q->rear->next = temp;
    q->rear = temp;
}
 
// Function to remove a key from given queue q
struct QNode *deQueue(struct Queue *q)
{
    // If queue is empty, return NULL.
    if (q->front == NULL)
       return NULL;
 
    // Store previous front and move front one node ahead
    struct QNode *temp = q->front;
    q->front = q->front->next;
 
    // If front becomes NULL, then change rear also as NULL
    if (q->front == NULL)
       q->rear = NULL;
    return temp;
}

// Check queue is empty
int isEmptyQueue(struct Queue *q) 
{
    if (q->front == NULL)
        return 1;
    else
        return 0;
}

void printQueue(struct Queue *q)
{
    printf("\n");
	struct QNode *head = q->front; 
    while (head != NULL)
    {
        printf(" %d ", head->key);
        head = head->next;
    }
}

int sizeQueue(struct Queue *q)
{

    int count = 0;
    printf("\n");
	  struct QNode *head = q->front; 
    while (head != NULL)
    {
        count += 1;
        head = head->next;
    }
    
    return count;
}      

void interLeavingQueue(struct Queue *q) {
    if (sizeQueue(q) % 2 != 0)
        return;

    struct sNode *s = NULL;
    int halfSize = sizeQueue(q) / 2;
    int i;
    for (i = 0; i < halfSize; i++)
        push(&s, deQueue(q)->key);
    while (!isEmptyStack(s))
        enQueue(q, pop(&s));
    for (i = 0; i < halfSize; i++)
        enQueue(q, deQueue(q)->key);
    for (i = 0; i < halfSize; i++)
        push(&s, deQueue(q)->key);
    while (!isEmptyStack(s)) {
        enQueue(q, pop(&s));
        enQueue(q, deQueue(q)->key);
    }
}

void reverseQueueFirstKElements(int k, struct Queue *q) {
    if (q == NULL || k > sizeQueue(q)) {
        return;
    }
    else if (k > 0) {
        struct sNode *s = NULL;
        int i;
        for (i = 0; i < k; i++) {
            push(&s, deQueue(q)->key);
        }

        while (!isEmptyStack(s)) {
            enQueue(q, pop(&s));
        }

        for (i = 0; i < sizeQueue(q) -k; i++) {
            enQueue(q, deQueue(q)->key);
        }
    }
}


// Driver program
int main()
{
    struct Queue *q = createQueue();
    enQueue(q, 11);
    enQueue(q, 12);
    enQueue(q, 13);
    enQueue(q, 14);
    enQueue(q, 15);
    enQueue(q, 16);
    enQueue(q, 17);
    enQueue(q, 18);
    enQueue(q, 19);
    enQueue(q, 20);
    printQueue(q);

    reverseQueueFirstKElements(4, q);
    printQueue(q);
    
    return 0;
}
