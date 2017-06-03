1. Stack
//List Stack
class ListStack:
    # Init
    def __init__(self):
        self._theItems = list()

    # Length
    def __len__(self):
        return len(self._theItems)

    # IsEmpty
    def isEmpty(self):
        return len(self._theItems) == 0

    # Push
    def push(self, item):
        self._theItems.append(item)

    # Pop
    def pop(self):
        assert not self.isEmpty(), "Pop cannot be done at an empty Stack."
        self._theItems.pop()

    # Peek
    def peek(self):
        assert not self.isEmpty(), "Pop cannot be done at an empty Stack."
        return self._theItems[-1]

    # Iter
    def __iter__(self):
        return _StackIter(self._theItems)

class _StackIter:
    # Init
    def __init__(self, theItems):
        self._theItems = theItems
        self._size = 0
    def __iter__(self):
        return self
    def next(self):
        if self._size < len(self._theItems):
            cItem = self._theItems[self._size]
            self._size += 1
            return cItem
        else:
            raise StopIteration

def test_liststack():
    
    print '#Init a stack named smith using push'
    smith = ListStack()
    smith.push('CSCI-112')
    smith.push('MATH-121')
    smith.push('HIST-340')
    smith.push('ECON-101')
    
    print '\n#output smith stack'
    for element in smith:
        print element
           
    print '\n#pop one item'
    smith.pop()
    
    print '\n#output smith stack after pop'
    for element in smith:
        print element 
        
    print '\n#get the peek item'
    peek_item = smith.peek()
    print 'peek item is ', peek_item
    
    print '\n#get the length of stack'
    print 'the lenght of stack is ', len(smith)
    
    print '\n#check wheter the stack is empty'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
        
    print '\n#pop all items'
    while not smith.isEmpty():
        smith.pop()
    
    print '\n#check wheter the stack is empty after pop all items'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
    
if __name__ == "__main__":
    test_liststack()

//LinkedList Stack
class LinkListStack:
    # Init
    def __init__(self):
        self._top = None
        self._size = 0

    # Length
    def __len__(self):
        return self._size

    # IsEmpty
    def isEmpty(self):
        return self._size == 0

    # Push
    def push(self, item):
        if self._top is None:
            newNode = _StackNode(item)
            newNode.next = None
            self._top = newNode
            self._size += 1
        else:
            newNode = _StackNode(item)
            newNode.next = self._top
            self._top = newNode
            self._size += 1

    # Pop
    def pop(self):
        assert not self.isEmpty(), "Stack is empty."
        self._top = self._top.next
        self._size -= 1

    # Peek
    def peek(self):
        assert not self.isEmpty(), "Stack is empty."
        return self._top.item

    # Iter
    def __iter__(self):
        return _StackIter(self._top)

class _StackNode:
    # Init
    def __init__(self, theItem):
        self.item = theItem
        self.next = None

class _StackIter:
    # Init
    def __init__(self, top):
        self._cTop = top
    def __iter__(self):
        return self
    def next(self):
        if self._cTop is not None:
            item = self._cTop.item
            self._cTop = self._cTop.next
            return item
        else:
            raise StopIteration

def test_linkliststack():
    
    print '#Init a stack named smith using push'
    smith = LinkListStack()
    smith.push('CSCI-112')
    smith.push('MATH-121')
    smith.push('HIST-340')
    smith.push('ECON-101')
    
    print '\n#output smith stack'
    for element in smith:
        print element
           
    print '\n#pop one item'
    smith.pop()
    
    print '\n#output smith stack after pop'
    for element in smith:
        print element 
        
    print '\n#get the peek item'
    peek_item = smith.peek()
    print 'peek item is ', peek_item
    
    print '\n#get the length of stack'
    print 'the lenght of stack is ', len(smith)
    
    print '\n#check wheter the stack is empty'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
        
    print '\n#pop all items'
    while not smith.isEmpty():
        smith.pop()
    
    print '\n#check wheter the stack is empty after pop all items'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
    
if __name__ == "__main__":
    test_linkliststack()

2. Find maximum difference between nearest left and right smaller elements
Given array of integers, the task is to find the maximum absolute
difference between nearest left and right smaller element of every element in array
#! coding=utf-8 

