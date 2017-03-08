1. Single Linked list
class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __length__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self, item):
        newNode = SingleLinkedListNode(item)
        newNode.next = self._head
        self._head = newNode

        self._size += 1

    def insert(self, item, position):
        if position == 0:
            # insert at the beginning
            newNode = SingleLinkedListNode(item)
            newNode.next = self._head
            self._head = newNode

            self._size += 1

        elif position == -1:
            # insert at the ending
            newNode = SingleLinkedListNode(item)
            
            preNode = self._head
            curNode = self._head
            while curNode is not None:
                preNode = curNode
                curNode = curNode.next

            preNode.next = newNode
            
            self._size += 1

        else:
            # insert at the middle
            newNode = SingleLinkedListNode(item)
            if self._head is None:
                self._head  = newNode
                self._size += 1

            else:
                curNode = self._head
                preNode = self._head
                index = 0
                while curNode is not None and index != position:
                    preNode = curNode
                    curNode = curNode.next
                    index += 1

                newNode.next = curNode
                preNode.next = newNode
                self._size += 1

    def removePos(self, position):
        assert not self.isEmpty(), "LinkedList is empty!"
        if position == 0:
            # remove the first item
            self._head = self._head.next
            self._size -= 1
        elif position == -1:
            # remove the last item
            preNode = self._head
            curNode = self._head
            while curNode.next is not None:
                preNode = curNode
                curNode = curNode.next

            preNode.next = None
            self._size -= 1

        else:
            # remove the middle item
            preNode = self._head
            curNode = self._head
            index = 0
            while curNode is not None and index != position:
                preNode = curNode
                curNode = curNode.next

                index += 1

            preNode.next = curNode.next
            self._size -= 1

    def remove(self, item):
        assert not self.isEmpty(), "Linkedlist is empty!"
        preNode = self._head 
        curNode = self._head 
        while curNode is not None and curNode.item !=  item:
            preNode = curNode 
            curNode = curNode.next 
            
        assert curNode.item is not None, "item is not in!"
        if curNode is self._head:
            self._head = self._head.next 
        else:
            preNode.next = curNode.next 
        
        self._size -= 1
            
    def __iter__(self):
        return SingleLinkedListIer(self._head)

class SingleLinkedListNode:
    def __init__(self, item):
        self.item = item
        self.next = None
        
class SingleLinkedListIer:
    def __init__(self, head):
        self._head = head 
    def __iter__(self):
        return self 
    def next(self):
        if self._head is not None:
            curNode = self._head.item 
            self._head = self._head.next 
            return curNode 
        else:
            raise StopIteration
    
'''
smith: 
ECON-101 HIST-340 MATH-121 CSCI-112 

roberts: 
ECON-101 CSCI-112 ANTH-230 POL-101 

remove ECON-101 of smith


smith: 
HIST-340 MATH-121 CSCI-112 

remove MATH-121 of smith


smith: 
HIST-340 CSCI-112 

in check
True
False


insert pos check


smith: 
nihao HIST-340 CSCI-112 

smith: 
nihao HIST-340 CSCI-112 nihao 

smith: 
nihao HIST-340 nihao CSCI-112 nihao 

remove pos check


smith: 
HIST-340 nihao CSCI-112 nihao 

smith: 
HIST-340 nihao CSCI-112 

smith: 
HIST-340 CSCI-112
'''    
def test_linkedList():
    
    # init a set named smith
    smith = SingleLinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    print 'smith: '
    for item in smith:
        print item,
    
    # init a set named roberts
    roberts = SingleLinkedList()
    roberts.add('POL-101')
    roberts.add('ANTH-230')
    roberts.add('CSCI-112')
    roberts.add('ECON-101')
    
    print '\r\rroberts: '
    for item in roberts:
        print item,
        
    print '\r\rremove ECON-101 of smith'
    smith.remove('ECON-101')

    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rremove MATH-121 of smith'
    smith.remove('MATH-121')
            
    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rin check'
    print 'HIST-340' in smith 
    print 'MATH-121' in smith
    
    print '\r\rinsert pos check'
    item = 'nihao'
    smith.insert(item, 0)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
        
    item = 'nihao'
    smith.insert(item, -1)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
                
    item = 'nihao'
    smith.insert(item, 2)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
        
    print '\r\rremove pos check'
    item = 'nihao'
    smith.removePos(0)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
        
    item = 'nihao'
    smith.removePos(-1)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
                
    item = 'nihao'
    smith.removePos(1)
    
    print '\r\rsmith: '
    for item in smith:
        print item,   
            
