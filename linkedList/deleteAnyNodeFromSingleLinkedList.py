'''
Given a pointer to a node (not the tail node( in a singly linked list)
Delete that node from the linked list
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Given a reference (pointer to pointer) to the head
# of a list and an int, push a new node on the front of the list
def push(head_ref, new_data):

    # put the in the data
    new_node = Node(new_data)

    # link the old list off the new node
    new_node.next = head_ref

    # move the head to point to the new node
    head_ref = new_node
    
    return head_ref

# Print the list
def printList(head):

    temp = head
    while temp is not None:
        print "%s " % temp.data
        temp = temp.next

# Delete node
def deleteNode(node_ptr):

    temp = node_ptr.next
    node_ptr.data = temp.data
    node_ptr.next = temp.next
    temp = None

# Driver program to test above function
def main():

    # Start with the empty list
    head = None

    # Use push to construct below list
    head = push(head, 1)
    head = push(head, 4)
    head = push(head, 1)
    head = push(head, 12)
    head = push(head, 1)

    print "\rBefore deleting \n"
    printList(head)

    print "\rAfter deleteing \n"
    deleteNode(head.next.next)
    printList(head)

'''

Before deleting 

1 
12 
1 
4 
1 

After deleteing 

1 
12 
4 
1 
'''
if __name__ == "__main__":
    main()
