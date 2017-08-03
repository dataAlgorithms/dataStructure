#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#define bool int

struct binaryTreeNode
{
    int data;
    struct binaryTreeNode *left;
    struct binaryTreeNode *right;
};

struct binaryTreeNode *newTreeNode(int data)
{
    // Allocate memory for new node
    struct binaryTreeNode *node = (struct binaryTreeNode*)malloc(sizeof(struct binaryTreeNode));

    // Assign data to the node
    node->data = data;

    // Initialize left and right children as NULL
    node->left = NULL;
    node->right = NULL;

    return node;
}

// A linked list (LL) node to store a queue entry
struct queueNode
{
    struct binaryTreeNode *key;
    struct queueNode *next;
};
 
// The queue, front stores the front node of LL and rear stores ths
// last node of LL
struct Queue
{
    struct queueNode *front, *rear;
};
 
// A utility function to create a new linked list node.
struct queueNode* newQueueNode(struct binaryTreeNode *k)
{
    struct queueNode *temp = (struct queueNode*)malloc(sizeof(struct queueNode));
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
void enQueue(struct Queue *q, struct binaryTreeNode *k)
{
    // Create a new LL node
    struct queueNode *temp = newQueueNode(k);
 
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
struct binaryTreeNode *deQueue(struct Queue *q)
{
    // If queue is empty, return NULL.
    if (q->front == NULL)
       return NULL;
 
    // Store previous front and move front one node ahead
    struct binaryTreeNode *temp = q->front->key;
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
	struct queueNode *head = q->front; 
    while (head != NULL)
    {
        printf(" %d ", head->key->data);
        head = head->next;
    }
}

int sizeQueue(struct Queue *q)
{

    int count = 0;
    printf("\n");
	struct queueNode *head = q->front; 
    while (head != NULL)
    {
        count += 1;
        head = head->next;
    }
    
    return count;
}      

//Get the front node of queue
int queueFront(struct Queue *q) 
{
    if (q->front == NULL)
        return INT_MIN;
        
    return q->front->key->data;
}

//Get the rear node of queue
int queueRear(struct Queue *q) 
{
    if (q->rear == NULL)
        return INT_MIN;
        
    return q->rear->key->data;
}

//Clear the queue
int clearQueue(struct Queue *q)
{
    struct queueNode *p = NULL;
    while(q->front){
        p = q->front;
        q->front = q->front->next;
        free(p);
    }
    return 0;
}

//Destroy the queue
int destroyQueue(struct Queue *q)
{
    clearQueue(q);
    q = NULL;
    return 0;
}

// Driver program
int main()
{
    struct Queue* queue = createQueue();
 
    enQueue(queue, newTreeNode(10));
    enQueue(queue, newTreeNode(20));
    enQueue(queue, newTreeNode(30));
    enQueue(queue, newTreeNode(40));
    
    printQueue(queue);
    printf("\n%d dequeued from queue", deQueue(queue)->data);
    printQueue(queue); 
    printf("\nFront item is %d", queueFront(queue));
    printf("\nRear item is %d", queueRear(queue));
    
    destroyQueue(queue);
    printQueue(queue);
    
    return 0;
}
