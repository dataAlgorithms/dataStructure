#include <stdio.h>
#include <stdlib.h>
#define bool int

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

// Recursive function that inserts an element 
// at the bottom of a stack
void insertAtBottom(struct sNode** top_ref, int item)
{
    if (isEmpty(*top_ref))
        push(top_ref, item);
    else
    {
        /*
        Hold all items in function call stack until we reach
        end of the stack. when the stack becomes empty, 
        the isEmpty(*top_ref) becomes true, the above if part is
        executed and the item is inserted at the bottom
        */
        int temp = pop(top_ref);
        insertAtBottom(top_ref, item);

        /*
        Once the item is inserted at the bottom, push all the items
        held in function call stack
        */
        push(top_ref, temp);
    }
}

// Reverse the given stack using insertAtBottom
void reverse(struct sNode** top_ref)
{
    if (!isEmpty(*top_ref))
    {
        /* Hold all items in function call stack until we
           reach end of the stack
        */
        int temp = pop(top_ref);
        reverse(top_ref);

        /* Insert all the items (held in function call stack)
           one by one from the bottom to top. Every item is
           inserted at the bottom*/
        insertAtBottom(top_ref, temp);
    }
}

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
    reverse(&s);
    printf("\n Reversed stack ");
    print(s);
    return 0;
}