if __name__ == "__main__":
    test_linkedList()
    
2. both linked list
class LinkedList:
    # Init
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def __length__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def __contains__(self, item):
        curNode = self._front
        while curNode is not None and curNode.item != item:
            curNode = curNode.next
        
        return curNode is not None
    
    def add(self, item):
        newNode = _LinkedListNode(item)
        if self._front is None:
            self._front = newNode
            self._back = newNode
            self._size += 1
        else:
            self._back.next = newNode
            self._back = newNode
            self._size += 1

    def remove(self, item):
        assert not self.isEmpty(), "Linked list is empty."
        preNode = None
        curNode = self._front
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next
        
        assert curNode.item == item, "item is not exits"
        preNode.next = curNode.next
        
        if curNode == self._back:
            self._back = preNode

        self._size -= 1

    def __iter__(self):
        return _LinkedListIter(self._front)

class _LinkedListIter:
    # Init
    def __init__(self, front):
        self._curNode = front
    def __iter__(self):
        return self
    def next(self):
        if self._curNode is not None:
            theItem = self._curNode.item
            self._curNode = self._curNode.next
            return theItem
        else:
            raise StopIteration

class _LinkedListNode:
    # Init
    def __init__(self, item):
        self.item = item
        self.next = None
        
def test_linkedListBag():
    
    # init a set named smith
    smith = LinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    print 'smith: '
    for item in smith:
        print item,
    
    # init a set named roberts
    roberts = LinkedList()
    roberts.add('POL-101')
    roberts.add('ANTH-230')
    roberts.add('CSCI-112')
    roberts.add('ECON-101')
    
    print '\r\rroberts: '
    for item in roberts:
        print item,
        
    print '\r\rremove ECON-101 of smith'
    smith.remove('ECON-101')

    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rremove MATH-121 of smith'
    smith.remove('MATH-121')
            
    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rin check'
    print 'HIST-340' in smith 
    print 'MATH-121' in smith
    
'''
smith: 
CSCI-112 MATH-121 HIST-340 ECON-101 

roberts: 
POL-101 ANTH-230 CSCI-112 ECON-101 

remove ECON-101 of smith


smith: 
CSCI-112 MATH-121 HIST-340 

remove MATH-121 of smith


smith: 
CSCI-112 HIST-340 

in check
True
False

'''
if __name__ == "__main__":
    test_linkedListBag()

3. double linked list
class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self, item):
        newNode = DoubleLinkedListNode(item)
        if self._head is None:
            self._head = newNode 
            self._size += 1
        else:
            newNode.next = self._head
            self._head.prev = newNode
            self._head = newNode
            self._size += 1

    def insert(self, item, position):
        newNode = DoubleLinkedListNode(item)
        if position == 0:
            newNode.next = self._head
            self._head.prev = newNode
            self._head = newNode
            self._size += 1
        elif position == -1:
            preNode = self._head
            curNode = self._head
            while curNode is not None:
                preNode = curNode
                curNode = curNode.next

            preNode.next = newNode
            newNode.prev = preNode
            self._size += 1
        else:
            preNode = self._head
            curNode = self._head
            index = 0
            while curNode is not None and index != position:
                preNode = curNode
                curNode = curNode.next
                index += 1

            newNode.next = curNode
            newNode.prev = preNode
            preNode.next = newNode
            curNode.prev = newNode

            self._size += 1

    def remove(self, item):
        assert not self.isEmpty(), "Linked list is empty!"
        preNode = self._head
        curNode = self._head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next

        if curNode is self._head:
            self._head = self._head.next
            self._size -= 1
        else:
            preNode.next = curNode.next
            self._size -= 1

    def __iter__(self):
        return DoubleLinkedListIter(self._head)

