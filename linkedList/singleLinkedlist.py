import unittest

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
    def listLength(self):  
        return self._count

    # Check whether the sinlge linked list is empty
    def listIsEmpty(self):
        return self.listLength() == 0

    # Insert node into single linked list  
    def listNodeInsert(self, data, position):
        
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
  
class TestSingleLinkedList(unittest.TestCase):  
  
    def setUp(self):  
        self.stl = SingleLinkedList()
  
    def test_listLength(self):  
        print '\rLength check!'
        self.assertEqual(self.stl.listLength(), 0)  
        self.stl.listNodeInsert(1, 0)
        self.stl.listNodeInsert(2, 0)
        self.stl.listNodeInsert(3, 0)        
        self.stl.listTraversal()
        self.assertEqual(self.stl.listLength(), 3)    

    def test_listIsEmpty(self):
        print '\rEmpty check!'
        self.assertEqual(self.stl.listIsEmpty(), True)  
        self.stl.listNodeInsert(4, 0)
        self.stl.listNodeInsert(5, 0)
        self.stl.listNodeInsert(6, 0)     
        self.stl.listTraversal()
        self.assertEqual(self.stl.listIsEmpty(), False)  

    def test_listNodeInsert(self):
        print '\rInsert check!'
        self.stl.listNodeInsert(1, 0)
        self.stl.listNodeInsert(2, 0)
        self.stl.listTraversal()           
        self.stl.listNodeInsert(3, -1)
        self.stl.listNodeInsert(4, -1)
        self.stl.listTraversal()              
        self.stl.listNodeInsert(5, 3)
        self.stl.listNodeInsert(6, 2)   
        self.stl.listTraversal()               
        self.assertEqual(self.stl.listLength(), 6) 
        self.stl.listNodeInsert(7, 6)
        self.stl.listTraversal()               
        self.assertEqual(self.stl.listLength(), 7) 
                
    def test_listNodeDelete(self):
        print '\rDelete check!'
        self.stl.listNodeInsert(1, 0)
        self.stl.listNodeInsert(2, 0)
        self.stl.listTraversal()       
        self.stl.listNodeDelete(-1)
        self.stl.listTraversal()    
        self.stl.listNodeDelete(0)
        self.stl.listTraversal()   
        self.stl.listNodeInsert(1, 0)
        self.stl.listNodeInsert(2, 0)
        self.stl.listNodeInsert(3, 0)
        self.stl.listNodeInsert(4, 0)
        self.stl.listTraversal()       
        self.stl.listNodeDelete(2)
        self.stl.listTraversal()   
                
    def test_listClear(self):
        print '\rClear check'
        self.stl.listNodeInsert(1, 0)
        self.stl.listNodeInsert(2, 0)
        self.stl.listNodeInsert(3, 0)
        self.stl.listNodeInsert(4, 0)
        self.stl.listTraversal()
        self.stl.listClear()       
        self.stl.listTraversal() 
  
    def test_listIter(self):
        print '\rIter check'
        self.stl.listNodeInsert(1, 0)
        self.stl.listNodeInsert(2, 0)
        self.stl.listNodeInsert(3, 0)
        self.stl.listNodeInsert(4, 0)
        self.stl.listTraversal()
        for item in self.stl:
            print "%s " % item,
            
        print '\r'
        
        
'''
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK

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
2  1  6  3  5  4  7  
'''            
if __name__ == '__main__':  
    unittest.main()  
