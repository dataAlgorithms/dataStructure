import unittest

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
    
class TestDoubleLinkedList(unittest.TestCase):  
  
    def setUp(self):  
        self.dll = DoubleLinkedList()
  
    def test_listLength(self):  
        print '\rLength check!'
        self.assertEqual(self.dll.listLength(), 0)  
        self.dll.listNodeInsert(1, 0)
        self.dll.listNodeInsert(2, 0)
        self.dll.listNodeInsert(3, 0)        
        self.dll.listTraversal()
        self.assertEqual(self.dll.listLength(), 3)    

    def test_listIsEmpty(self):
        print '\rEmpty check!'
        self.assertEqual(self.dll.listIsEmpty(), True)  
        self.dll.listNodeInsert(4, 0)
        self.dll.listNodeInsert(5, 0)
        self.dll.listNodeInsert(6, 0)     
        self.dll.listTraversal()
        self.assertEqual(self.dll.listIsEmpty(), False)  

    def test_listNodeInsert(self):
        print '\rInsert check!'
        self.dll.listNodeInsert(1, 0)
        self.dll.listNodeInsert(2, 0)
        self.dll.listTraversal()           
        self.dll.listNodeInsert(3, -1)
        self.dll.listNodeInsert(4, -1)
        self.dll.listTraversal()              
        self.dll.listNodeInsert(5, 3)
        self.dll.listNodeInsert(6, 2)   
        self.dll.listTraversal()               
        self.assertEqual(self.dll.listLength(), 6) 
        self.dll.listNodeInsert(7, 6)
        self.dll.listTraversal()               
        self.assertEqual(self.dll.listLength(), 7) 
                
    def test_listNodeDelete(self):
        print '\rDelete check!'
        self.dll.listNodeInsert(1, 0)
        self.dll.listNodeInsert(2, 0)
        self.dll.listTraversal()       
        self.dll.listNodeDelete(-1)
        self.dll.listTraversal()    
        self.dll.listNodeDelete(0)
        self.dll.listTraversal()   
        self.dll.listNodeInsert(1, 0)
        self.dll.listNodeInsert(2, 0)
        self.dll.listNodeInsert(3, 0)
        self.dll.listNodeInsert(4, 0)
        self.dll.listTraversal()       
        self.dll.listNodeDelete(2)
        self.dll.listTraversal()   
                
    def test_listClear(self):
        print '\rClear check'
        self.dll.listNodeInsert(1, 0)
        self.dll.listNodeInsert(2, 0)
        self.dll.listNodeInsert(3, 0)
        self.dll.listNodeInsert(4, 0)
        self.dll.listTraversal()
        self.dll.listClear()       
        self.dll.listTraversal() 
  
    def test_listIter(self):
        print '\rIter check'
        self.dll.listNodeInsert(1, 0)
        self.dll.listNodeInsert(2, 0)
        self.dll.listNodeInsert(3, 0)
        self.dll.listNodeInsert(4, 0)
        self.dll.listTraversal()
        for item in self.dll:
            print "%s " % item,
            
        print '\r'
     
'''
Finding files... done.
Importing test modules ... done.


Clear check
4  3  2  1  


Empty check!
6  5  4  

Iter check
4  3  2  1  
4  3  2  1  

Length check!
3  2  1  

Delete check!
2  1  
2  

4  3  2  1  
4  3  1  

Insert check!
2  1  
2  1  3  4  
2  1  6  3  5  4  
2  1  6  3  5  7  4  
----------------------------------------------------------------------
Ran 6 tests in 0.028s

OK
'''   
if __name__ == '__main__':  
    unittest.main()  
