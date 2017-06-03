#! coding=utf-8 

'''
Count of distinct substrings of a string using Suffix Trie
Given a string of length n of lowercase alphabet characters, 
we need to count total number of distinct substrings of this string.

Examples:

Input  : str = “ababa”
Output : 10
Total number of distinct substring are 10, which are,
"", "a", "b", "ab", "ba", "aba", "bab", "abab", "baba"
and "ababa"
'''

MAX_CHAR = 26

# A Suffix Trie (A Trie of all suffixes) Node
class SuffixTrieNode:
    # init
    def __init__(self):
        self.children = [None] * MAX_CHAR

    # a recursive function to insert a suffix of the s
    # in subtree rooted with this node
    def insertSuffix(self, s):
        # get the length of s
        n = len(s)

        # If string has more characters
        if n > 0:
            # Find the first character and convert it
            # into 0~25 range
            cIndex = ord(s[0]) - ord('a')

            # If there is no edge for this character
            # add a new edge
            if self.children[cIndex] is None:
                self.children[cIndex] = SuffixTrieNode()

            # Recur for next suffix
            self.children[cIndex].insertSuffix(s[1:])

# A Trie of all Suffixes
class SuffixTrie:
    # init
    def __init__(self, s):
        self.root = SuffixTrieNode()

        # Consider all Suffixes of given string and insert
        # them into the Suffix Trie using recursive function
        # insertSuffix in SuffixTrieNode class
        for i in range(len(s)):
            self.root.insertSuffix(s[i:])

    # method to count total nodes in suffix trie
    def countNodesInTrie(self):
        return self._countNodesInTrie(self.root)

    # A recursive function to count nodes in trie
    def _countNodesInTrie(self, node):
        # If all characters of pattern have been processed
        if node is None:
            return 0

        count = 0
        for i in range(MAX_CHAR):
            # If children is not NULL then find count
            # of all nodes in this subtrie
            if node.children[i] is not None:
                count += self._countNodesInTrie(node.children[i])

        # return count of nodes of subtrie and plus 
        # 1 because of node's own count
        return 1 + count

# Return count of distinct substrings of str
def countDistinctSubstring(aStr):

    # Construct a Trie of all Suffixes
    sTrie = SuffixTrie(aStr)

    # Return count of nodes in Trie of Suffixes
    return sTrie.countNodesInTrie()

'''
10
2
4
352
1
'''
if __name__ == "__main__":
    for aStr in ['ababa', 'a', 'ab', 'abcdefghijklmnopqrstuvwxyz', '']:
        print countDistinctSubstring(aStr)
