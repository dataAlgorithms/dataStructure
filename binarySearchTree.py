#! coding=utf-8

import copy
import unittest

class BST(object):
    """Tree node: left and right child + data which can be any object

    """
    def __init__(self, data):
        """Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """Insert new node with data

        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """Lookup node containing data

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

    def delete(self, data):
        """Delete node containing data

        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, just remove it
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.data = None
            elif children_count == 1:
                # if node has 1 child
                # replace node by its child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                else:
                    self.left = n.left
                    self.right = n.right
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
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def compare_trees(self, node):
        """Compare 2 trees

        @param node tree to compare
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
            res = self.right.compare_trees(node.right)
        return res

    def print_tree(self):
        """Print tree content inorder

        """
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def tree_data(self):
        """Generator to get the tree nodes data

        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.data
                node = node.right

    def children_count(self):
        """Return the number of children

        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.root_single_node = BST(None)
        self.root = BST(10)
        self.root.left = BST(5)
        self.root.left.left = BST(3)
        self.root.left.right = BST(7)
        self.root.right = BST(15)
        self.root.right.left = BST(12)
        self.root.right.left.left = BST(11)
        self.root.right.right = BST(20)
        self.root_copy = copy.deepcopy(self.root)

    def test_insert(self):
        root = self.root_single_node

        root.insert(10)
        self.assertEqual(root.data, 10)

        root.insert(5)
        self.assertEqual(root.left.data, 5)

        root.insert(15)
        self.assertEqual(root.right.data, 15)

        root.insert(8)
        self.assertEqual(root.left.right.data, 8)

        root.insert(2)
        self.assertEqual(root.left.left.data, 2)

        root.insert(12)
        self.assertEqual(root.right.left.data, 12)

        root.insert(17)
        self.assertEqual(root.right.right.data, 17)

    def test_lookup(self):
        node, parent = self.root.lookup(0)
        self.assertIsNone(parent)
        self.assertIsNone(node)

        node, parent = self.root.lookup(13)
        self.assertIsNone(parent)
        self.assertIsNone(node)

        node, parent = self.root.lookup(7)
        self.assertIs(node, self.root.left.right)
        self.assertIs(parent, self.root.left)

    def test_delete_root_no_child(self):
        self.root_single_node.data = 7
        self.root_single_node.delete(7)
        self.assertIsNone(self.root_single_node.data)

    def test_delete_root_one_child(self):
        self.root_single_node.data = 7
        self.root_single_node.insert(3)
        self.root_single_node.delete(7)
        self.assertEqual(self.root_single_node.data, 3)

    def test_delete_one_child_left(self):
        self.root.delete(12)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 11)
        self.assertEqual(self.root.right.right.data, 20)

    def test_delete_one_child_right(self):
        self.root.insert(25)
        self.root.delete(20)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)
        self.assertEqual(self.root.right.right.data, 25)

    def test_delete_right_leaf(self):
        self.root.delete(7)
        self.assertIsNone(self.root.left.right)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)
        self.assertEqual(self.root.right.right.data, 20)

    def test_delete_left_leaf(self):
        self.root.delete(3)
        self.assertIsNone(self.root.left.left)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)
        self.assertEqual(self.root.right.right.data, 20)

    def test_delete_right_node_two_childs(self):
        self.root.delete(15)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.right.data, 20)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)

    def test_delete_left_node_two_childs(self):
        self.root.delete(5)
        self.assertEqual(self.root.left.data, 7)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)
        self.assertEqual(self.root.right.right.data, 20)

    def test_delete_root_two_childs(self):
        self.root.delete(10)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.data, 11)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.right.data, 20)

    def test_compare_trees_left_leaf_missing(self):
        self.root_copy.delete(11)
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_compare_trees_right_leaf_missing(self):
        self.root_copy.delete(20)
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_compare_trees_diff_value(self):
        self.root_copy.left.data = 16
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_compare_trees_extra_right_leaf(self):
        self.root_copy.insert(25)
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_compare_trees_extra_left_leaf(self):
        self.root_copy.insert(18)
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_print_tree(self):
        self.root.print_tree()

    def test_tree_data(self):
        self.assertEqual([e for e in self.root.tree_data()],
                         [3, 5, 7, 10, 11, 12, 15, 20])

'''
..................
----------------------------------------------------------------------
Ran 18 tests in 0.003s

OK
3
5
7
10
11
12
15
20
'''
if __name__ == '__main__':
    unittest.main()