class DoubleLinkedListNode:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DoubleLinkedListIter:
    def __init__(self, head):
        self.head = head
    def __iter__(self):
        return self
    def next(self):
        if self.head is not None:
            curNode = self.head.item
            self.head = self.head.next
            return curNode
        else:
            raise StopIteration 
 
'''
primary smith
ECON-101
HIST-340
MATH-121
CSCI-112

deleted smith
ECON-101
MATH-121
CSCI-112

lenght of smith
3

check whether not in
False

check whether in
True

check insert
nihao
ECON-101
MATH-121
CSCI-112


nihao
ECON-101
MATH-121
CSCI-112
nihao


nihao
ECON-101
nihao
MATH-121
CSCI-112
nihao

check remove
ECON-101
nihao
MATH-121
CSCI-112
nihao
1111

ECON-101
MATH-121
CSCI-112
nihao
2222

ECON-101
MATH-121
CSCI-112
'''       
def test_doublelinkedlist():
    
    # init a linkedlist named smith
    smith = DoubleLinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    # print smith
    print 'primary smith'
    for item in smith:
        print item
        
    # remove one item
    smith.remove('HIST-340')
    
    # print smith
    print '\ndeleted smith'
    for item in smith:
        print item
        
    # pring length
    print '\nlenght of smith'
    print len(smith)
    
    # check whether not in
    print '\ncheck whether not in'
    print 'abc' in smith
 
    # check whether in
    print '\ncheck whether in'
    print 'ECON-101' in smith      
    
    # check insert
    print '\ncheck insert'
    item = 'nihao'
    smith.insert(item, 0)
    
    for item in smith:
        print item
        
    print '\n'
        
    item = 'nihao'
    smith.insert(item, -1)
    
    for item in smith:
        print item

    print '\n'
    
    item = 'nihao'
    smith.insert(item, 2)
    
    for item in smith:
        print item
        
    # check remove
    print '\ncheck remove'
    smith.remove('nihao')
    
    for item in smith:
        print item
       
    print '1111\n'
     
    smith.remove('nihao')
    
    for item in smith:
        print item
        
    print '2222\n'
     
    smith.remove('nihao')
    
    for item in smith:
        print item
if __name__ == "__main__":
    test_doublelinkedlist()

4. sorted circular linked list
class CircularSortedLinkedList:
    # Init
    def __init__(self):
        self._listRef = None
        self._size = 0
    # Length
    def __len__(self):
        return self._size
    # Check whether the list is empty
    def isEmpty(self):
        return self._size == 0
    # Check whether the item in the list
    def __contains__(self, item):
        curNode = self._listRef
        done = self._listRef is None 
        while not done:
            curNode = curNode.next
            if curNode.value == item:
                return True 
            else:
                done = curNode is self._listRef or curNode.value > item
                
        return False

    # Add operation
    def add(self, item):
        newnode = _DLinkListNode(item)
        if self._listRef is None:
            self._listRef = newnode
            newnode.next = newnode
        elif item < self._listRef.next.value:
            newnode.next = self._listRef.next
            self._listRef.next = newnode
        elif item > self._listRef.value:
            newnode.next = self._listRef.next
            self._listRef.next = newnode
            self._listRef = newnode
        else:
            preNode = None
            curNode = self._listRef
            done = self._listRef is None
            while not done:
                preNode = curNode
                curNode = curNode.next
                done = curNode is self._listRef or curNode.value > item
            newnode.next = curNode
            preNode.next = newnode
        self._size += 1
        
    # Remove operation
    def remove(self, item):
        assert item in self, "item is not in"
        
        if self._listRef is None:
            return False
        elif item == self._listRef.next.value:
            self._listRef.next = self._listRef.next.next
        elif item == self._listRef.value:
            preNode = None
            curNode = self._listRef
            done = self._listRef is None
            while not done:
                preNode = curNode
                curNode = curNode.next
                done = curNode is self._listRef
            preNode.next = self._listRef.next
            self._listRef = preNode
        else:
            preNode = None
            curNode = self._listRef.next
            done = self._listRef  is None
            while not done:
                preNode = curNode
                curNode = curNode.next
                done = curNode is self._listRef or curNode.value == item
            preNode.next = curNode.next
        self._size -= 1
    # Iter
    def __iter__(self):
        return _CircularSortedLinkedListIter(self._listRef, self._size)

