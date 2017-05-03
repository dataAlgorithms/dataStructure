'''
Method one: Insert sort for single linked list

1) Create an empty sorted (or result) list
2) Traverse the given list, do following for every node.
......a) Insert current node in sorted way in sorted or result list.
3) Change head of given linked list to head of sorted (or result) list
'''
# sort a singly linked list using insertion sort
def insertSort(h):
    if h == None:
        return None
    #Make the first node the start of the sorted list.
    sortedList= h
    h=h.next
    sortedList.next= None
    while h != None:
        curr= h
        h=h.next
        if curr.data<sortedList.data:
            #Advance the nodes
            curr.next= sortedList
            sortedList= curr
        else: 
            #Search list for correct position of current.
            search= sortedList
            while search.next!= None and curr.data > search.next.data:
                search= search.next
            #current goes after search.
            curr.next= search.next
            search.next= curr
    return sortedList

'''
Method two: Quick sort for single linked list

In partition(), we consider last element as pivot. We traverse through the current list and if a node 
has value greater than pivot, we move it after tail. If the node has smaller value, we keep it at its current position.
In QuickSortRecur(), we first call partition() which places pivot at correct position and returns pivot. After pivot is 
placed at correct position, we find tail node of left side (list before pivot) and recur for left list.
 Finally, we recur for right list.
'''
# Quick sort wrapper 
def quickSort(headRef):

    headRef = quickSortRec(headRef, getTail(headRef))
    return headRef

# Here the sorting happens exclusive of the end node
def quickSortRec(head, end):

    # base condition
    if not head or head == end:
        return head

    newHead = None
    newEnd = None

    # partition the list, newHead and newEnd will be updated 
    # by the partition function
    pivot,newHead,newEnd = partition(head, end, newHead, newEnd)

    # If pivot is the smallest element - no need to recur for
    # the left part
    if newHead != pivot:
        # Set the node before the pivot node as None
        tmp = newHead
        while tmp.next != pivot:
            tmp = tmp.next
        tmp.next = None

        # Recur for the list before pivot
        newHead = quickSortRec(newHead, tmp)
        
        # Change next of last node of the left half to pivot
        tmp = getTail(newHead)
        tmp.next = pivot

    # Recur for the list after the pivot element
    pivot.next = quickSortRec(pivot.next, newEnd)

    return newHead

# Partition the list taking the last element as the pivot
def partition(head, end, newHead, newEnd):

    pivot = end
    prev = None
    cur = head
    tail = pivot

    # During partition, both the head and end of the list might change
    # which is updated in the newHead and newEnd variables
    while cur != pivot:
        if cur.data < pivot.data:
            # First node that has a value less than the pivot - becomes the new head
            if newHead is None:
                newHead = cur

            prev = cur
            cur = cur.next
        else:
            # Move cur node to next of tail, and change tail
            if prev is not None:
                prev.next = cur.next
            tmp = cur.next
            cur.next = None
            tail.next = cur
            tail = cur
            cur = tmp

    # If the pivot data is the smallest element is the current list, pivot becomes the head
    if newHead is None:
        newHead = pivot

    # Update the newEnd to the current last node
    newEnd = tail

    # Return the pivot node
    return pivot,newHead,newEnd 

# Return the last node of the list
def getTail(cur):

    while cur is not None and cur.next is not None:
        cur = cur.next

    return cur

'''
Method Three: merge sort the single linked list   ---prefered algorithms: sort for single linked list
'''

'''
sort the linked list by changing next pointer
'''
def mergeSort(headRef):

    head = headRef
    
    # Base case -- length 0 or 1
    if head is None or head.next is None:
        return head

    # Split head into two sublists
    frontRef, backRef = frontBackSplit(head)

    # Recursively sort the sublists
    frontRef = mergeSort(frontRef)
    backRef = mergeSort(backRef)

    # Merge the two sorted list together
    headRef = sortedMerge(frontRef, backRef)

    return headRef

def mergeSortLinkedList(A):
    if A is None or A.next is None:
        return A

    leftHalf, rightHalf = splitTheList(A)

    left = mergeSortLinkedList(leftHalf)
    right = mergeSortLinkedList(rightHalf)

    return mergeTheLists(left, right)

'''
sort merge
'''
def sortedMerge(frontRef, backRef):

    # base cases
    if frontRef is None:
        return backRef
    elif backRef is None:
        return frontRef

    # Pick either frontRef or backRef and recur
    if frontRef.data <= backRef.data:
        result = frontRef
        result.next = sortedMerge(frontRef.next, backRef)
    else:
        result = backRef
        result.next = sortedMerge(frontRef, backRef.next)

    return result

