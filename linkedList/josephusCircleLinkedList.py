'''
Question:
There are n people standing in a circle waiting to be executed. The counting out begins at some point in the circle and
 proceeds around the circle in a fixed direction. In each step, a certain number of people are skipped and the next 
 person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the 
 executed people are removed), until only the last person remains, who is given freedom. Given the total number
  of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle. 
  The task is to choose the place in the initial circle so that you are the last one remaining and so survive.

For example, if n = 5 and k = 2, then the safe position is 3. Firstly, the person at position 2 is killed, then
 person at position 4 is killed, then person at position 1 is killed. Finally, the person at position 5 is killed. 
 So the person at position 3 survives.
If n = 7 and k = 3, then the safe position is 4. The persons at positions 3, 6, 2, 7, 5, 1 are killed in order,
 and person at position 4 survives.

picture display:
http://thedailywtf.com/articles/Programming-Praxis-Josephus-Circle
'''

'''
Solution one:
  josephuse circle using number, any step
  refer:http://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
'''
def josephusCircleOne(n, k):

    if n == 1:
        return 1
    else:
        '''
        The position returned by josephus circle (n-1,  k) is 
        adjusted because the recursive call josephus(n-1, k) considers
        original position k%n + 1 as position 1
        '''
        return (josephusCircleOne(n-1, k) + k -1) % n +1

def mainOne():

    print ':::5 node, step is 2'
    n = 5
    k = 2
    print("The chosen place using soluation one is ", josephusCircleOne(n, k))
    
    print '\r:::7 node, step is 3'
    n = 7
    k = 3
    print("The chosen place using soluation one is ", josephusCircleOne(n, k))

'''
 Solution two: any number, step is 2
 refer:http://www.geeksforgeeks.org/josephus-problem-set-2-simple-solution-k-2/
'''
def josephusCircleTwo(n):

    '''
    Find value of 2 ^ (1+floor(Log n))
    which is a power of 2 whose value
    is just above n
    '''
    p = 1
    while (p <= n):
        p *= 2

    '''
    Return 2n - 2^(1+floor(logn)) + 1
    '''
    return 2*n - p + 1

def mainTwo():

    print ':::5 node, step is 2'
    n = 5
    print("The chosen place uisng soluation two is ", josephusCircleTwo(n))
    
    print '\r:::16 node, step is 2'
    n = 16
    print("The chosen place using soluaton two is ", josephusCircleTwo(n))
    
"""
Soluation three: using circular linked list to store data
"""
class _CircularLinkedListNode:
    def __init__(self, data):
        self.data = data 
        self.next = None

class _CircularLinkedListIter:
    def __init__(self, listRef, count):
        self._listRef = listRef
        self._index = 0
        self._count = count 
    def __iter__(self):
        return self
    def next(self):
        if self._index < self._count:
            curNode = self._listRef.data
            self._listRef = self._listRef.next
            self._index += 1
            return curNode
        else:
            raise StopIteration

class CircularLinkedList:
    def __init__(self):
        self._listRef = None
        self._count = 0

    def __len__(self):
        return self._count

    def listLength(self):
        return self._count
    
    def listIsEmpty(self):
        return self._count == 0

    def listNodeInsert(self, data, position):
        newNode = _CircularLinkedListNode(data)
        
        if position == 0:
            if len(self) == 0:
                self._listRef = newNode 
                newNode.next = self._listRef
            elif len(self) == 1:
                curNode = self._listRef
                newNode.next = self._listRef
                self._listRef.next = newNode 
                self._listRef = newNode
            else:
                curNode = self._listRef
                while curNode.next is not self._listRef:
                    curNode = curNode.next
                newNode.next = self._listRef
                curNode.next = newNode
                self._listRef = newNode
            
        elif position == -1:
            if len(self) == 0:
                self._listRef = newNode 
                newNode.next = self._listRef
            elif len(self) == 1:
                curNode = self._listRef
                newNode.next = self._listRef
                self._listRef.next = newNode 
            else:                
                curNode = self._listRef
                while curNode.next is not self._listRef:
                    curNode = curNode.next
                curNode.next = newNode
                newNode.next = self._listRef
        else:
            if len(self) == 0:
                self._listRef = newNode 
                newNode.next = self._listRef
            elif len(self) == 1:
                curNode = self._listRef
                newNode.next = self._listRef
                self._listRef.next = newNode 
                self._listRef = newNode
            else:               
                preNode = self._listRef
                curNode = self._listRef
                index = 0
                while curNode.next is not self._listRef and index < position:
                    preNode  = curNode
                    curNode = curNode.next
                    index += 1
        
                newNode.next = curNode
                preNode.next = newNode

        self._count += 1

    def listNodeDelete(self, position):
        assert position >= -1 and position < len(self), \
                  "Out of subcription!"
        assert not self.listIsEmpty(), "List is empty!"
        if len(self) == 1:
            self._listRef = None
        else:
            if position == 0:
                curNode = self._listRef
                while curNode.next is not self._listRef:
                    curNode = curNode.next

                self._listRef = self._listRef.next
                curNode.next = self._listRef
            elif position == -1:
                preNode = self._listRef
                curNode = self._listRef
                while curNode.next is not self._listRef:
                    preNode = curNode
                    curNode = curNode.next
                
                preNode.next = self._listRef
            else:
                preNode = self._listRef
                curNode = self._listRef
                index = 0
                while curNode.next is not self._listRef and index < position:
                    preNode = curNode
                    curNode = curNode.next
                    index += 1

                preNode.next = curNode.next

        self._count -= 1

    def listTraversal(self):
        index = 0
        curNode = self._listRef
        
        while index < len(self):
            print "%s " % curNode.data,
            curNode = curNode.next
            index += 1

        print "\r"
        
    def __iter__(self):
        return _CircularLinkedListIter(self._listRef, len(self))
    
def josephusCircleThree(n, k, p):
    
    # Eliminate every Mth player as long as more than one player remains
    for _count in range(n, 1, -1):
        for _i in range(k-1):
            p = p.next 
        p.next = p.next.next  # Remove the eliminated plaayer from the circular linked list
    
    print ':::%s node, step is %s' % (n, k)
    print "The chosen place using soluaton three is ", p.data

def mainThree():

    print '\r'
    cll = CircularLinkedList()
  
    for i in range(5, 0, -1):
        cll.listNodeInsert(i, 0)   
    cll.listTraversal()
    
    q = cll._listRef
    p = cll._listRef
    # q is pointing to first node
    # p is pointing to last node
    # p.next is q
    while p.next is not q:
        p = p.next 
        
    josephusCircleThree(5, 2, p)

    cll = CircularLinkedList()
  
    for i in range(7, 0, -1):
        cll.listNodeInsert(i, 0)   
    cll.listTraversal()
    
    q = cll._listRef
    p = cll._listRef
    # q is pointing to first node
    # p is pointing to last node
    # p.next is q
    while p.next is not q:
        p = p.next 
        
    josephusCircleThree(7, 3, p)
        
"""
:::5 node, step is 2
('The chosen place using soluation one is ', 3)

:::7 node, step is 3
('The chosen place using soluation one is ', 4)
:::5 node, step is 2
('The chosen place uisng soluation two is ', 3)

:::16 node, step is 2
('The chosen place using soluaton two is ', 1)

1  2  3  4  5  
:::5 node, step is 2
The chosen place using soluaton three is  3
1  2  3  4  5  6  7  
:::7 node, step is 3
The chosen place using soluaton three is  4
"""
if __name__ == "__main__":
    mainOne()
    mainTwo()
    mainThree()