# Iter
class _CircularSortedLinkedListIter:
    # Init
    def __init__(self, listRef, size):
        self._curNode = listRef.next
        self._size = size 
        self._cIndex = 0
    def __iter__(self):
        return self
    def next(self):
        if self._cIndex < self._size:
            value = self._curNode.value
            self._curNode = self._curNode.next
            self._cIndex += 1
            return value
        else:
            raise StopIteration

# Node
class _DLinkListNode:
    # Init
    def __init__(self, item):
        self.value = item
        self.next = None
        
def test_sortedcircularlinkedlist():
    
    # init a linkedlist named smith
    smith = CircularSortedLinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    # print smith
    print 'primary smith'
    for item in smith:
        print item
        
    # remove one item
    smith.remove('MATH-121')
    smith.remove('HIST-340')
        
    # print smith
    print '\ndeleted smith'
    for item in smith:
        print item
        
    # pring length
    print '\nlenght of smith'
    print len(smith)
    
    # check whether not in
    print '\ncheck whether not in'
    print 'abc' in smith
 
    # check whether in
    print '\ncheck whether in'
    print 'ECON-101' in smith       
    
    # delete all
    smith.remove('CSCI-112')
    smith.remove('ECON-101')
    
    for item in smith:
        print item
        
if __name__ == "__main__":
    test_sortedcircularlinkedlist()

5. circular linked list
class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self, item):
        newNode = _CircularLinkedListNode(item)
        if self._head is None:
            newNode.next = newNode 
            self._head = newNode 
            self._size += 1
        else:
            curNode = self._head 
            while curNode.next is not self._head:
                curNode = curNode.next 
            
            curNode.next = newNode 
            newNode.next = self._head
            self._size += 1
            
    def insertPos(self, pos, item):
        newNode = _CircularLinkedListNode(item)
        if pos == 0:
            # insert at the front
            curNode = self._head
            while curNode.next is not self._head:
                curNode = curNode.next

            curNode.next = newNode
            newNode.next = self._head
            self._head = newNode
            self._size += 1
        elif pos == -1:
            # insert at the end
            curNode = self._head
            while curNode.next is not self._head:
                curNode = curNode.next
            curNode.next = newNode
            newNode.next = self._head

            self._size += 1
        else:
            # insert at the pos position
            preNode = self._head
            curNode = self._head
            index = 0
            while curNode.next is not self._head and index != pos:
                preNode = curNode
                curNode = curNode.next    
                index += 1        
 
            assert curNode.next is not self._head, "pos is not exist!"
            preNode.next = newNode
            newNode.next = curNode

            self._size += 1

    def deletePos(self, pos):
        assert not self.isEmpty(), "Circurlar linked list is empty"
        if pos == 0:
            # delete the item at the front
            curNode = self._head
            while curNode.next is not self._head:
                curNode = curNode.next

            curNode.next = self._head.next
            self._head = self._head.next
            self._size -= 1
        elif pos == -1:
            # delete the item at the end
            preNode = self._head
            curNode = self._head
            while curNode.next is not self._head:
                preNode = curNode
                curNode = curNode.next

            preNode.next = self._head
            self._size -= 1
        else:
            # delete the item at the pos position
            preNode = self._head
            curNode = self._head
            index = 0
            while curNode.next is not self._head and index != pos:
                preNode = curNode
                curNode = curNode.next
                index += 1

            assert curNode.next is not self._head, "pos is not exist!"
            preNode.next = curNode.next
            self._size -= 1 

    def remove(self, item):
        assert not self.isEmpty(), "Linked list is empty!"
        preNode = self._head
        curNode = self._head
        while curNode.next is not self._head and curNode.item != item:
            preNode = curNode
            curNode = curNode.next        

        assert curNode.item == item, "item is not exist!"
        if curNode is self._head:
            preNode.next = self._head.next
            self._head = self._head.next
            self._size -= 1
        else:
            preNode.next = curNode.next        
            self._size -= 1

    def __iter__(self):
        return _CircularLinkedListIter(self._head, self._size)

