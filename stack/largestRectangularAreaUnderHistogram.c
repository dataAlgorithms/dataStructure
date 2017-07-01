/*
Question:
Largest rectangle under histogram

Algorithms:
Process the elements in left-to-right order and maintain a stack of information
about started but yet unfinished sub histograms

if the stack is empty, open a new sub problem by pushing the element onto the stack
otherwise compare it to the element on top of the stack. If the new one is greater we
again push it. If the new one is equal we skip it. In all these cases, we continue with 
the next new element. If the new one is less, we finish the topmost sub problem by 
updating the maximum area with respect to the element at the top of the stack
then, we discard the element at the top, and repeat the procedure keeping the current new element

this wy, all sub problems are finished when the stack becomes empty, or its top element is less
than or equal to the new element, leading to the actions described above, if all elements have 
been processed, and the stack is not yet empty, we finish the remaining sub problems by updating the 
maximum area with respect to the elements at the top

Time Complexity:
O(n)

Output:
12
*/

#include <stdio.h>
#include <stdlib.h>

struct StackItem {
    int height;
    int index;
};

int MaxRectangleArea(int A[], int n) {
    int i, maxArea=-1, top=-1, left, currentArea;
    struct StackItem *S = (struct StackItem *)malloc(sizeof(struct StackItem) * n);
    for (i=0; i <= n; i++) 
    {
        while (top >= 0 && (i == n || S[top].height > A[i])) {
            if (top > 0)
                left = S[top-1].index;
            else
                left = -1;

            currentArea = (i - left - 1) * S[top].height;
            --top;
            if (currentArea > maxArea)
                maxArea = currentArea;
        }

        if (i < n) {
            ++top;
            S[top].height = A[i];
            S[top].index = i;
        }
    }

    return maxArea;
}

int main()
{
    int hist[] =  {6, 1, 5, 4, 5, 2, 6};
    int n = sizeof(hist)/sizeof(hist[0]);
    int tmp = MaxRectangleArea(hist, n);

    printf("%d \n", tmp);
    return 0;
}
