/*
Implement Double Ended Queue using Double Linked List

Output:
[root@newisscenter soft]# gcc dequeUsingDoubleLinkedList.c
[root@newisscenter soft]# ./a.out 
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:2
Enter ur data to insert:11
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:1
Enter the data to insert:10
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:2
Enter ur data to insert:12
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:1
Enter the data to insert:9
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:2
Enter ur data to insert:13
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:1
Enter the data to insert:8
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:2
Enter ur data to insert:14
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:1
Enter the data to insert:7
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:5
7  8  9  10 11 12 13 14 
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:4
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:4
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:4
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:5
7  8  9  10 11 
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:3
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:3
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:5
9  10 11 
1. Enqueue at front
2. Enqueue at rear
3. Dequeue at front
4. Dequeue at rear
5. Display
6. Exit
Enter you choice:6
*/

#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *prev, *next;
};

struct node *head = NULL, *tail = NULL;

struct node *createNode(int data) {
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data = data;
    newnode->next = newnode->prev = NULL;
    return newnode;
}

/*
create sentinel(dummy head & tail) that
helps us to do insertion and deletion
operation at front and rear so easily, And
these dummy head and tail wont get deleted
till the end of execution of this program
*/
void createSentinels() {
    head = createNode(0);
    tail = createNode(0);
    head->next = tail;
    tail->prev = head;
}

/*
insertion at the front of the queue
*/
void enqueueAtFront(int data) {
    struct node *newnode, *temp;

    newnode = createNode(data);
    temp = head->next;
    head->next = newnode;
    newnode->prev = head;
    newnode->next = temp;
    temp->prev = newnode;
}

/*
insertion at the rear of the queue
*/
void enqueueAtRear(int data) {
    struct node *newnode, *temp;
    newnode = createNode(data);
    temp = tail->prev;
    tail->prev = newnode;
    newnode->next = tail;
    newnode->prev = temp;
    temp->next = newnode;
}

/*
deletion at the front of the queue
*/
void dequeueAtFront() {
    struct node *temp;

    if (head->next ==  tail) {
        printf("Queue is empty\n");
    } else {
        temp = head->next;
        head->next = temp->next;
        temp->next->prev = head;
        free(temp);
    }
    return;
}

/*
delete at the rear of the queue
*/
void dequeueAtRear() {
    struct node *temp;
  
    if (tail->prev == head) {
        printf("Queue is empty\n");
    } else {
        temp = tail->prev;
        tail->prev = temp->prev;
        temp->prev->next = tail;
        free(temp);
    }
    return;
}

/*
display elements present in the queue
*/
void display() {
    struct node *temp;

    if (head->next == tail) {
        printf("Queue is empty\n");
        return;
    }

    temp = head->next;
    while (temp != tail) {
        printf("%-3d", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

/*
driver program
*/
int main() {
    int data, ch;

    createSentinels();
    while (1) {
        printf("1. Enqueue at front\n2. Enqueue at rear\n");
        printf("3. Dequeue at front\n4. Dequeue at rear\n");
        printf("5. Display\n6. Exit\n");
        printf("Enter you choice:");
        scanf("%d", &ch);
        switch(ch) {
            case 1:
                printf("Enter the data to insert:");
                scanf("%d", &data);
                enqueueAtFront(data);
                break;
            case 2:
                printf("Enter ur data to insert:");
                scanf("%d", &data);
                enqueueAtRear(data);
                break;
            case 3:
                dequeueAtFront();
                break;
            case 4:
                dequeueAtRear();
                break;
            case 5:
                display();
                break;
            case 6:
                exit(0);
            default:
                printf("Pls, enter corrent option\n");
                break;
        }
    }
    return 0;
}
