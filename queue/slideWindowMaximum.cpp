/*
Method Two: use Dequeue

Algo:
Create a Dequeue, Qi of capacity k, that stores only usefull 
elements of current window of k elements.
An element is usefull if it is in current window and is greater
tha all other elements on left side of it in current window.
We process all array elements one by one and maintain Qi to contain
useful elements of current window and these usefull elements are 
maintained in sorted order. The element at front of the Qi is the 
largest and element at rear of Qi is the smallest of current window

Time Complexity: O(n). It seems more than O(n) at first look. 
If we take a closer look, we can observe that every element of array 
is added and removed at most once. So there are total 2n operations.
Auxiliary Space: O(k)

Output:
78 90 90 90 89
*/

#include <iostream>
#include <deque>

using namespace std;

/*
A Dequeue (Double ended queue) based method for printing maximum
element of all subarrays of size k
*/
void printKMax(int arr[], int n, int k)
{
    /*
    Create a Double Ended Queue, Qi that will store indexes of array elements
    The queue will store indexes of usefull elements in every window and it will
    maintain decreasing order of values from front to rear in Qi, ie.
    arr[Qi.front[]] to arr[Qi.rear()] are sorted in decreasing order
    */
    std::deque<int> Qi(k);

    /*
    Process first k (or first window) elements of array
    */
    int i;
    for (i = 0; i < k; ++i)
    {
        // For very element, the previous smaller elements are useless so
        // remove them from Qi
        while ((!Qi.empty()) && arr[i] >= arr[Qi.back()])
            Qi.pop_back();  // Remove from rear

        // Add new element at rear of queue
        Qi.push_back(i);
    }

    /*
    Process rest of the elements, ie. from arr[i] to arr[n-1]
    */
    for (; i < n; ++i)
    {
        // The element at the front of the queue is the largest element of
        // previous window, so print it
        cout << arr[Qi.front()] << " ";

        // Remove the elements which are out of this window
        while ((!Qi.empty()) && Qi.front() <= i - k)
            Qi.pop_front(); // Remove from front of queue

        // Remove all elements smaller than the currently
        // being added element (remove useless elements)
        while ((!Qi.empty()) && arr[i] >= arr[Qi.back()])
            Qi.pop_back();

        // Add current element at the rear of Qi
        Qi.push_back(i);
    }

    // Print the maximum element of last window
    cout << arr[Qi.front()];
}

// Driver program 
int main()
{
    int arr[] = {12, 1, 78, 90, 57, 89, 56};
    int n = sizeof(arr)/sizeof(arr[0]);
    int k = 3;
    printKMax(arr, n, k);
    return 0;
}
