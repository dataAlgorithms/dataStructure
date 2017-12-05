# Single Linked list node
class SingleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Single Linked list class
class SingleLinkedList:

    # Assign head to None    
    def __init__(self):
        self.head = None

    # Get the length
    def __len__(self):
        return self.getListLength()

    # Get the length of single linked list
    def getListLength(self):
        current = self.head
        count = 0

        # Loop until the end of single linked list reaches
        while current is not None:
            count += 1
            current = current.next

        # Return the length
        return count

    # Insert node into single linked list
    def insertNodeIntoList(self, data, position):
        assert position >= -1 and position < len(self), \
                      "position is out of index of single linked list"

        newNode = SingleLinkedListNode(data)
       
        # insert at the beginning
        if position == 0:
            newNode.next = self.head
            self.head = newNode
            
        elif position == -1 or position == len(self):

            preNode = self.head
            curNode = self.head

            while curNode is not None:
                preNode = curNode
                curNode = curNode.next

            preNode.next = newNode

        else:
            preNode = self.head
            curNode = self.head
            i = 0

            while curNode is not None and i < position:
                preNode = curNode
                curNode = curNode.next
                i += 1

            newNode.next = curNode
            preNode.next = newNode


    # Delete node from single linked list
    def deleteNodeFromList(self, position):
        assert position >= -1 and position < len(self), \
                      "position is out of index of single linked list"

       
        # delete at the beginning
        if position == 0:

            self.head = self.head.next
            
        elif position == -1 or position == len(self):

            if len(self) == 1:
                self.head = None
            else:
                preNode = self.head
                curNode = self.head.next
                
                while curNode != None:
                    preNode = curNode
                    curNode = curNode.next

                preNode.next = None

        else:
            preNode = self.head
            curNode = self.head
            i = 0

            while curNode is not None and i < position:
                preNode = curNode
                curNode = curNode.next
                i += 1
            
            preNode.next = curNode.next

    # Delete the single linked list
    def deleteList(self):
        for i in range(len(self)):
            self.deleteNodeFromList(i)       
