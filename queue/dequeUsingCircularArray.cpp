/*
Problem:
Implementation of Deque using circular array
Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.In previous post we had discussed introduction of deque. Now in this post we see how we implement deque Using circular array.
Operations on Deque:
Mainly the following four basic operations are performed on queue:
insetFront(): Adds an item at the front of Deque.
insertRear(): Adds an item at the rear of Deque.
deleteFront(): Deletes an item from front of Deque.
deleteRear(): Deletes an item from rear of Deque.

In addition to above operations, following operations are also supported
getFront(): Gets the front item from queue.
getRear(): Gets the last item from queue.
isEmpty(): Checks whether Deque is empty or not.
isFull(): Checks whether Deque is full or not.

Algorithms:
 In the function

Time Complexity: 
All operations like insertfront(), insertlast(), deletefront(), deletelast()is O(1).

Output:
get rear element 10
after delete rear element new rear 5
get front element  15
after delete front element new front 5

Refer:
http://www.geeksforgeeks.org/implementation-deque-using-circular-array/
*/

#include <iostream>
using namespace std;

// Maximum size of array or Dequeue
#define MAX 100

// A structure to represent a Deque
class Deque
{
    int arr[MAX];
    int front;
    int rear;
    int size;

public:
    Deque(int size)
    {
        front = -1;
        rear = 0;
        this->size = size;
    }

    // Operations on Deque
    void insertfront(int key);
    void insertrear(int key);
    void deletefront();
    void deleterear();
    bool isFull();
    bool isEmpty();
    int getFront();
    int getRear();
};

// Check whether Deque is full or not
bool Deque::isFull()
{
    return ((front == 0 && rear == size-1) || \
                front == rear + 1);
}

// Check whether Deque is empty or not
bool Deque::isEmpty()
{
    return (front == -1);
}

// Insert an element at front
void Deque::insertfront(int key)
{
    /*
    a). First we check deque if Full or Not
    b). IF Front == 0 || initial position, move Front
                     to points last index of array
       front = size - 1
    Else decremented front by '1' and push 
         current key into Arr[ Front] = key 
    Rear remain same. 
    */

    // check whether Deque is full or not
    if (isFull())
    {
        cout << "Overflow\n" << endl;
        return;
    }

    // If queue is initially empty
    if (front == -1)
    {
        front = 0;
        rear = 0;
    }

    // front is at first position of queue
    else if (front == 0)
        front = size - 1;
    // decrement front end by 1
    else
        front = front - 1;

    // insert current element into Deque
    arr[front] = key;
}

// insert element at rear end of Deque
void Deque::insertrear(int key)
{
    /*
    a). First we check deque if Full or Not 
    b). IF Rear == Size-1 
       then reinitialize Rear = 0 ;
    Else increment Rear by '1'
    and push current key into Arr[ rear ] = key 
    Front remain same.    
    */
    if (isFull())
    {
        cout << "Overflow\n" << endl;
        return;
    }

    // If queue is initially empty
    if (front == -1)
    {
        front = 0;
        rear = 0;
    }

    // rear if at last position of queue
    else if (rear == size-1)
        rear = 0;

    // increment rear end by 1
    else
        rear = rear + 1;

    // insert current element into Deque
    arr[rear] = key;
}

// Delete element at front end of Deque
void Deque::deletefront()
{
    /*
    a). first Check deque is Empty or Not
    b).  If deque has only one element
            front = -1 ; rear =-1 ;
    Else IF front points to the last index of the array
         it's means we have no more elements in array so 
          we move front to points first index of array
            front = 0 ;
    Else || increment Front by '1'  
            front = front+1;
    */
    // check whether Deque is empty or not
    if (isEmpty())
    {
        cout << "Queue underflow\n" << endl;
        return;
    }

    // Deque has only one element
    if (front == rear)
    {
        front = -1;
        rear = -1;
    }
    else
        // back to initial position
        if (front == size -1)
            front = 0;

        // increment front by 1 to remove current
        // front value from Deque
        else
            front = front + 1;
}

// Delete element at rear end of Deque
void Deque::deleterear()
{
    /*
    a). first Check deque is Empty or Not
    b).  If deque has only one element
        front = -1 ; rear =-1 ;
    Else IF Rear points to the first index of array
         it's means we have to move rear to points 
         last index [ now first inserted element at 
         front end become rear end ]  
            rear = size-1 ;
    Else || decrease rear by '1'  
            rear = rear-1;
    */
    if (isEmpty())
    {
        cout << "Underflow\n" << endl;
        return;
    }

    // Deque has only one element
    if (front == rear)
    {
        front = -1;
        rear = -1;
    }
    else if (rear == 0)
        rear = size - 1;
    else
        rear = rear - 1;
}

// Return front element of Deque
int Deque::getFront()
{
    // check whether Deque is empty or not
    if (isEmpty())
    {
        cout << "Underflow\n" << endl;
        return -1;
    }
    return arr[front];
}

// Return rear element of Deque
int Deque::getRear()
{
    // check whether Deque is empty or not
    if (isEmpty() || rear < 0)
    {
        cout << "Underflow\n" << endl;
        return -1;
    }
    return arr[rear];
}

// Driver program
int main()
{
    Deque dq(5);
    dq.insertrear(5);
    dq.insertrear(10);

    cout << "get rear element" << " "
            << dq.getRear() << endl;

    dq.deleterear();
    cout << "after delete rear element new rear " 
            << dq.getRear() << endl;

    dq.insertfront(15);
    cout << "get front element " << " "
           << dq.getFront() << endl;
   
    dq.deletefront();
    cout << "after delete front element new front "
           << dq.getFront() << endl;
    return 0;
}
