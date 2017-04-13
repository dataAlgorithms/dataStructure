# Function to reverse a Doubly linked list
def reverseList(head):

    temp = None
    current = head

    # Swap next and prev for all node of doubly linked list
    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    # Before changing head, check for the cases like
    # empty list and list with only one node
    if temp is not None:
        head = temp.prev

    return head

def listTraversal(head):
    curNode = head
    while curNode is not None:
        tmpNode = curNode.data
        print "%s " % tmpNode,
        curNode = curNode.next
    print '\r'
        
class _DoubleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class _DoubleLinkedListIter:
    def __init__(self, head):
        self._head = head
    def __iter__(self):
        return self
    def next(self):
        if self._head is not None:
            tmpNode = self._head.data
            self._head = self._head.next
            return tmpNode
        else:
            raise StopIteration

class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._count = 0

    def __len__(self):
        return self._count

    def listLength(self):
        return self._count 
    
    def listIsEmpty(self):
        return self._count == 0

    def listNodeInsertBak(self, data, position):
        assert position >= -1 and position <= len(self), \
             "Position is out of list length."
        newNode = _DoubleLinkedListNode(data)
        if position == 0:
            if self.listIsEmpty():
                self._head = newNode 
            else:
                newNode.next = self._head
                self._head.prev = newNode
                self._head = newNode
        elif position == -1:
            preNode = self._head
            curNode = self._head
            while curNode is not None:
                preNode = curNode
                curNode = curNode.next

            newNode.prev = preNode
            preNode.next = newNode
        else:
            if len(self) == 1:
                assert position == 0 or position == -1, \
                    "position is out of range!"
                if position == 0:
                    newNode.next = self._head 
                    self._head.prev = newNode 
                    self._head = newNode
                elif position == -1:
                    self._head.next = newNode  
                    newNode.prev = self._head
            else:
                preNode = self._head
                curNode = self._head
                index = 0
                while curNode.next is not None and index < position:
                    preNode = curNode
                    curNode = curNode.next
                    index += 1

                newNode.next = curNode
                newNode.prev = preNode
                preNode.next = newNode
                curNode.prev = newNode

        self._count += 1            

    def listNodeInsert(self, data, position):
        assert position >= -1 and position <= len(self), \
             "Position is out of list length."
        newNode = _DoubleLinkedListNode(data)
        if len(self) == 1:
            assert position == 0 or position == -1, \
                "position is out of range!"
            if position == 0:
                newNode.next = self._head 
                self._head.prev = newNode 
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
                    self._head.prev = newNode
                    self._head = newNode
            elif position == -1:
                preNode = self._head
                curNode = self._head
                while curNode is not None:
                    preNode = curNode
                    curNode = curNode.next

                newNode.prev = preNode
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
                newNode.prev = preNode
                preNode.next = newNode
                curNode.prev = newNode

        self._count += 1      
        
    def listNodeDelete(self, position):
        assert not self.listIsEmpty(), "List is empty!"
        assert position >= -1 and position < len(self), \
             "position is out of list range!"
        if len(self) == 1:
            assert position == 0 or position == -1, \
                    "Position is out of range!"
            self._head.next = None
            self._head.prev = None
            self._head = None
        else:
            if position == 0:
                self._head = self._head.next
                self._head.prev = None
            elif position == -1:
                preNode = self._head
                curNode = self._head
                while curNode.next is not None:
                    preNode = curNode
                    curNode = curNode.next

                preNode.next = None
                curNode.prev = None
            else:
                preNode = self._head
                curNode = self._head
                index = 0
                while curNode.next is not None and index < position:
                    preNode = curNode
                    curNode = curNode.next
                    index += 1

                preNode.next = curNode.next
                curNode.next.prev = preNode

        self._count -= 1

    def listClear(self):
        assert not self.listIsEmpty(), "List is Empty!"
        n = len(self)
        for _ in range(n):
            self.listNodeDelete(0)

    def listTraversal(self):
        curNode = self._head
        while curNode is not None:
            tmpNode = curNode.data
            print "%s " % tmpNode,
            curNode = curNode.next
        print '\r'

    def __iter__(self):
        return _DoubleLinkedListIter(self._head)
    
def main():
    
    dll = DoubleLinkedList()
    dll.listNodeInsert(1, 0)
    dll.listNodeInsert(2, 0)
    dll.listNodeInsert(3, 0)        
    dll.listTraversal()
    
    head = reverseList(dll._head)
    listTraversal(head)
        
'''
3  2  1  
1  2  3  
'''
if __name__ == '__main__':  
    main()  
