//Method One

#include <stdio.h>
#include <stdlib.h>

/*
Question:
Implement queue with two user stacks

Algorithms:
enQueue(q,  x)
  1) Push x to stack1 (assuming size of stacks is unlimited).

deQueue(q)
  1) If both stacks are empty then error.
  2) If stack2 is empty
       While stack1 is not empty, push everything from stack1 to stack2.
  3) Pop the element from stack2 and return it.

Output:
1 2 3 
*/

// structure of a stack node
struct sNode
{
    int data;
    struct sNode *next;
};

// push an item to stack
void push(struct sNode** top_ref, int new_data);

// pop an item from stack
int pop(struct sNode** top_ref);

// structure of queue having two stacks
struct queue
{
    struct sNode *stack1;
    struct sNode *stack2;
};

// enqueue an item to queue
void enQueue(struct queue *q, int x)
{
    push(&q->stack1, x);
}

// dequeue an item from queue
int deQueue(struct queue *q)
{
    int x;

    //both stacks are empty then error
    if(q->stack1 == NULL && q->stack2 == NULL)
    {
        printf("Q is empty");
        exit(0);
    }

    //Move elements from stack1 to stack2 only if stack2 is empty
    if(q->stack2 == NULL)
    {
        while(q->stack1 != NULL)
        {
            x = pop(&q->stack1);
            push(&q->stack2, x);
        }
    }

    x = pop(&q->stack2);
    return x;
}

// push an item to stack
void push(struct sNode** top_ref, int new_data)
{
    // alocate node
    struct sNode* new_node = (struct sNode*) malloc(sizeof(struct sNode));
    if(new_node == NULL)
    {
        printf("Stack overflow\n");
        exit(0);
    }

    // put in the data
    new_node->data = new_data;

    // link the old list off the new node
    new_node->next = (*top_ref);

    // move the head to point to the new node
    (*top_ref) = new_node;          
}

// pop an item from stack
int pop(struct sNode** top_ref)
{
    int res;
    struct sNode *top;

    //If stack is empty then error
    if(*top_ref == NULL)
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

// driver function
int main()
{
    // create a queue with items 1 2 3
    struct queue *q = (struct queue*)malloc(sizeof(struct queue));
    q->stack1 = NULL;
    q->stack2 = NULL;
    enQueue(q, 1);
    enQueue(q, 2);
    enQueue(q, 3);

    // Dequeue items
    printf("%d ", deQueue(q));
    printf("%d ", deQueue(q));
    printf("%d ", deQueue(q));

    return 0;
}



//Method Two: 

/*
Queue:
Implement queue using two stacks

Algorithms:
Implemented using one user stack and one Function Call Stack. Below is modified Method 2 w
here recursion (or Function Call Stack) is used to implement queue using only one user defined stack.

enQueue(x)
  1) Push x to stack1.

deQueue:
  1) If stack1 is empty then error.
  2) If stack1 has only one element then return it.
  3) Recursively pop everything from the stack1, store the popped item 
    in a variable res,  push the res back to stack1 and return res

Output:
1 2 3
*/

#include <stdio.h>
#include <stdlib.h>

// structure of a stack node
struct sNode
{
    int data;
    struct sNode *next;
};

// structure of queue having two stacks
struct queue
{
    struct sNode *stack1;
};

// push an item to stack
void push(struct sNode** top_ref, int new_data);

// pop an item from stack
int pop(struct sNode** top_ref);

// enqueue an item to queue
void enQueue(struct queue *q, int x)
{
    push(&q->stack1, x);
}

// dequeue an item from queue
int deQueue(struct queue *q)
{
    int x, res;

    // both stacks are empty then error
    if (q->stack1 == NULL)
    {
        printf("Q is empty");
        exit(0);
    }
    else if (q->stack1->next == NULL)
    {
        return pop(&q->stack1);
    }
    else
    {
        // pop an item from the stack1
        x = pop(&q->stack1);

        // store the last dequeued item
        res = deQueue(q);

        // push everything back to stack1
        push(&q->stack1, x);
        return res;
    }
}

// push an item to stack
void push(struct sNode** top_ref, int new_data)
{
    // allocate node
    struct sNode* new_node = (struct sNode*)malloc(sizeof(struct sNode));

    if(new_node == NULL)
    {
        printf("Stack overflow\n");
        exit(0);
    }

    // put in the data
    new_node->data = new_data;

    // link the old list off the new node
    new_node->next = (*top_ref);

    // move the head to point to the new node
    (*top_ref) = new_node;
}

// pop an item from stack
int pop(struct sNode** top_ref)
{
    int res;
    struct sNode *top;

    // If stack is empty then error
    if(*top_ref == NULL)
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

// Driver program
int main()
{
    // Create a queue with items 1, 2, 3
    struct queue *q = (struct queue*)malloc(sizeof(struct queue));
    q->stack1 = NULL;

    enQueue(q, 1);
    enQueue(q, 2);
    enQueue(q, 3);

    // Dequeue items
    printf("%d ", deQueue(q));
    printf("%d ", deQueue(q));
    printf("%d ", deQueue(q));

    return 0;
}