class _CircularLinkedListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class _CircularLinkedListIter:
    def __init__(self, head, size):
        self._head = head
        self._size = size 
        self._cIndex = 0
        self._curNode = head
    def __iter__(self):
        return self
    def next(self):
        if self._cIndex < self._size:
            tmpNode = self._curNode
            self._curNode = self._curNode.next
            self._cIndex += 1
            return tmpNode.item
        else:
            raise StopIteration
        
def test_circularlinkedlist():
    
    # init a linkedlist named smith
    smith = CircularLinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    # print smith
    print 'primary smith'
    for item in smith:
        print item
        
    # remove one item
    smith.remove('MATH-121')
    smith.remove('HIST-340')
        
    # print smith
    print '\ndeleted smith'
    for item in smith:
        print item
        
    # pring length
    print '\nlenght of smith'
    print len(smith)
    
    # check whether not in
    print '\ncheck whether not in'
    print 'abc' in smith
 
    # check whether in
    print '\ncheck whether in'
    print 'ECON-101' in smith       
        
    # insert 
    smith.insertPos(0, 'nihao')
    for item in smith:
        print item    
    
    print '\r'    
    smith.insertPos(-1, 'nihao')
    
    for item in smith:
        print item    
    print '\r' 
            
    smith.insertPos(1, 'nihao')

    for item in smith:
        print item    
    print '\r'
    
    # deletePos
    smith.deletePos(0)
    for item in smith:
        print item    
    print '\r'

    smith.deletePos(-1)
    for item in smith:
        print item    
    print '\r'
                
    # delete all
    smith.remove('CSCI-112')
    smith.remove('ECON-101')
    
    for item in smith:
        print item
     
'''
primary smith
CSCI-112
MATH-121
HIST-340
ECON-101

deleted smith
CSCI-112
ECON-101

lenght of smith
2

check whether not in
False

check whether in
True
nihao
CSCI-112
ECON-101

nihao
CSCI-112
ECON-101
nihao

nihao
nihao
CSCI-112
ECON-101
nihao

nihao
CSCI-112
ECON-101
nihao

nihao
CSCI-112
ECON-101

nihao
'''       
if __name__ == "__main__":
    test_circularlinkedlist()

6. xor double linked list
'''
refer:
http://eddmann.com/posts/implementing-a-xor-doubly-linked-list-in-c/
http://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-2/


address to value
1. ctypes
import ctypes
a = "hello world"
print ctypes.cast(id(a), ctypes.py_object).value

2. globals
var = 'I need to be accessed by id!'
address = id(var)
print(address)
var2 = [x for x in globals().values() if id(x)==address]
'''

