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
bool isEmpty(struct sNode* top);
void print(struct sNode* top);

// Check the stack is empty or not
bool isEmpty(struct sNode* top)
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
void print(struct sNode* top)
{
    printf("\n");
    while (top != NULL)
    {
        printf(" %d ", top->data);
        top = top->next;
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
int queueIsEmpty(struct Queue *q) 
{
    if (q->front == NULL)
        return 1;
    else
        return 0;
}

void printQueue(struct Queue *q)
{
    printf("\n");
    while (q->front != NULL)
    {
        printf(" %d ", q->front->key);
        q->front = q->front->next;
    }
}

void queueStack(struct Queue *q)
{
/*
Do
Delete an item from Q
Push the item to S
While (! empty Q); 

Do
Pop an item from S
Insert the item to Q
While (! empty S); 

Do
Delete an item from Q
Push the item to S
While (! empty Q); 
*/
    // init a stack
    struct sNode *s = NULL;
    int n;
    struct QNode *temp = NULL;;
    
    do {
        temp = deQueue(q);
        push(&s, temp->key);
    }while (!queueIsEmpty(q));
	
    do {
        n = pop(&s);
        enQueue(q, n);
    }while (!isEmpty(s));    
    
    do {
        temp = deQueue(q);
        push(&s, temp->key);
    }while (!queueIsEmpty(q));
    
    print(s);    
} 

// Driver program
int main()
{
    struct sNode *s = NULL;
    push(&s, 4);
    push(&s, 3);
    push(&s, 2);
    push(&s, 1);

    printf("\n Original stack ");
    print(s);

    printf("\n Original queue");

    struct Queue *q = createQueue();
    enQueue(q, 10);
    enQueue(q, 20);
    deQueue(q);
    deQueue(q);
    enQueue(q, 30);
    enQueue(q, 40);
    enQueue(q, 50);
    printQueue(q);

    queueStack(q);

    return 0;
}
