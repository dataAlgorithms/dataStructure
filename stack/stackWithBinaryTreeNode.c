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

// Driver program
int main()
{
    struct Stack *stack = createStack();
    printf("\nthe stack is empty?%d", isEmptyStack(stack));

    push(stack, newTreeNode(10));
    push(stack, newTreeNode(20));
    push(stack, newTreeNode(30));

    printStack(stack);
    printf("\n%d poped from stack", pop(stack));
    printf("\nthe stack is empty?%d", isEmptyStack(stack));
    printf("\nthe top of stack is %d", top(stack)->data);
    printStack(stack);
    
    destroyStack(stack);
    printStack(stack);
	    
    return 0;
}