'''
c code and make
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct node {
    int item;
    struct node *np;
} node;

node *head, *tail;

node *xor(node *a, node *b)
{
    return (node*) ((uintptr_t) a ^ (uintptr_t) b);
}

void insert(int item, bool at_tail)
{
    node *ptr = (node*) malloc(sizeof(node));
    ptr->item = item;

    if (NULL == head) {
        ptr->np = NULL;
        head = tail = ptr;
    } else if (at_tail) {
        ptr->np = xor(tail, NULL);
        tail->np = xor(ptr, xor(tail->np, NULL));
        tail = ptr;
    } else {
        ptr->np = xor(NULL, head);
        head->np = xor(ptr, xor(NULL, head->np));
        head = ptr;
    }
}

int delete(bool from_tail)
{
    if (NULL == head) {
        printf("Empty list.\n");
        exit(1);
    } else if (from_tail) {
        node *ptr = tail;
        int item = ptr->item;
        node *prev = xor(ptr->np, NULL);
        if (NULL == prev) head = NULL;
        else prev->np = xor(ptr, xor(prev->np, NULL));
        tail = prev;
        free(ptr);
        ptr = NULL;
        return item;
    } else {
        node *ptr = head;
        int item = ptr->item;
        node *next = xor(NULL, ptr->np);
        if (NULL == next) tail = NULL;
        else next->np = xor(ptr, xor(NULL, next->np));
        head = next;
        free(ptr);
        ptr = NULL;
        return item;
    }
}

void list()
{
    node *curr = head;
    node *prev = NULL, *next;

    while (NULL != curr) {
        printf("%d ", curr->item);
        next = xor(prev, curr->np);
        prev = curr;
        curr = next;
    }

    printf("\n");
}

int main(int argc, char *argv[])
{
    int i;
    for (i = 1; i <= 10; i++)
        insert(i, i < 6);

    list(); // 10 9 8 7 6 1 2 3 4 5

    for (i = 1; i <= 4; i++)
        delete(i < 3);

    list(); // 8 7 6 1 2 3
}

Make: (linux)
gcc -c -fPIC xorDBL.c 
gcc -shared xorDBL.o -o xorDBL.so

Python call C: (linux)
>>> from ctypes import *
>>> import os
>>> libtest = cdll.LoadLibrary(os.getcwd() + '/xorDBL.so')
>>> libtest
<CDLL '/root/tmp/xorDBL.so', handle 1aace240 at 2b8d2d315f90>
>>> dir(libtest)
['_FuncPtr', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_func_flags_', '_func_restype_', '_handle', '_name']
>>> libtest.main()
10 9 8 7 6 1 2 3 4 5 
8 7 6 1 2 3 
10
>>> 


Python call c refer:
http://www.bjhee.com/python-ctypes.html
http://coolshell.cn/articles/671.html
'''

