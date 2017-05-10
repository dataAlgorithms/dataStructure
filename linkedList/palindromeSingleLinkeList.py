'''
Check whether Single Linked List is Palindrome
1. Get the middle of the linked list.
2. Reverse the second half of the linked list.
3. Compare the first half and second half
'''
class Palindrome:
    def __init__(self, head):
        self._head = head

    # palindrome check
    def isPalindrome(self):
        
        head = self._head 
        
        # input check abcda abccba
        if head is None or head.next is None:
            return True

        # get the middle node
        middle = self.partition(head)
       
        # reverse the other half from middle node
        middle = self.reverse(middle)

        # compare
        while head is not None and middle is not None:
            if head.data != middle.data:
                return False

            head = head.next
            middle = middle.next

        return True

    # Get the middle node
    def partition(self, head):
        
        p = self._head
        while p.next is not None and p.next.next is not None:
            p = p.next.next
            head = head.next

        p = head.next
        head.next = None
        return p

    # Reverse the single linked list
    def reverse(self, head):

        if head is None or head.next is None:
            return head

        preNode = head
        curNode = head.next
        preNode.next = None
        
        while curNode is not None:
            nxtNode = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = nxtNode

        return preNode

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
  
def main(): 
  
    print '::Check <1 2 3 2 1>'
    stl = SingleLinkedList()
    stl.listNodeInsert('1', 0)    
    stl.listNodeInsert('2', 0)   
    stl.listNodeInsert('3', 0)   
    stl.listNodeInsert('2', 0)   
    stl.listNodeInsert('1', 0)      
    stl.listTraversal()
    
    pal = Palindrome(stl._head)
    print pal.isPalindrome()
 
    print '\r::Check <1 2 3 3 2 1>'
    stl = SingleLinkedList()
    stl.listNodeInsert('1', 0)    
    stl.listNodeInsert('2', 0)   
    stl.listNodeInsert('3', 0)   
    stl.listNodeInsert('3', 0) 
    stl.listNodeInsert('2', 0)   
    stl.listNodeInsert('1', 0)      
    stl.listTraversal()
    
    pal = Palindrome(stl._head)
    print pal.isPalindrome()
       
    print '\r::Check <a>'
    stl = SingleLinkedList()
    stl.listNodeInsert('a', 0)        
    stl.listTraversal()
    
    pal = Palindrome(stl._head)
    print pal.isPalindrome()
    
    print '\r::Check <b a>'
    stl = SingleLinkedList()
    stl.listNodeInsert('a', 0)  
    stl.listNodeInsert('b', 0)       
    stl.listTraversal()
    
    pal = Palindrome(stl._head)
    print pal.isPalindrome()
    
    print '\r::Check <a b a>'
    stl = SingleLinkedList()
    stl.listNodeInsert('a', 0)  
    stl.listNodeInsert('b', 0)  
    stl.listNodeInsert('a', 0)       
    stl.listTraversal()
    
    pal = Palindrome(stl._head)
    print pal.isPalindrome()
 
    print '\r::Check <c a b a>'
    stl = SingleLinkedList()
    stl.listNodeInsert('a', 0)  
    stl.listNodeInsert('b', 0)  
    stl.listNodeInsert('a', 0)  
    stl.listNodeInsert('c', 0)       
    stl.listTraversal()
    
    pal = Palindrome(stl._head)
    print pal.isPalindrome() 
    
if __name__ == '__main__':  
    main()  
