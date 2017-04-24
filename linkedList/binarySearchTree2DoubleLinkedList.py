#! coding=utf-8

'''
1. If left subtree exists, process the left subtree
��..1.a) Recursively convert the left subtree to DLL.
��..1.b) Then find inorder predecessor of root in left subtree (inorder predecessor is rightmost node in left subtree).
��..1.c) Make inorder predecessor as previous of root and root as next of inorder predecessor.
2. If right subtree exists, process the right subtree (Below 3 steps are similar to left subtree).
��..2.a) Recursively convert the right subtree to DLL.
��..2.b) Then find inorder successor of root in right subtree (inorder successor is leftmost node in right subtree).
��..2.c) Make inorder successor as next of root and root as previous of inorder successor.
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
                
'''
:::Primary binary search tree
10 12 15 25 30 36 

::Binary search tree to double linked list
10 12 15 25 30 36
'''
def main():
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
        
if __name__ == "__main__":
    main()
