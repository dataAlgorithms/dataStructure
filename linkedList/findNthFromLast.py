'''
Find n'th node from the enf of a linked list
'''

'''
Method 1 (Brute force: Use length of linked list)
1) Calculate the length of linked list, let the length be len_
2) Print the len_ - n +1 node from the begining of the linked list
'''

def printNthFromLastBf(head, n):

    len_ = 0
    curNode = head 
 
    # Count the number of nodes
    while curNode is not None:
        curNode = curNode.next
        len_ += 1

    # Check if value of n is not more than length of the linked list
    if (len_ < n):
        return

    # 2) get the (n-len+1)th node from the begining (same as (n)th node from the end) 
    curNode = head
    for _ in range(1, len_ - n + 1):
        curNode = curNode.next

    print "%s" % curNode.data,

    return        

'''
Method 2: Recursive
'''
def printNthFromLastRec(head, n):

    global gi;
    if head is None:
        return
    printNthFromLastRec(head.next, n)
    gi += 1
    if (gi == n):
        print "%s" % head.data,    
        
'''
Method 3: Use two pointer
Maintain two pointer - reference pointer and main pointer
Initialize both reference and main pointers to head
First move reference pointer to n nodes from head 
Now move both pointers one by one until reference pointer reaches end
Now main pointer will point to nth node from the end
Return main pointer
'''
def printNthFromLastTP(head, n):

    main_ptr = head
    ref_ptr = head

    count = 0
    if head is not None:
        while (count < n):
            if ref_ptr is None:
                print "Few nodes"
                return
            ref_ptr = ref_ptr.next
            count += 1

    while ref_ptr is not None:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next
    print "%s" % main_ptr.data,
    
'''
Method 4
Use hash table
'''
    
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
               not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
        
# Find Nth node of linked list from the end
def printNthFromLastHT(head, n):
    
    len_ = 0
    curNode = head 
 
    # Count the number of nodes
    while curNode is not None:
        curNode = curNode.next
        len_ += 1

    # Check if value of n is not more than length of the linked list
    if (len_ < n):
        return
    
    # Use hash table to store key,value for nodeIndex,nodeValue
    ht = HashTable(len_)
    
    curNode = head 
    index = 0
    while curNode is not None:
        ht[index] = curNode.data 
        curNode = curNode.next 
        index += 1
        
    return ht[len_ -n]

'''
Use brute force:
a b c d e 

Use recursive:
a b c d e 

Use two pointer:
a b c d e 

Use hash table:
a b c d e
'''
if __name__ == "__main__":
    from singleLinkedList import SingleLinkedList as LinkedList
    sll = LinkedList()
    sll.listNodeInsert('a', 0)
    sll.listNodeInsert('b', 0)
    sll.listNodeInsert('c', 0) 
    sll.listNodeInsert('d', 0) 
    sll.listNodeInsert('e', 0) 
    
    print 'Use brute force:'
    for i in range(1, len(sll)+1):
        printNthFromLastBf(sll._head, i)
        
    print '\r\rUse recursive:'
    for i in range(1, len(sll)+1):     
        gi = 0
        printNthFromLastRec(sll._head, i)
        
    print '\r\rUse two pointer:'
    for i in range(1, len(sll)+1):
        printNthFromLastTP(sll._head, i)
        
    print '\r\rUse hash table:'
    for i in range(1, len(sll)+1):
        print printNthFromLastHT(sll._head, i),
