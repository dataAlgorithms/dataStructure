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

struct Stack 
{
    struct sNode *top;	
};

// Function prototypes
void push(struct Stack *s, int new_data);
int pop(struct Stack *s);
bool isEmptyStack(struct Stack *s);
void printStack(struct Stack *s);
struct sNode* stackNode(int k);
int peek(struct Stack *s);

// A utility function to create a new linked list node.
struct sNode* stackNode(int k)
{
    struct sNode *temp = (struct sNode*)malloc(sizeof(struct sNode));
    temp->data = k;
    temp->next = NULL;
    
    return temp; 
}

// Push an item to stack
void push(struct Stack *s, int new_data)
{
    // allocate node
    struct sNode *new_node = stackNode(new_data);

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
int pop(struct Stack *s)
{
    char res;
    struct sNode *top;
    
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
int peek(struct Stack *s)
{
    int res;
    struct sNode *top;
    
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
	struct sNode *top = s->top;
	
    while (top != NULL)
    {
        printf(" %d ", top->data);
        top = top->next;
    }
}

// A utility function to create an empty queue
struct Stack *createStack()
{
	struct Stack *s = (struct Stack*)malloc(sizeof(struct Stack));
    s->top = NULL;

    return s;
}


// Driver program
int main()
{
    struct Stack *stack = createStack();
    printf("\nthe stack is empty?%d", isEmptyStack(stack));

    push(stack, 10);
    push(stack, 20);
    push(stack, 30);

    printStack(stack);
    printf("\n%d poped from stack", pop(stack));
    printf("\nthe stack is empty?%d", isEmptyStack(stack));
    printf("\nthe top of stack is %d", peek(stack));
    printStack(stack);
    
    return 0;
}

/*
the stack is empty?1
 30  20  10
30 poped from stack
the stack is empty?0
the top of stack is 20
 20  10
 */
