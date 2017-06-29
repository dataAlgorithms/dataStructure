/*
Question:
The stock span problem is a financial problem where we have a series of n 
daily price quotes for a stock and we need to calculate span of stock’s 
price for all n days. 
The span Si of the stock’s price on a given day i is defined as the
 maximum number of consecutive days just before the given day, for which the
 price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, 
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

Algorithms:
se a stack as an abstract data type to store the days i, h(i), h(h(i)) and so on. 
When we go from day i-1 to i, we pop the days when the price of the stock was 
less than or equal to price[i] and then push the value of day i back into the stack.

Time Complexity: O(n).
Auxiliary Space: O(n) in worst case when all elements are sorted in decreasing order.

Output: 1 1 2 4 5 1 
*/

#include <iostream>
#include <stack>
using namespace std;

// A stack based efficient method to calculate stock span values
void calculateSpan(int price[], int n, int S[])
{
    // Create a stack and push index of first element to it
    stack<int> st;
    st.push(0);

    // Span value of first element is always 1
    S[0] = 1;

    // Calculate span values for rest of the elements
    for (int i = 1; i < n; i++)
    {
        // Pop elements from stack while stack is not empty and top of
        // stack is smaller than price[i]
        while (!st.empty() && price[st.top()] <= price[i])
            st.pop();

        // If stack becomes empty, then price[i] is greater than all elements
        // on left of it, ie, price[0], price[1], ..price[i-1],
        // else price[i] is greater than elements after top of stack
        S[i] = (st.empty())? (i+1): (i - st.top());

        // Push this element to stack
        st.push(i);
    }
}

// A utility function to print elements of array
void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
}

// Driver program
int main()
{
    int price[] = {10, 4, 5, 90, 120, 80};
    int n = sizeof(price)/sizeof(price[0]);
    int S[n];

    // Fill the span values in array S[]
    calculateSpan(price, n, S);

    // print the calculated span values
    printArray(S, n);

    return 0;
}
