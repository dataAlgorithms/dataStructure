/*
Question:
check-if-array-elements-are-consecutive/

Algorithms:
The idea is to check for following two conditions. If following two conditions are true, then return true.
1) max – min + 1 = n where max is the maximum element in array, min is minimum element in array and 
n is the number of elements in array.
2) All elements are distinct.

To check if all elements are distinct, we can create a visited[] array of size n. 
We can map the ith element of input array arr[] to visited array by using arr[i] – min as index in visited[].

Time Complexity: O(n)
Extra Space: O(n)
*/

#include <stdio.h>
#include <stdlib.h>

// Helper function to get minimum and maximum in an array
int getMin(int arr[], int n);
int getMax(int arr[], int n);

// Check if the array elements are consecutive 
bool areaConsecutive(int arr[], int n)
{
    if (n < 1)
        return false;

    // get the minimum element
    int min = getMin(arr, n);

    // get the maximum element
    int max = getMax(arr, n);

    // max - min + 1 is equal to n, then only check all elements
    if (max - min + 1 == n)
    {
        // Create a temp array to hold visited flag of all ements
        // calloc is used here so that all values are initialized as false
        bool *visited = (bool *)calloc(n , sizeof(bool));
        int i;

        for (i = 0 ; i < n ; i++)
        {
            // if we see an element again, then return false
            if (visited[arr[i] - min] != false)
                return false;

            // if visted first time, then mark the element as visited
            visited[arr[i] - min] = true;

        }

        // if all elements occur once, then return true
        return true;
    }

    return false;
}

// get min
int getMin(int arr[], int n)
{
    int min = arr[0];
    
    for (int i = 1; i < n; i++)
        if (arr[i] < min)
            min = arr[i];

    return min;
}

// get max
int getMax(int arr[], int n)
{
    int max = arr[0];

    for (int i = 1; i < n; i++)
        if (arr[i] > max)
            max = arr[i];

    return max;
}

// driver program
int main()
{
    int arr[] = {5, 2, 3, 1, 4};

    int n = sizeof(arr)/sizeof(arr[0]);
    
    if (areaConsecutive(arr, n) == true)
        printf(" Consecutive!");
    else
        printf(" Not consecutive!");
    
   return 0;
}
