# coding=utf-8

# A node of the singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Segregate even odd in a linked list
'''
Method One:

Algorithm:
  1) Get pointer to the last node.
  2) Move all the odd nodes to the end.
  ..a) Consider all odd nodes before the first even node and move them to end.
  ..b) Change the head pointer to point to the first even node.
  ..b) Consider all odd nodes after the first even node and move them to the end.
'''
def segregateEvenOdd(head_ref):

    end = head_ref
    prev = None
    curr = head_ref

    # Get pointer to the last node
    while end.next is not None:
        end = end.next

    new_end = end

    # Consider all odd nodes before the first even node
    # and move them after end
    while curr.data % 2 != 0 and curr is not end:
        new_end.next = curr
        curr = curr.next
        new_end.next.next = None
        new_end = new_end.next

    # Do following steps only if there is any even node
    if curr.data % 2 == 0:
        # Change the head pointer to point to first even node
        head_ref = curr

        # now current points to the first even node
        while curr is not end:
            if curr.data %2 == 0:
                prev = curr
                curr = curr.next
            else:
                # break the link between prev and current
                prev.next = curr.next

                # make next of curr as NULL
                curr.next = None

                # Move curr to end
                new_end.next = curr

                # make curr as new end of list
                new_end = curr

                # Update current pointer to next of the move node
                curr = prev.next
        # We must have prev set before executing lines following this statement
    else:
        prev = curr

    # If there are more than 1 odd nodes and end of original list is 
    # odd then move this node to end to maintain same order of odd
    # numbers in modified list
    if new_end != end and end.data %2 != 0:
        prev.next = end.next
        end.next = None
        new_end.next = end

    return head_ref

# Push to insert a node at the beginning
def push(head_ref, new_data):

    # allocate node
    new_node = Node(new_data)

    # link the old list off the new node
    new_node.next = head_ref

    # move the head to point to the new node
    head_ref = new_node

    return head_ref

# Print nodes
def printList(head):

    while head is not None:
        print "%d " % head.data,
        head = head.next

# Data build
def buildData(aList=None):
    
    '''
    aList = [17,15,8,12,10,5,4,1,7,6]
    aList = [8,12,10,5,4,1,6]
    aList = [8,12,10]
    aList = [1,3,5,7]
    '''
    
    head = None
    for i in range(len(aList)-1, -1, -1):
        head = push(head, aList[i])
        
    return head
   
'''
Method Two:

Split the linked list into two, 
    one containing all even nodes and other containing all odd nodes
    And finally attach the odd node linked list after the even node linked list

To split the linked list, traverse the original linked list and move all odd nodes to a separate linked list of all odd nodes
at the end of loop, the original list will have all the even nodes and the odd node list will have all the odd nodes
To keep keep the ordering of all nodes same, we must insert all the odd nodes at the end of the odd node list

And to do that in constant time, we must keep track of last pointer in the odd node list
'''

class LinkedList:
    def __init__(self):
        self.head = None

    def segregateEvenOdd(self):
        evenStart = None
        evenEnd = None
        oddStart = None
        oddEnd = None
        currentNode = self.head

        while currentNode is not None:
            element = currentNode.data

            if element % 2 == 0:
                if evenStart is None:
                    evenStart = currentNode
                    evenEnd = evenStart
                else:
                    evenEnd.next = currentNode
                    evenEnd = evenEnd.next
            else:
                if oddStart is None:
                    oddStart = currentNode
                    oddEnd = oddStart
                else:
                    oddEnd.next = currentNode
                    oddEnd = oddEnd.next

            # Move head pointer one step in forward direction
            currentNode = currentNode.next

        if oddStart is None or evenStart is None:
            return 

        evenEnd.next = oddStart
        oddEnd.next = None
        self.head = evenStart

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # print the linked list
    def printList(self):
        temp = self.head
        while temp is not None:
            print "%d " % temp.data,
            temp = temp.next

        print ""

def test_main(aList=None):

    llist = LinkedList()
    for i in range(len(aList)-1, -1, -1):
        llist.push(aList[i]);

    print "\r\n\nOriginal linked list:"
    llist.printList()

    print "\r\nModified linked list:"
    llist.segregateEvenOdd()
    llist.printList()    
     
# Driver program
def main():

    print "\nOriginal Linked list "
    head = buildData(aList = [17,15,8,12,10,5,4,1,7,6])
    printList(head);

    print "\n\nModified Linked list "
    head = segregateEvenOdd(head);
    printList(head);
    
    print "\n\nOriginal Linked list "
    head = buildData(aList = [8,12,10,5,4,1,6])
    printList(head);

    print "\n\nModified Linked list "
    head = segregateEvenOdd(head);
    printList(head);
    
    print "\n\nOriginal Linked list "
    head = buildData(aList = [8,12,10])
    printList(head);

    print "\n\nModified Linked list "
    head = segregateEvenOdd(head);
    printList(head);
  
    print "\n\nOriginal Linked list "
    head = buildData(aList = [1,3,5,7])
    printList(head);

    print "\n\nModified Linked list "
    head = segregateEvenOdd(head);
    printList(head);
      
'''

Original Linked list 
17  15  8  12  10  5  4  1  7  6  

Modified Linked list 
8  12  10  4  6  17  15  5  1  7  

Original Linked list 
8  12  10  5  4  1  6  

Modified Linked list 
8  12  10  4  6  5  1  

Original Linked list 
8  12  10  

Modified Linked list 
8  12  10  

Original Linked list 
1  3  5  7  

Modified Linked list 
1  3  5  7  

Original linked list:
17  15  8  12  10  5  4  1  7  6  

Modified linked list:
8  12  10  4  6  17  15  5  1  7  


Original linked list:
8  12  10  5  4  1  6  

Modified linked list:
8  12  10  4  6  5  1  


Original linked list:
8  12  10  

Modified linked list:
8  12  10  


Original linked list:
1  3  5  7  

Modified linked list:
1  3  5  7  
'''
if __name__ == "__main__":
    main()
    test_main(aList = [17,15,8,12,10,5,4,1,7,6])
    test_main(aList = [8,12,10,5,4,1,6])
    test_main(aList = [8,12,10])
    test_main(aList = [1,3,5,7])
