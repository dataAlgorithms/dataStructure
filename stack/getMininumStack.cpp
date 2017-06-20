/*
C++ program to implement a stack that supports
getMininum() in O(1) time and O(1) extra space

Algorithms:
Push(x) : Inserts x at the top of stack.

If stack is empty, insert x into the stack and make minEle equal to x.
If stack is not empty, compare x with minEle. Two cases arise:
If x is greater than or equal to minEle, simply insert x.
If x is less than minEle, insert (2*x – minEle) into the stack and make minEle equal to x. 
For example, let previous minEle was 3. Now we want to insert 2. 
We update minEle as 2 and insert 2*2 – 3 = 1 into the stack.
Pop() : Removes an element from top of stack.

Remove element from top. Let the removed element be y. Two cases arise:
If y is greater than or equal to minEle, the minimum element in the stack is still minEle.
If y is less than minEle, the minimum element now becomes (2*minEle – y), so update (minEle = 2*minEle – y). 
This is where we retrieve previous minimum from current minimum and its value in stack. For example, 
let the element to be removed be 1 and minEle be 2. We remove 1 and update minEle as 2*2 – 1 = 3.

Important Points:
Stack doesn’t hold actual value of an element if it is minimum so far.
Actual minimum element is always stored in minEle


Suppose: (insert 3 5 2 1 1 -1 into stack)
Number to be Inserted: 3, Stack is empty, so insert 3 into stack and minEle = 3.
Number to be Inserted: 5, Stack is not empty, 5> minEle, insert 5 into stack and minEle = 3.
Number to be Inserted: 2, Stack is not empty, 2< minEle, insert (2*2-3 = 1) into stack and minEle = 2.
Number to be Inserted: 1, Stack is not empty, 1< minEle, insert (2*1-2 = 0) into stack and minEle = 1.
Number to be Inserted: 1, Stack is not empty, 1 = minEle, insert 1 into stack and minEle = 1.
Number to be Inserted: -1, Stack is not empty, -1 < minEle, insert (2*-1 – 1 = -3) into stack and minEle = -1.

Suppse: (pop stack: -3 1 0 1 5 3)
Initially the minimum element minEle in the stack is -1.
Number removed: -3, Since -3 is less than the minimum element the original 
number being removed is minEle which is -1, and the new minEle = 2*-1 – (-3) = 1
Number removed: 1, 1 == minEle, so number removed is 1 and minEle is still equal to 1.
Number removed: 0, 0< minEle, original number is minEle which is 1 and new minEle = 2*1 – 0 = 2.
Number removed: 1, 1< minEle, original number is minEle which is 2 and new minEle = 2*2 – 1 = 3.
Number removed: 5, 5> minEle, original number is 5 and minEle is still 3
*/

using namespace std;

// A stack that supports getMin() 
//in addition to push() and pop()
struct MyStack
{
    stack<int> s;
    int minEle;

    //Print minimum element of MyStack
    void getMin()
    {
        if (s.empty())
            cout << "Stack is empty\n";

        //Variable minEle stores the minimum element
        //in the stack
        else
            cout << "Mininum element is: " << minEle << "\n";
    }

    //Print top element of MyStack
    void peek()
    {
        if (s.empty())
        {
            cout << "Stack is empty";
            return;
        }

        int t = s.top();
        cout << "Top most element is: ";

        //If t < minEle means minEle stores value of t
        (t < minEle)? cout << minEle: cout << t;
    }

    //Remove the top element from MyStack
    void pop()
    {
        if (s.empty())
        {
            cout << "Stack is empty\n";
            return;
        }

        cout << "Top most element removed:";
        int t = s.top();
        s.pop();

        //Minimum will change as the minimum element
        //of the stack is being removed
        if (t < minEle)
        {
            cout << minEle << "\n";
            minEle = 2*minEle - t;
        }
        else
            cout << t << "\n";
    }

    //Push element into MyStack
    void push(int x)
    {
        //Insert new number into the stack
        if (s.empty())
        {
            minEle = x;
            s.push(x);
            cout << "Number inserted: " << x << "\n";
            return;
        }

        //If new number is less than minEle
        if (x < minEle)
        {
            s.push(2*x - minEle);
            minEle = x;
        }
        else
            s.push(x);

        cout << "Number inserted: " << x << "\n";
    }
};

//Driver code
int main()
{
    MyStack s;
    s.push(3);
    s.push(5);
    s.getMin();
    s.push(2);
    s.push(1);
    s.getMin();
    s.pop();
    s.getMin();
    s.pop();
    s.peek();

    return 0;
}

/*
Number inserted: 3
Number inserted: 5
Mininum element is: 3
Number inserted: 2
Number inserted: 1
Mininum element is: 1
Top most element removed:1
Mininum element is: 2
Top most element removed:2
Top most element is: 5
*/
