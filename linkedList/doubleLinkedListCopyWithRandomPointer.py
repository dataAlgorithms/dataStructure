'''
Clone a linked list with next and random pointer

Given a linked list having two pointers in each node. 
The first one points to the next node of the list, 
however the other pointer is random and can point to any node of the list.
'''

'''
Create the copy of node 1 and insert it between node 1 & node 2 in original Linked List, create the copy of 2 and insert it between 2 & 3.. Continue in this fashion, add the copy of N afte the Nth node
Now copy the random link in this fashion
original->next->random= original->random->next;  /*TRAVERSE TWO NODES*/
This works because original->next is nothing but copy of original and Original->random->next is nothing but copy of random.

Now restore the original and copy linked lists in this fashion in a single loop.
original->next = original->next->next;
copy->next = copy->next->next;
Ensure that original->next is NULL and return the cloned list

refer:http://www.geeksforgeeks.org/clone-linked-list-next-random-pointer-o1-space/
'''
def cloneWithoutExtraSpace(head):

    curr = head
    temp = None

    # insert additional node after every node of original list
    while curr is not None:
        temp = curr.next

        # Insert node
        curr.next = Node(curr.data)
        curr.next.next = temp
        curr = temp

    curr = head

    # adjust the random pointers of the newly added node
    while curr is not None:
        curr.next.random = curr.random.next

        # move to the next newly added node by 
        # skipping an original node
        if curr.next is not None:
            curr = curr.next.next
        else:
            curr = curr.next

    original = head
    copy = head.next

    # save the start of copied linked list
    temp = copy

    # new separate the original list and copied list
    while original is not None and copy is not None:
        if original.next is not None:
            original.next = original.next.next
        else:
            original.next = original.next

        if copy.next is not None:
            copy.next = copy.next.next
        else:
            copy.next = copy.next

        original = original.next
        copy = copy.next

    return temp

# Utility function to print the list
def printList(start):
    
    ptr = start 
    while ptr is not None:
        print "Data = " + str(ptr.data) + ", Random = " + str(ptr.random.data)
        ptr = ptr.next 
        
class Entry:
    """ Entry
        Used in every hashtable but the ChainedHashtable, an Entry is a key, value pair
    """

    def __str__(self):
        return str(self.value)

    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        
def DoubleHash(key, i, size):
    return int((DivisionHash(key, size) + i * AuxiliaryHash2(key, size)) % size)

def AuxiliaryHash2(key, size):
    return 1 + (key % (size - 1))

def DivisionHash(key, size):
    return key % size

class DoubleHashtable:
    size = 31

    def __init__(self):
        self.entries = [None] * DoubleHashtable.size

    def get(self, key):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while entry is None or entry.key != key:
            i += 1
            if i == DoubleHashtable.size:
                return None
            entry = self.entries[self.hash(key, i)]
        return entry.value

    def put(self, key, value):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while entry is not None and entry.key != key:
            i += 1
            if i+1 == DoubleHashtable.size:
                return
            entry = self.entries[self.hash(key, i)]
        if entry is None:
            entry = Entry(key=key, value=value)
            self.entries[self.hash(key, i)] = entry
        else:
            entry.value = value

    def search(self, key):
        i = 0
        search_result = ""
        entry = self.entries[self.hash(key, i)]
        search_result = str(self.hash(key, i)) + " "
        while entry is None or entry.key != key:
            i += 1
            if i+1 == DoubleHashtable.size:
                return search_result + "-1"
            entry = self.entries[self.hash(key, i)]
            search_result += str(self.hash(key, i)) + " "
        return search_result

    def insert(self, value):
        self.put(value, value)

    def hash(self, key, i):
        return DoubleHash(key, i, DoubleHashtable.size)

    def __str__(self):
        lines = []
        for i in range(len(self.entries)):
            if self.entries[i] is None:
                lines.append("" + str(i) + "\t" + "-1")
            else:
                lines.append("" + str(i) + "\t" + str(self.entries[i].value))
        return "\n".join(lines)

# Linked List Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

