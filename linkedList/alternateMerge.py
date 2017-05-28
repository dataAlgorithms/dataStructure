'''
Given two lists List1 = {A1, A2, ..., An} and
                list2 = {B1, B2, ..., Bm}
with data in ascending order

Merge them into the third list in ascending order so the merged list will be
{A1, B1, A2, B2, ...Am, Bm, Am+1...An} if n >= m
{A1, B1, A2, B2, ...An, Bn, Bn+1...Bm} if m >= n
'''
def alternateMerge(list1, list2):

    newNode = _SingleLinkedListNode(None)
    temp = newNode

    while list1 is not None and list2 is not None:
        temp.next = list1
        temp = temp.next
        list1 = list1.next
        temp.next = list2
        list2 = list2.next
        temp = temp.next

    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2

    temp = newNode.next
    return temp

def printList(head):
    
    while head is not None:
        print '%s ' % head.data, 
        head = head.next
        
'''
Merge a linked list into another linked list at alternate positions
Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should
 become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list
 should only be inserted when there are positions available. For example, if the first list is 1->2->3 and 
second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.

Use of extra space is not allowed (Not allowed to create additional nodes), i.e., 
insertion must be done in-place. Expected time complexity is O(n) where n is number of 
nodes in first list.

The idea is to run a loop while there are available positions in first loop and insert 
nodes of second list by changing pointers. Following are C and Java implementations of this approach.
'''
# Merge a linked list into another at alternate positions
class LinkedList:
    def __init__(self):
        self.head = None

    # Inserts a new Node at front of the list
    def push(self, new_data):
        new_node = _SingleLinkedListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # Main function that inserts nodes of linked list q into p at
    # alternate position, Since head of first list never changes
    # and head of second list/may change, we need single pointer
    # for first list and double pointer for second list
    def merge(self, q):
        p_curr = self.head
        q_curr = q.head

        # while there are available position in p
        while p_curr is not None and q_curr is not None:

            # Save next pointers
            p_next = p_curr.next
            q_next = q_curr.next

            # Make q_curr as next of p_curr
            q_curr.next = p_next # change next pointer of q_curr
            p_curr.next = q_curr # change next pointer of p_curr

            # Update current pointers for next iteration
            p_curr = p_next
            q_curr = q_next

        q.head = q_curr

    # Print linked list
    def printList(self):
        temp = self.head
        while temp is not None:
            print '%s ' % temp.data,
            temp = temp.next
        print ''

def test_new_alternateMerge():

    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)

    print "\r\rFirst linked list:"
    llist1.printList()

    llist2.push(8)
    llist2.push(7)
    llist2.push(6)
    llist2.push(5)
    llist2.push(4)

    print "\rSecond linked list:"
    llist2.printList()
    llist1.merge(llist2)

    print "\rModified first linked list:"
    llist1.printList()

    print "\rModified second linked list:"
    llist2.printList()
    
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
  
def test_alternateMerge():

    print ':::Equal size'
    stl = SingleLinkedList()
    stl.listNodeInsert(5, 0)
    stl.listNodeInsert(3, 0)
    stl.listNodeInsert(1, 0)
    stl.listTraversal()
    
    stl1 = SingleLinkedList()
    stl1.listNodeInsert(6, 0)
    stl1.listNodeInsert(4, 0)
    stl1.listNodeInsert(2, 0)
    stl1.listTraversal()  
         
    newList= alternateMerge(stl._head, stl1._head)
    printList(newList) 
    
    print '\r\r:::Above size'
    stl = SingleLinkedList()
    stl.listNodeInsert(7, 0)
    stl.listNodeInsert(5, 0)
    stl.listNodeInsert(3, 0)
    stl.listNodeInsert(1, 0)
    stl.listTraversal()
    
    stl1 = SingleLinkedList()
    stl1.listNodeInsert(4, 0)
    stl1.listNodeInsert(2, 0)
    stl1.listTraversal()  
         
    newList= alternateMerge(stl._head, stl1._head)
    printList(newList) 

    print '\r\r:::Less size'
    stl = SingleLinkedList()
    stl.listNodeInsert(3, 0)
    stl.listNodeInsert(1, 0)
    stl.listTraversal()
    
    stl1 = SingleLinkedList()
    stl1.listNodeInsert(8, 0)
    stl1.listNodeInsert(6, 0)
    stl1.listNodeInsert(4, 0)
    stl1.listNodeInsert(2, 0)
    stl1.listTraversal()  
         
    newList= alternateMerge(stl._head, stl1._head)
    printList(newList) 

'''
:::Equal size
1  3  5  
2  4  6  
1  2  3  4  5  6  

:::Above size
1  3  5  7  
2  4  
1  2  3  4  5  7  

:::Less size
1  3  
2  4  6  8  
1  2  3  4  6  8  

First linked list:
1  2  3  

Second linked list:
4  5  6  7  8  

Modified first linked list:
1  4  2  5  3  6  

Modified second linked list:
7  8  
'''                
if __name__ == '__main__':  
    test_alternateMerge()
    test_new_alternateMerge()  
