//Method One

/*
Question:
 Implement stack using queue. 

Algorithms:
 We start with an empty queue. For the push operation we simply insert the value to 
be pushed into the queue. The pop operation needs some manipulation. When we need to 
pop from the stack (simulated with a queue), first we get the number of elements in the
 queue, say n, and remove (n-1) elements from the queue and keep on inserting in the queue 
one by one. That is, we remove the front element from the queue, and immediately insert into 
the queue in the rear, then we remove the front element from the queue and then immediately 
insert into the rear, thus we continue upto (n-1) elements. Then we will perform a remove operation, 
which will actually remove the nth element of the original state of the queue, and return.
 Note that the nth element in the queue is the one which was inserted last, and we are returning 
it first, therefore it works like a pop operation (Last in First Out).

*/
#include <stdio.h>
#include <stdlib.h>

/* Queue structure */
#define QUEUE_EMPTY_MAGIC 0xdeadbeef
typedef struct _queue_t {
    int *arr;
    int rear, front, count, max;
} queue_t;

/* Queue operation function prototypes */
queue_t *queue_allocate(int n);
void queue_insert(queue_t * q, int v);
int queue_remove(queue_t * q);
int queue_count(queue_t * q);
int queue_is_empty(queue_t * q);

/* Note: here is the stuff we are interested in */
/* Simulated stack operations START */

/* Note: passing the queue object on which we will only operate the
   queue operations*/
void stack_push(queue_t *q, int v) {
    queue_insert(q, v);
}

int stack_pop(queue_t * q) {
    int i, n = queue_count(q);
    int removed_element;

    for (i = 0; i < (n - 1); i++) {
        removed_element = queue_remove(q);
        queue_insert(q, removed_element);
        /* same as below */
        //queue_insert(q, queue_remove(q))
    }
    removed_element = queue_remove(q);

    return removed_element;
}

int stack_is_empty(queue_t * q) {
    return queue_is_empty(q);
}

int stack_count(queue_t * q) {
    return queue_count(q);
}

/* Simulated stack  operations END */

/* Queue operations START */
int queue_count(queue_t *q) {
    return q->count;
}

queue_t *
queue_allocate(int n) {
    queue_t *queue;

    queue = malloc(sizeof(queue_t));
    if (queue == NULL)
        return NULL;

    queue->max = n;

    queue->arr = malloc(sizeof(int) * n);
    queue->rear = n - 1;
    queue->front = n - 1;

    return queue;
}

void queue_insert(queue_t * q, int v) {
    if (q->count == q->max)
        return;

    q->rear = (q->rear + 1) % q->max;
    q->arr[q->rear] = v;
    q->count++;
}

int queue_remove(queue_t * q) {
    int retval;

    /* magic number if queue is empty */
    if (q->count == 0)
        return QUEUE_EMPTY_MAGIC;

    q->front = (q->front + 1) % q->max;
    retval = q->arr[q->front];
    q->count--;

    return retval;
}

int queue_is_empty(queue_t * q) {
    return (q->count == 0);
}

/* Queue operations END */

/* For demo */
void queue_display(queue_t * q) {
    int i = (q->front + 1) % q->max, elements=queue_count(q);

    while (elements--) {
        printf("[%d], ", q->arr[i]);
        i = (i >= q->max) ? 0: (i + 1);
    }
}

#define MAX 128
int main(void) {
    queue_t *q;
    int x, select;

    /* Static allocation */
    q = queue_allocate(MAX);

    do {
        printf("\n[1] Push\n[2] Pop\n[0] Exit");
        printf("\nChoice: ");
        scanf(" %d", &select);

        switch (select) {
            case 1:
                printf("\nEnter value to push:");
                scanf(" %d", &x);
                /* Pushing */
                stack_push(q, x);
                printf("\n\n--------\nCurrent Queue:\n");
                queue_display(q);
                printf("\n\nPushed value: %d", x);
                printf("\n---------------\n");
                break;
            case 2:
                /* Popping */
                x = stack_pop(q);

                printf("\n\n\n\n-------\nCurrent Queue:\n");
                queue_display(q);
                if (x == QUEUE_EMPTY_MAGIC)
                    printf("\n\nNo vaues removed");
                else
                    printf("\n\nPopped value: %d", x);

                printf("\n--------------\n");
                break;
            case 0:
                printf("\nQutting.\n");
                return 0;

            default:
                printf("\nQutting.\n");
                return 0;
        }
    } while (1);

    return 0;
}


// Method Two
/*
push(s, x) // x is the element to be pushed and s is stack
  1) Enqueue x to q2
  2) One by one dequeue everything from q1 and enqueue to q2.
  3) Swap the names of q1 and q2 
// Swapping of names is done to avoid one more movement of all elements 
// from q2 to q1. 

pop(s)
  1) Dequeue an item from q1 and return it.
*/

// Method Three
/*
push(s,  x)
  1) Enqueue x to q1 (assuming size of q1 is unlimited).

pop(s)  
  1) One by one dequeue everything except the last element from q1 and enqueue to q2.
  2) Dequeue the last item of q1, the dequeued item is result, store it.
  3) Swap the names of q1 and q2
  4) Return the item stored in step 2.
// Swapping of names is done to avoid one more movement of all elements 
// from q2 to q1.
*/

// Method Four
struct Stack {
    struct Queue *Q1;
    struct Queue *Q2;
}

/*
Push operation Algorithm:
 Insert the element in whichever queue is not empty
   check whether queue Q1 is empty or not, if Q1 is empty then enqueue the element into Q2
   otherwise Enqueue the element into Q1
*/
void Push(struct Stack *S, int data) {
    if (IsEmptyQueue(S->Q1))
        EnQueue(S->Q2, data);
    else
        EnQueue(S->Q1, data);
}

/*
Pop operation algorithms:
 Transfer n-1 elements to the other queue and delete last from queue for performing pop operation
  If queue Q1 is not empty then transfer n-1 elements from Q1 to Q2 and then, DeQueue the last element of Q1 and return it
  If queue Q2 is not empty then transfer n-1 elements from Q2 to Q1 and then, DeQueue the last
element of Q2 and return it
*/
int Pop(struct Stack *S) {
    int i, size;
    if (IsEmptyQueue(S->Q2)) {
        size = Size(S->Q1);
        i = 0;
        while (i < size -1) {
            EnQueue(S->Q2, DeQeueue(S->Q1));
            i++;
        }
        return DeQueue(S->Q1);
    }
    else {
        size = Size(S->Q2);
        while (i < size-1) {
            EnQueue(S->Q1, DeQueeu(S->Q2));
            i++;
        }
        return DeQueue(S->Q2);
    }
}