'''
Find maximum difference between nearest left and right smaller elements
Given array of integers, the task is to find the maximum absolute 
difference between nearest left and right smaller element of every element in array.

Note : If there is no smaller element on right side or left side of any element then we take zero 
as smaller element. For example for leftmost element, nearest smaller element on left side is 
considered as 0. Similarly for rightmost elements, smaller element on right side is considered as 0.

Examples:

Input : arr[] = {2, 1, 8}
Output : 1
Left smaller  LS[] {0, 0, 1}
Right smaller RS[] {1, 0, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 1 

Input  : arr[] = {2, 4, 8, 7, 7, 9, 3}
Output : 4
Left smaller   LS[] = {0, 2, 4, 4, 4, 7, 2}
Right smaller  RS[] = {0, 3, 7, 3, 3, 3, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 7 - 3 = 4 

Input : arr[] = {5, 1, 9, 2, 5, 1, 7}
Output : 1
Left smaller LS[] = {0, 0, 0, 1, 2, 0, 1}
Right smaller RS[] = {1, 0, 2, 1, 1, 0, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 2 - 1 = 1

A simple solution is to find nearest left and right smaller elements for every element and 
then update the maximum difference between left and right smaller element , this take O(n^2) time.

An efficient solution takes O(n) time. We use a stack. 
The interesting part here is we compute both left smaller and right smaller using same function.

Let input array be 'arr[]' and size of array be 'n'

Find all smaller element on left side
     1. Create a new empty stack S and an array LS[]
     2. For every element 'arr[i]' in the input arr[],
          where 'i' goes from 0 to n-1.
        a) while S is nonempty and the top element of 
           S is greater than or equal to 'arr[i]':
           pop S
    
        b) if S is empty:
           'arr[i]' has no preceding smaller value 
            LS[i] = 0 
            
        c) else:
            the nearest smaller value to 'arr[i]' is top
            of stack
              LS[i] = s.top()

        d) push 'arr[i]' onto S   

Find all smaller element on right side
     3. First reverse array arr[]. After reversing the array, 
        right smaller become left smaller.
     4. Create an array RRS[] and repeat steps  1 and 2 to 
        fill RRS (in-place of LS).
         
5. Initialize result as -1 and do following for every element
   arr[i]. In the reversed array right smaller for arr[i] is
   stored at RRS[n-i-1]
      return result = max(result, LS[i]-RRS[n-i-1])
'''

class Stack:
    # Init
    def __init__(self):
        self._top = None
        self._size = 0

    # Length
    def __len__(self):
        return self._size

    # IsEmpty
    def isEmpty(self):
        return self._size == 0

    # Push
    def push(self, item):
        if self._top is None:
            newNode = _StackNode(item)
            newNode.next = None
            self._top = newNode
            self._size += 1
        else:
            newNode = _StackNode(item)
            newNode.next = self._top
            self._top = newNode
            self._size += 1

    # Pop
    def pop(self):
        assert not self.isEmpty(), "Stack is empty."
        self._top = self._top.next
        self._size -= 1

    # Peek
    def peek(self):
        assert not self.isEmpty(), "Stack is empty."
        return self._top.item

    # Iter
    def __iter__(self):
        return _StackIter(self._top)

class _StackNode:
    # Init
    def __init__(self, theItem):
        self.item = theItem
        self.next = None

class _StackIter:
    # Init
    def __init__(self, top):
        self._cTop = top
    def __iter__(self):
        return self
    def next(self):
        if self._cTop is not None:
            item = self._cTop.item
            self._cTop = self._cTop.next
            return item
        else:
            raise StopIteration

'''
Function to fill left smaller element for every
element of arr[0..n-1], These values are filled
in se[0...n-1]
'''
def leftSmaller(arr, SE):

    # get the length 
    n = len(arr)

    # Create an empty stack
    S = Stack()

    # Traverse all array elements
    # compute nearest smaller elements of every element
    for i in range(n):
        # Keep removing smaller element from S which the top
        # element is greater than or equal to arr[i]
        while not S.isEmpty() and S.peek() >= arr[i]:
            S.pop()

        # Store the smaller element of current element
        if not S.isEmpty():
            SE[i] = S.peek()

        # If all elements in S were greater than arr[i]
        else:
            SE[i] = 0

        # Push this elment
        S.push(arr[i])

'''
Function returns maximum difference b/w Left &
right smaller element
'''
def findMaxDiff(arr):

    # get the length 
    n = len(arr)
    
    # get the length
    LS = [0] * n

    # find left smaller element of every element
    leftSmaller(arr, LS)

    # find right smaller element of every element
    # first reverse the array and do the same process
    RRS = [0] * n # store right smaller elements in reverse array

    # reverse the array
    arr = [arr[i] for i in range(len(arr)-1, -1, -1)]
    leftSmaller(arr, RRS)

    # find maximum absolute difference b/w LS & RRS
    # In the reversed array right smaller for arr[i] is 
    # stored at RRS[n-i-1]
    result = -1
    for i in range(n):
        result = max(result, abs(LS[i] - RRS[n-1-i]))

    # return maximum difference b/w LS & RRS
    return result

'''
4
1
1
'''
if __name__ == "__main__":
    for arr in [[2, 4, 8, 7, 7, 9, 3], [2, 1, 8], [5, 1, 9, 2, 5, 1, 7]]:
        print findMaxDiff(arr)