def mergeTheLists(leftHalf, rightHalf):
    fake_head = _SingleLinkedListNode(None)
    curr = fake_head

    while leftHalf and rightHalf:
        if leftHalf.data < rightHalf.data:
            curr.next = leftHalf
            leftHalf = leftHalf.next

        else:
            curr.next = rightHalf
            rightHalf = rightHalf.next

        curr = curr.next

    if leftHalf == None:
        curr.next = rightHalf

    elif rightHalf == None:
        curr.next = leftHalf

    return fake_head.next

'''
utility function

split the nodes of the given list into front and back halves
and return the two lists using the reference parameters
if the length is odd, the extra node should go in the front list
use the fast/slow pointer strategy
'''
def frontBackSplit(source):

    if source is None or source.next is None:
        # length < 2 cases
        frontRef = source
        backRef = None
    else:
        slow = source
        fast = source.next

        # Advacne fast two nodes, and advance slow one node
        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next

        # slow is beforre the midpoint in the list, so split it in two at that point
        frontRef = source
        backRef = slow.next
        slow.next = None

    return frontRef, backRef

def splitTheList(sourceList):
    if sourceList == None or sourceList.next == None:
        leftHalf = sourceList
        rightHalf = None

        return leftHalf, rightHalf

    else:
        midPointer = sourceList
        frontRunner = sourceList.next
        # totalLength += 1        - This is unnecessary

        while frontRunner != None:
            frontRunner = frontRunner.next

            if frontRunner != None:
                frontRunner = frontRunner.next
                midPointer = midPointer.next

    leftHalf = sourceList
    rightHalf = midPointer.next
    midPointer.next = None

    return leftHalf, rightHalf

class _SingleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class _SingleLinkedListIter:
    def __init__(self, head):
        self.curNode = head 
    def __iter__(self):
        return self
    def next(self):
        if self.curNode is not None:
            curNode = self.curNode 
            self.curNode = self.curNode.next 
            return curNode.data 
        else:
            raise StopIteration
    
class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._count = 0

    # Get the length of single linked list
    def __len__(self):  
        return self._count
    
    # Get the item
    def __getitem__(self, pos):
        assert pos >= -1 and pos < len(self), \
                "invalid position!"
        preNode = self._head
        curNode = self._head 
        index = 0
        while curNode is not None and index < pos:
            preNode = curNode
            curNode = curNode.next 
            index += 1
            
        return preNode.data 
    
    # Get the length of single linked list
    def listLength(self):  
        return self._count

    # Check whether the sinlge linked list is empty
    def listIsEmpty(self):
        return self.listLength() == 0

    # Function to reverse the linked list
    def listReverseIter(self):
        prev = None
        current = self._head
        while(current is not None):
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self._head = prev
        
    def reverseUtil(self, curr, prev):
    
        # If last node mark it head
        if curr.next is None:
            self._head = curr
    
            # Update next to prev node
            curr.next = prev
            return
    
        # Save curr.next node for recursive call
        next_ = curr.next
    
        # And update next
        curr.next = prev
    
        self.reverseUtil(next_, curr)
    
    # This function mainly calls reverseUtil with previous as None
    def listReverseRecu(self):
        if self._head is None:
            return
        self.reverseUtil(self._head, None)
        
    # Insert node into single linked list  
    def listNodeInsertBak(self, data, position):
        
        newNode = _SingleLinkedListNode(data)
        if position == 0: # insert a node at the front
            newNode.next = self._head 
            self._head = newNode 
        elif position == -1: # insert a node at the end
            preNode = self._head
            curNode = self._head 
            while curNode is not None:
                preNode = curNode 
                curNode = curNode.next 
                
            preNode.next = newNode 
        else: # insert a node at middle
            listLen = self.listLength()
            assert position >= 1 and position <= listLen, \
                "position:%s is out of list length:%s" % (position, listLen)
                
            preNode = self._head 
            curNode = self._head
            index = 0 
            while curNode is not None and index < position:
                preNode = curNode 
                curNode = curNode.next 
                index += 1
                
            newNode.next = curNode 
            preNode.next = newNode 
            
        self._count += 1

    def listNodeInsert(self, data, position):
        assert position >= -1 and position <= len(self), \
             "Position is out of list length."
        newNode = _SingleLinkedListNode(data)
        if len(self) == 1:
            assert position == 0 or position == -1, \
                "position is out of range!"
            if position == 0:
                newNode.next = self._head 
                self._head = newNode
            elif position == -1:
                self._head.next = newNode  
                newNode.prev = self._head
        else:        
            if position == 0:
                if self.listIsEmpty():
                    self._head = newNode 
                else:
                    newNode.next = self._head
                    self._head = newNode
            elif position == -1:
                preNode = self._head
                curNode = self._head
                while curNode is not None:
                    preNode = curNode
                    curNode = curNode.next

                preNode.next = newNode
            else:                 
                preNode = self._head
                curNode = self._head
                index = 0
                while curNode.next is not None and index < position:
                    preNode = curNode
                    curNode = curNode.next
                    index += 1

                newNode.next = curNode
                preNode.next = newNode

        self._count += 1    
                        
    # Delete node from single linked list
    def listNodeDelete(self, position):
        
        assert not self.listIsEmpty(), "Single linked list is empty!"
        if self.listLength() == 1:
            assert position == 0 or position == -1, "position should be 0 or -1 when list length is 1!"
            self._head = None
        else:
            if position == 0:
                self._head = self._head.next 
            elif position == -1:
                preNode = self._head 
                curNode = self._head 
                while curNode.next is not None:
                    preNode = curNode 
                    curNode = curNode.next 
                
                preNode.next = curNode.next 
            else:
                preNode = self._head 
                curNode = self._head 
                index = 0
            
                assert position >=1 and position < self.listLength(), \
                   "positon:%s is out of list length:%s" % (position, self.listLength())
                while curNode.next is not None and index < position:
                    preNode = curNode 
                    curNode = curNode.next 
                    index += 1
                
                preNode.next = curNode.next    
            
        self._count -= 1

    def listTraversal(self):
        curNode = self._head 
        while curNode is not None:
            print "%s " % curNode.data,
            curNode = curNode.next 
        print '\r'

    def listClear(self):
        listLen = self.listLength()
        for _ in range(listLen):
            self.listNodeDelete(0)

    def __iter__(self):
        return _SingleLinkedListIter(self._head)
  
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self._head
        while(temp):
            print temp.data,
            temp = temp.next
            
