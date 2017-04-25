#! coding=utf-8

'''
Method one: with three step
'''
'''
1. If left subtree exists, process the left subtree
..1.a) Recursively convert the left subtree to DLL.
..1.b) Then find inorder predecessor of root in left subtree (inorder predecessor is rightmost node in left subtree).
..1.c) Make inorder predecessor as previous of root and root as next of inorder predecessor.
2. If right subtree exists, process the right subtree (Below 3 steps are similar to left subtree).
..2.a) Recursively convert the right subtree to DLL.
..2.b) Then find inorder successor of root in right subtree (inorder successor is leftmost node in right subtree).
..2.c) Make inorder successor as next of root and root as previous of inorder successor.
'''
def bst2DllUtil(root):

    # base case
    if root is None:
        return root

    # convert the left subtree and link to root
    if root.left is not None:
        # convert the  left subtree
        left = bst2DllUtil(root.left)

        # find inorder predecessor, after this loop, left
        # will point to the inorder predecessor
        while left.right is not None:
            left = left.right

        # Make root as next of the predecessor
        left.right = root

        # Make predecessor as previous of root
        root.left = left

    # Convert the right subtree and link to root
    if root.right is not None:
        # Convert the right subtree
        right = bst2DllUtil(root.right)

        # Find inorder successor, after this loop, right
        # will point to the inorder successor
        while right.left is not None:
            right = right.left

        # Make root as previous of successor
        right.left = root

        # Make sucessor as next of root
        root.right = right

    return root

'''
3. Find the leftmost node and return it (the leftmost node is always head of converted DLL).
'''
def bst2Dll(root):

    # Base case
    if root is None:
        return root

    # Convert to DLL
    root = bst2DllUtil(root)

    # bst2DllUtil return root node of the converted
    # DLL, we need pointer to the leftmost node which is
    # head of the constructed DLL, so move to the leftmost node
    while root.left is not None:
        root = root.left

    return root

# Print the list
def printList(head):
    
    while head is not None:
        print head.data, 
        head = head.right

'''
Method two: with two steps
'''
# Change left pointers to work as previous pointers
# in converted DLL
# The function simply does inorder traversal of 
# Binary tree and updates
# left pointer using previously visited node
def static_vars(**kwargs):
    '''http://stackoverflow.com/questions/279561/what-is-the-Python-equivalent-of-static-variables-inside-a-function'''
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(prev=None)
def fixPrevPtr(root):
    if root is not None: 
        fixPrevPtr(root.left)
        root.left = fixPrevPtr.prev
        fixPrevPtr.prev = root
        fixPrevPtr(root.right)

# Change right pointers to work as next pointer in
# converted DLL
def fixNextPtr(root):

    prev = None
    # Find the right most node in BT or last node in DLL
    while root is not None and root.right is not None:
        root = root.right

    # Start from the rightmost node, traverse back using left pointers
    # While traversing, change right pointer of nodes
    while root is not None and root.left is not None:
        prev = root
        root = root.left
        root.right = prev

    # The leftmost node is head of linked list, return it
    return root

# The main function that converts BST to DLL and returns head of DLL
def bst2DLL2(root):

    # Set the previous pointer
    fixPrevPtr(root)

    # Set the next pointer and return head of dll
    return fixNextPtr(root)    
                
'''
Method 3: using recursive way
'''
@static_vars(prev=None)
def bst2DLL3(root):

    global newhead
    
    # Base case
    if root is None:
        return

    # Recursively convert left subtree
    bst2DLL3(root.left)

    # Now convet this node
    if bst2DLL3.prev is None:
        newhead = root
    else:
        root.left = bst2DLL3.prev
        bst2DLL3.prev.right = root

    bst2DLL3.prev = root

    # Finally convert right subtree
    bst2DLL3(root.right)
        
class Node:
    """
    Tree node: left and right child + data which can be any obejct
    """
    def __init__(self, data):
        """
        Node constructor
        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data
        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """
        Lookup node containing data
        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        """
        Returns the number of children
        @returns number of of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        """
        Delete node containing data
        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        children_counts = 0
        if node is not None:
            children_counts = node.children_count()

        if children_counts == 0:
            # if node has no children, just remove it
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.data = None

        elif children_counts == 1:
            # if node has 1 child
            # replace node with its child
            if node.left:
                n = node.left
            else:
                n = node.right

            if  parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                self.left = n.left
                self.rigth = n.right
                self.data = n.data

        else:
            # if node has 2 children
            # find its successor
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            # replace node data by its successor data
            node.data = successor.data
            # fix successor's parent's child
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def print_tree(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print self.data,
        if self.right:
            self.right.print_tree()

    def compare_trees(self, node):
        """
        Compare 2 trees
        @param node tree's root node to compare to
        @returns True if the tree passed is identical to this tree
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.rigth.compare_trees(node.right)
        return res

    def tree_data(self):
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.right
                
def main():
    print ':::Using method one'
    root = Node(10)
    root.insert(12)
    root.insert(15)
    root.insert(25)
    root.insert(30)
    root.insert(36)
    
    print ':::Primary binary search tree'
    root.print_tree()
    
    print '\r\r::Binary search tree to double linked list'
    head = bst2Dll(root)
    printList(head)
    
    print '\r\r:::Using method two'
    root1 = Node(10)
    root1.insert(12)
    root1.insert(15)
    root1.insert(25)
    root1.insert(30)
    root1.insert(36)
    
    print ':::Primary binary search tree'
    root1.print_tree()
    
    print '\r\r::Binary search tree to double linked list'
    head = bst2DLL2(root1)
    printList(head)
    
    print '\r\r:::Using method three'
    root2 = Node(10)
    root2.insert(12)
    root2.insert(15)
    root2.insert(25)
    root2.insert(30)
    root2.insert(36)
    
    print ':::Primary binary search tree'
    root2.print_tree()
    
    print '\r\r::Binary search tree to double linked list'
    global newhead 
    bst2DLL3(root2)
    printList(newhead)
        
'''
:::Using method one
:::Primary binary search tree
10 12 15 25 30 36 

::Binary search tree to double linked list
10 12 15 25 30 36 

:::Using method two
:::Primary binary search tree
10 12 15 25 30 36 

::Binary search tree to double linked list
10 12 15 25 30 36 

:::Using method three
:::Primary binary search tree
10 12 15 25 30 36 

::Binary search tree to double linked list
10 12 15 25 30 36
'''
if __name__ == "__main__":
    main(),
