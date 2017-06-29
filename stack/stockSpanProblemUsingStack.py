#! coding=utf-8

'''
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
'''

# stock span problem using stack
def calculateSpan(price, S):

    n = len(price)

    # Create a stack and push index of first element to it
    st = []
    st.append(0)

    # Span value of first element is always 1
    S[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):
        # Pop element from stack while stack is not
        # empty and top of stack i smaller than price[i]
        while (len(st) > 0 and price[st[0]] <= price[i]):
            st.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, ie, price[0],
        # price[1], ..price[i-1], else the price[i] is
        # greater than elements after top of stack
        S[i] = i+1 if len(st) <= 0 else (i - st[0])

        # Push the element to stack
        st.append(i)

# Print array
def printArray(arr, n):

    for i in range(0, n):
        print arr[i],

# Driver program
def main():

    price = [10, 4, 5, 90, 120, 80]
    S = [0 for i in range(len(price) + 1)]

    # Fill the span values in array S[]
    calculateSpan(price, S)

    # Print
    printArray(S, len(price))

if __name__ == "__main__":
    main()
