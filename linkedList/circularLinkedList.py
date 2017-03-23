import unittest

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
    
class TestDoubleLinkedList(unittest.TestCase):  
  
    def setUp(self):  
        self.cll = CircularLinkedList()
  
    def test_listLength(self):  
        print '\rLength check!'
        self.assertEqual(self.cll.listLength(), 0)  
        self.cll.listNodeInsert(1, 0)
        self.cll.listNodeInsert(2, 0)
        self.cll.listNodeInsert(3, 0)        
        self.cll.listTraversal()
        self.assertEqual(self.cll.listLength(), 3)    

    def test_listIsEmpty(self):
        print '\rEmpty check!'
        self.assertEqual(self.cll.listIsEmpty(), True)  
        self.cll.listNodeInsert(4, 0)
        self.cll.listNodeInsert(5, 0)
        self.cll.listNodeInsert(6, 0)     
        self.cll.listTraversal()
        self.assertEqual(self.cll.listIsEmpty(), False)  

    def test_listNodeInsert(self):
        print '\rInsert check!'
        self.cll.listNodeInsert(1, 0)
        self.cll.listNodeInsert(2, 0)
        self.cll.listTraversal()           
        self.cll.listNodeInsert(3, -1)
        self.cll.listNodeInsert(4, -1)
        self.cll.listTraversal()              
        self.cll.listNodeInsert(5, 3)
        self.cll.listNodeInsert(6, 2)   
        self.cll.listTraversal()               
        self.assertEqual(self.cll.listLength(), 6) 
        self.cll.listNodeInsert(7, 6)
        self.cll.listTraversal()               
        self.assertEqual(self.cll.listLength(), 7) 
                
    def test_listNodeDelete(self):
        print '\rDelete check!'
        self.cll.listNodeInsert(1, 0)
        self.cll.listNodeInsert(2, 0)
        self.cll.listTraversal()       
        self.cll.listNodeDelete(-1)
        self.cll.listTraversal()    
        self.cll.listNodeDelete(0)
        self.cll.listTraversal()   
        self.cll.listNodeInsert(1, 0)
        self.cll.listNodeInsert(2, 0)
        self.cll.listNodeInsert(3, 0)
        self.cll.listNodeInsert(4, 0)
        self.cll.listTraversal()       
        self.cll.listNodeDelete(2)
        self.cll.listTraversal()   
  
    def test_listIter(self):
        print '\rIter check'
        self.cll.listNodeInsert(1, 0)
        self.cll.listNodeInsert(2, 0)
        self.cll.listNodeInsert(3, 0)
        self.cll.listNodeInsert(4, 0)
        self.cll.listTraversal()
        for item in self.cll:
            print "%s " % item,
            
        print '\r'
'''
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
Ran 5 tests in 0.004s
'''       
if __name__ == '__main__':  
    unittest.main()  