7. unrolled linked list 
'''
Java: (not verify by now)
/*
 *  Java Program to Implement Unrolled Linked List
 */
 
import java.util.Scanner;
 
/*  Class ULLNode  */
class ULLNode    
{
    ULLNode next;
    int numElements;
    int array[];
 
    /* Constructor */
    public ULLNode(int n)
    {
        next = null;
        numElements = 0;
        array = new int[n];        
    }
}
 
/* Class UnrolledLinkedList */
class UnrolledLinkedList
{
    private ULLNode start;
    private ULLNode end;
    private int sizeNode;
    private int nNode;
 
    /* Constructor */
    public UnrolledLinkedList(int capacity)
    {
        start = null;
        end = null;
        nNode = 0;
        sizeNode = capacity + 1;
    }
    /*  Function to check if list is empty  */
    public boolean isEmpty()
    {
        return start == null;
    }
    /*  Function to get size of list  */
    public int getSize()
    {
        return nNode;
    }  
    /* Function to clear list */
    public void makeEmpty()
    {
        start = null;
        end = null;
        nNode = 0;
    }
    /* Function to insert element */
    public void insert(int x)
    {
        nNode++;
        if (start == null)
        {
            start = new ULLNode(sizeNode);
            start.array[0] = x;
            start.numElements++;
            end = start;
            return;
        }
        if (end.numElements + 1 < sizeNode)
        {
            end.array[end.numElements] = x;
            end.numElements++;                        
        }
        else
        {
            ULLNode nptr = new ULLNode(sizeNode);
            int j = 0;
            for (int i = end.numElements / 2 + 1; i < end.numElements; i++)
                nptr.array[j++] = end.array[i];
            nptr.array[j++] = x;
            nptr.numElements = j;
            end.numElements = end.numElements/2 + 1;
            end.next = nptr;  
            end = nptr;          
        }        
    }
    /* Function to display list */
    public void display()
    {
        System.out.print("\nUnrolled Linked List = ");
        if (nNode == 0) 
        {
            System.out.print("empty\n");
            return;
        }
        System.out.println();
        ULLNode ptr = start;
        while (ptr != null)
        {
            for (int i = 0; i < ptr.numElements; i++)
                System.out.print(ptr.array[i] +" ");
            System.out.println();            
            ptr = ptr.next;
        }
    }
 
}
 
/*  Class UnrolledLinkedListTest  */
public class UnrolledLinkedListTest
{    
    public static void main(String[] args)
    {             
        Scanner scan = new Scanner(System.in);
        System.out.println("Unrolled Linked List Test\n");  
        System.out.println("Enter array size of each node");       
        /* Creating object of class UnrolledLinkedList */
        UnrolledLinkedList ull = new UnrolledLinkedList(scan.nextInt() ); 
 
        char ch;
        /*  Perform list operations  */
        do
        {
            System.out.println("\nUnrolled Linked List Operations\n");
            System.out.println("1. insert");
            System.out.println("2. check empty");
            System.out.println("3. get size");  
            System.out.println("4. clear");            
            int choice = scan.nextInt();            
            switch (choice)
            {
            case 1 :  
                System.out.println("Enter integer element to insert");
                ull.insert( scan.nextInt() );                     
                break;                          
            case 2 : 
                System.out.println("Empty status = "+ ull.isEmpty());
                break;                   
            case 3 : 
                System.out.println("Size = "+ ull.getSize() +" \n");
                break; 
            case 4 : 
                System.out.println("List Cleared\n");
                ull.makeEmpty();
                break;                        
            default : 
                System.out.println("Wrong Entry \n ");
                break;   
            }
            /*  Display List  */ 
            ull.display();
 
            System.out.println("\nDo you want to continue (Type y or n) \n");
            ch = scan.next().charAt(0);                        
        } while (ch == 'Y'|| ch == 'y');               
    }
}
Unrolled Linked List Test
 
Enter array size of each node
5
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
23
 
Unrolled Linked List =
23
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
7
 
Unrolled Linked List =
23 7
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
87
 
Unrolled Linked List =
23 7 87
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
19
 
Unrolled Linked List =
23 7 87 19
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
24
 
Unrolled Linked List =
23 7 87 19 24
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
6
 
Unrolled Linked List =
23 7 87
19 24 6
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
94
 
Unrolled Linked List =
23 7 87
19 24 6 94
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
28
 
Unrolled Linked List =
23 7 87
19 24 6 94 28
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
5
 
Unrolled Linked List =
23 7 87
19 24 6
94 28 5
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
1
Enter integer element to insert
63
 
Unrolled Linked List =
23 7 87
19 24 6
94 28 5 63
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
3
Size = 10
 
 
Unrolled Linked List =
23 7 87
19 24 6
94 28 5 63
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
4
List Cleared
 
 
Unrolled Linked List = empty
 
Do you want to continue (Type y or n)
 
y
 
Unrolled Linked List Operations
 
1. insert
2. check empty
3. get size
4. clear
2
Empty status = true
 
Unrolled Linked List = empty
 
Do you want to continue (Type y or n)
 
n
'''