# Linked List class
class LinkedList:
    # Linked list constructor
    def __init__(self, head):
        self.head = head

    # push method to put data always at the head
    # in the linked list
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # method to print the list
    def printList(self):
        temp = self.head
        while temp is not None:
            random = temp.random
            if random is not None:
                randomData = random.data
            else:
                randomData = -1
            
            print "Data = " + str(temp.data) + ", Random data = " + str(randomData)

            temp = temp.next
 
    '''
    Actual clone method which returns head reference of cloned linked list
    
    The idea is to use Hashing. Below is algorithm.
    1. Traverse the original linked list and make a copy in terms of data.
    2. Make a hash map of key value pair with original linked list node and copied linked list node.
    3. Traverse the original linked list again and using the hash map adjust the next and random reference of cloned linked list nodes.
    
    Time complexity : O(n)
    Auxiliary space : O(n)
    
    refer:http://www.geeksforgeeks.org/clone-linked-list-next-arbit-pointer-set-2/
    '''
    def dllCloneUseHash(self):
    
        # Initialize two references, one with original list head
        origCurr = self.head
        cloneCurr = None
    
        # Hash Map with contains node to node mapping of original and clone linked list
        newMap = DoubleHashtable()
    
        # Traverse the original list and make a copy of that in the clone linked list
        while origCurr is not None:
            cloneCurr = Node(origCurr.data)
            newMap.put(id(origCurr), cloneCurr)
            origCurr = origCurr.next
    
        # Adjust the original list reference again
        origCurr = self.head
    
        # Traversal of original list again to adjust the next
        # and random references of clone list using hash map
        while origCurr is not None:
            cloneCurr = newMap.get(id(origCurr))
            cloneCurr.next = newMap.get(id(origCurr.next))
            cloneCurr.random = newMap.get(id(origCurr.random))
            origCurr = origCurr.next
    
        # Return the head reference of the clone list 
        return LinkedList(newMap.get(id(self.head)))

# Driver class
def main():

    # Push data in the linked list
    aList = LinkedList(Node(5))
    aList.push(4)
    aList.push(3)
    aList.push(2)
    aList.push(1)

    # Setting up random references
    aList.head.random = aList.head.next.next
    aList.head.next.random = aList.head.next.next.next
    aList.head.next.next.random = aList.head.next.next.next.next
    aList.head.next.next.next.random = aList.head.next.next.next.next.next
    aList.head.next.next.next.next.random = aList.head.next
            
    # Make a clone of the original linked list
    cloneList = aList.dllCloneUseHash()

    # Print the original and cloned linked list
    print ":::Original linked list"
    aList.printList()

    print "\r\r:::Cloned linked list using hash (with extra space)"
    cloneList.printList()
    
    # create a new list
    start = Node(1)
    start.next = Node(2)
    start.next.next = Node(3)
    start.next.next.next = Node(4)
    start.next.next.next.next = Node(5)
    
    # 1's random points to 3
    start.random = start.next.next 
    
    # 2's random points to 1
    start.next.random = start 
    
    # 3's and 4's random points to 5
    start.next.next.random = start.next.next.next.next 
    start.next.next.next.random = start.next.next.next.next 
    
    # 5's random points to 2
    start.next.next.next.next.random = start.next 
    
    # Print the original and cloned linked list
    print "\r:::Original linked list"
    printList(start)

    print "\r\r:::Cloned linked list without extra space"
    newCloneList = cloneWithoutExtraSpace(start)
    
    printList(newCloneList)
    

'''
:::Original linked list
Data = 1, Random data = 3
Data = 2, Random data = 4
Data = 3, Random data = 5
Data = 4, Random data = -1
Data = 5, Random data = 2


:::Cloned linked list using hash (with extra space)
Data = 1, Random data = 3
Data = 2, Random data = 4
Data = 3, Random data = 5
Data = 4, Random data = -1
Data = 5, Random data = 2

:::Original linked list
Data = 1, Random = 3
Data = 2, Random = 1
Data = 3, Random = 5
Data = 4, Random = 5
Data = 5, Random = 2


:::Cloned linked list without extra space
Data = 1, Random = 3
Data = 2, Random = 1
Data = 3, Random = 5
Data = 4, Random = 5
Data = 5, Random = 2
'''
if __name__ == "__main__":
    main()