def main():
 
    print ':::Insert sort the single Linked list'    
    stl = SingleLinkedList() 
    stl.listNodeInsert(5, 0)
    stl.listNodeInsert(20, 0)
    stl.listNodeInsert(4, 0)     
    stl.listNodeInsert(3, 0)
    stl.listNodeInsert(30, 0)    
    stl.listTraversal()

    head = insertSort(stl._head)
    while head is not None:
        print "%s " % head.data,
        head = head.next
        
    print '\r\r:::Quick sort for single linked list'
    stl = SingleLinkedList() 
    stl.listNodeInsert(5, 0)
    stl.listNodeInsert(20, 0)
    stl.listNodeInsert(4, 0)     
    stl.listNodeInsert(3, 0)
    stl.listNodeInsert(30, 0)    
    stl.listTraversal()

    head = quickSort(stl._head)
    while head is not None:
        print "%s " % head.data,
        head = head.next
    
    print '\r\r:::Merge sort for single linked list'
    stl = SingleLinkedList() 
    stl.listNodeInsert(5, 0)
    stl.listNodeInsert(20, 0)
    stl.listNodeInsert(4, 0)     
    stl.listNodeInsert(3, 0)
    stl.listNodeInsert(30, 0)    
    stl.listTraversal()

    head = mergeSort(stl._head)
    while head is not None:
        print "%s " % head.data,
        head = head.next
        
    print '\r\r:::new Merge sort for single linked list'
    stl = SingleLinkedList() 
    stl.listNodeInsert(5, 0)
    stl.listNodeInsert(20, 0)
    stl.listNodeInsert(4, 0)     
    stl.listNodeInsert(3, 0)
    stl.listNodeInsert(30, 0)    
    stl.listTraversal()

    head = mergeSortLinkedList(stl._head)
    while head is not None:
        print "%s " % head.data,
        head = head.next
            
'''
:::Insert sort the single Linked list
30  3  4  20  5  
3  4  5  20  30  

:::Quick sort for single linked list
30  3  4  20  5  
3  4  5  20  30  

:::Merge sort for single linked list
30  3  4  20  5  
3  4  5  20  30  

:::new Merge sort for single linked list
30  3  4  20  5  
3  4  5  20  30 
'''
if __name__ == '__main__':  
    main()  