'''
c language (not work by now)

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int blockSize; //max number of nodes in a block

struct ListNode {
    struct ListNode *next;
    int value;
};

struct LinkedBlock {
    struct LinkedBlock *next;
    struct ListNode *head;
    int nodeCount;
};

struct LinkedBlock *blockHead;

//create an empty block
struct LinkedBlock *newLinkedBlock() {
    struct LinkedBlock *block=(struct LinkedBlock*)malloc(sizeof(struct LinkedBlock));
    block->next = NULL;
    block->head = NULL;
    block->nodeCount = 0;
    return block;
}

//create a node
struct ListNode* newListNode(int value) {
    struct ListNode* temp=(struct ListNode*)malloc(sizeof(struct ListNode));
    temp->next = NULL;
    temp->value = value;
    return temp;
}

int searchElementVoid(int k, struct LinkedBlock **fLinkedBlock, struct ListNode **fListNode) {
    //find the block
    int j = (k+blockSize-1)/blockSize; //kth node is in the jth block
    struct LinkedBlock* p = blockHead;

    if(blockHead == NULL) {
    	return -1;
	}
	
    while(--j) {
        p = p->next;
        if(p == NULL) {
        	return -1;
		}
    }

    *fLinkedBlock = p;

    //find the node
    struct ListNode *q = p->head;
    k = k%blockSize;
    if(k==0) k = blockSize;
    k=p->nodeCount+1-k;
    
    while(k--) {
        q = q->next;
    }

    *fListNode = q;
    
    return 0;
}

//start shift operation from block *p
void shift(struct LinkedBlock *A) {
    struct LinkedBlock *B;
    struct ListNode* temp;
    while(A->nodeCount > blockSize) {//if this block still have to shift
        if(A->next == NULL){//reach the end. A little different
            A->next=newLinkedBlock();
            B=A->next;
            temp=A->head->next;
            A->head->next=A->head->next->next;
            B->head=temp;
            temp->next=temp;
            A->nodeCount--;
            B->nodeCount++;
        } else {
            B=A->next;
            temp = A->head->next;
            A->head->next=A->head->next->next;
            temp->next=B->head->next;
            B->head->next=temp;
            B->head=temp;
            A->nodeCount--;
            B->nodeCount++;
        }
        A=B;
    }
}

void addElement(int k, int x) {
    struct ListNode *p, *q;
    struct LinkedBlock *r;

    if(!blockHead) {//initial,first node and block
        blockHead=newLinkedBlock();
        blockHead->head=newListNode(x);
        blockHead->head->next=blockHead->head;
        blockHead->nodeCount++;
    }else {
        if(k==0) {//special case for k=0
            p = blockHead->head;
            q = p->next;
            p->next=newListNode(x);
            p->next->next=q;
            blockHead->head=p->next;
            blockHead->nodeCount++;
            shift(blockHead);
        }else {
            searchElementVoid(k,&r,&p);
            q = p;
            while(q->next!=p) q = q->next;
            q->next=newListNode(x);
            q->next->next=p;
            r->nodeCount++;
            shift(r);
       }
    }
}

int searchElement(int k) {
	int flag = 0;
	
    struct ListNode *p;
    struct LinkedBlock *q;
    flag = searchElementVoid(k, &q, &p);
    if(flag != -1) {
        return p->value;
    } else {
    	return -1;
	}
}

int testUnRolledLinkedList() {
    int tt=clock();
    int m, i, k, x;
    char cmd[10];
    int flag;
    printf("Count of doing cmd: ");
    scanf("%d", &m);
    blockSize = (int)(sqrt(m-0.001))+1;

    for(i=0; i<m; i++) {
    	printf("Please input cmd, eg, add, search.\n");
        scanf("%s", cmd);
        if(strcmp(cmd,"add")==0) {
        	printf("Doing add, please input two number at once\n");
            scanf("%d %d", &k, &x);
            addElement(k, x);
        } else if(strcmp(cmd, "search")== 0) {
        	printf("Doing search, please input the query number!\n");
            scanf("%d", &k);
            flag = searchElement(k);
            if(flag != -1) {
                printf("%d\n", searchElement(k));
            } else {
            	printf("No item!\n");
			}
        } else {
            fprintf(stderr, "Wrong Input\n");
        }
    }

    return 0;
}

int main() 
{
    testUnRolledLinkedList();    
}
'''
