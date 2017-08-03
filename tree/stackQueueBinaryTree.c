#include <stdio.h>
#include <stdlib.h>
#define bool int

/* ------------------------Stack Implemention-------------- */
// structure of a stack node
struct stackNode
{
    struct binaryTreeNode *data;
    struct stackNode *next;
};

struct Stack 
{
    struct stackNode *top;	
};

struct binaryTreeNode
{
    int data;
    struct binaryTreeNode *left;
    struct binaryTreeNode *right;
};

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
 
// Protocols
struct binaryTreeNode *newTreeNode(int);
struct stackNode* stackNode(struct binaryTreeNode *);
void push(struct Stack *, struct binaryTreeNode *);
bool isEmptyStack(struct Stack *);
struct binaryTreeNode *pop(struct Stack *);
struct binaryTreeNode *top(struct Stack *);
void printStack(struct Stack *);
struct Stack *createStack();
int clearStack(struct Stack *);
int destroyStack(struct Stack *);
struct queueNode* newQueueNode(struct binaryTreeNode *);
struct Queue *createQueue();
void enQueue(struct Queue *q, struct binaryTreeNode *);
struct binaryTreeNode *deQueue(struct Queue *);
int isEmptyQueue(struct Queue *);
void printQueue(struct Queue *);
int sizeQueue(struct Queue *);
int queueFront(struct Queue *);
int queueRear(struct Queue *); 
int clearQueue(struct Queue *);
int destroyQueue(struct Queue *);
void printPostorder(struct binaryTreeNode *);
void printPreorder(struct binaryTreeNode *);
void printLevelorder(struct binaryTreeNode *);
void printGivenLevel(struct binaryTreeNode *, int);
int height(struct binaryTreeNode *);

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

/* 
 newTreeNode allocates a new node with the given data
 and NULL left and right pointers
*/
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

// A utility function to create a new linked list node.
struct stackNode* stackNode(struct binaryTreeNode *k)
{
    struct stackNode *temp = (struct stackNode*)malloc(sizeof(struct stackNode));
    temp->data = k;
    temp->next = NULL;
    
    return temp; 
}

// Push an item to stack
void push(struct Stack *s, struct binaryTreeNode *new_data)
{
    // allocate node
    struct stackNode *new_node = stackNode(new_data);

    if (new_node == NULL)
    {
         printf("Stack overflow\n");
         exit(0);
    }

    // put in the data
    new_node->data = new_data;

    //link the old list off the new node
    new_node->next = s->top;

    //move the head to point to the new node
    s->top = new_node;
}

// Check the stack is empty or not
bool isEmptyStack(struct Stack *s)
{
    return (s->top == NULL) ? 1: 0;
}

// Pop an item from stack
struct binaryTreeNode *pop(struct Stack *s)
{
    struct binaryTreeNode *res;
    struct stackNode *top;
    
    // If stack is empty then error
    if (s->top == NULL)
    {
        printf("Stack overflow\n");
        exit(0);
    }
    else
    {
    	top = s->top;
        res = s->top->data;
        s->top = s->top->next;
        free(top);
        return res;
    }
}

// Return the top item
struct binaryTreeNode *top(struct Stack *s)
{
    struct binaryTreeNode *res;
    struct stackNode *top;
    
    // If stack is empty then error
    if (s->top == NULL)
    {
        printf("Stack overflow\n");
        exit(0);
    }
    else
    {

        res = s->top->data;
        return res;
    }
}

// Print a linked list
void printStack(struct Stack *s)
{
    printf("\n");
	struct stackNode *top = s->top;
	
    while (top != NULL)
    {
        printf(" %d ", top->data->data);
        top = top->next;
    }
}

// A utility function to create an empty stack
struct Stack *createStack()
{
	struct Stack *s = (struct Stack*)malloc(sizeof(struct Stack));
    s->top = NULL;

    return s;
}

//Clear the stack
int clearStack(struct Stack *s)
{
    struct stackNode *p = NULL;
    while(s->top){
        p = s->top;
        s->top = s->top->next;
        free(p);
    }
    return 0;
}

//Destroy the stack
int destroyStack(struct Stack *s)
{
    clearStack(s);
    s = NULL;
    return 0;
}

/*
 post order traversal of binary tree
*/
void printPostorder(struct binaryTreeNode *node)
{
    if (node == NULL)
        return;

    //first recur on left subtree
    printPostorder(node->left);

    //then recur on right subtree
    printPostorder(node->right);

    // deal with the node
    printf("%d ", node->data);
}

/*
 in order traversal of binary tree
*/
void printInorder(struct binaryTreeNode *node)
{
    if (node == NULL)
        return;

    //first recur on left subtree
    printInorder(node->left);

    //then deal with the node
    printf("%d ", node->data);

    //recur on right subtree
    printInorder(node->right);

}

/*
 pre order traversal of binary tree
*/
void printPreorder(struct binaryTreeNode *node)
{
    if (node == NULL)
        return;

    //deal with the node
    printf("%d ", node->data);

    //recur on left subtree
    printPreorder(node->left);

    //recur on right subtree
    printPreorder(node->right);


}

// print level order traversal a tree
void printLevelorder(struct binaryTreeNode *root)
{
    int h = height(root);
    int i;

    for (i=1; i<=h; i++)
        printGivenLevel(root, i);
}

// Print nodes at a given level
void printGivenLevel(struct binaryTreeNode *root, int level)
{
    if (root == NULL)
        return;

    if (level == 1)
        printf("%d ", root->data);
    else if (level > 1)
    {
        printGivenLevel(root->left, level-1);
        printGivenLevel(root->right, level-1);
    }
}

/* Compute the height of a tree -- the number of 
   nodes along the longest path from the root node
    down to the farthest leaf node*/
int height(struct binaryTreeNode *root)
{
    if (root == NULL)
        return 0;
    else 
    {
        // Compute the height of each subtree
        int lheight = height(root->left);
        int rheight = height(root->right);

        // Use the larger one
        if (lheight > rheight)
            return lheight+1;
        else
            return rheight+1;
    }
}

// Driver program
int main()
{
    // Create root
    struct binaryTreeNode *root = newTreeNode(1);
    root->left = newTreeNode(2);
    root->right = newTreeNode(3);

    root->left->left = newTreeNode(4);
    root->left->right = newTreeNode(5);

    printf("\nPreorder traversal of binary tree is \n");
    printPreorder(root);
 
    printf("\nInorder traversal of binary tree is \n");
    printInorder(root);  
 
    printf("\nPostorder traversal of binary tree is \n");
    printPostorder(root);

    printf("\nLevelorder traversal of binary tree is \n");
    printLevelorder(root);
    
    return 0;
}
