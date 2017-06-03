1. Common hash table
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

'''
[None, None, None, None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None, None, None, 54]
[None, None, None, None, None, None, None, None, None, None, 'cat']
[None, None, None, None, 26, None, None, None, None, None, 54]
[None, None, None, None, 'dog', None, None, None, None, None, 'cat']
[None, None, None, None, 26, 93, None, None, None, None, 54]
[None, None, None, None, 'dog', 'lion', None, None, None, None, 'cat']
[None, None, None, None, 26, 93, 17, None, None, None, 54]
[None, None, None, None, 'dog', 'lion', 'tiger', None, None, None, 'cat']
[77, None, None, None, 26, 93, 17, None, None, None, 54]
['bird', None, None, None, 'dog', 'lion', 'tiger', None, None, None, 'cat']
[77, None, None, None, 26, 93, 17, None, None, 31, 54]
['bird', None, None, None, 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
[77, 44, None, None, 26, 93, 17, None, None, 31, 54]
['bird', 'goat', None, None, 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
[77, 44, 55, None, 26, 93, 17, None, None, 31, 54]
['bird', 'goat', 'pig', None, 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
[77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
[77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
['bird', 'goat', 'pig', 'duck', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
[77, 44, 55, 20, 26, 93, 17, 66, None, 31, 54]
['bird', 'goat', 'pig', 'duck', 'dog', 'lion', 'tiger', 'cat1', None, 'cow', 'cat']
[77, 44, 55, 20, 26, 93, 17, 66, 88, 31, 54]
['bird', 'goat', 'pig', 'duck', 'dog', 'lion', 'tiger', 'cat1', 'cat2', 'cow', 'cat']
'''
if __name__ == "__main__":
    H=HashTable(11)
    print(H.slots)    
    print(H.data)
    H[54]="cat"
    print(H.slots)    
    print(H.data)
    H[26]="dog"
    print(H.slots)    
    print(H.data)
    H[93]="lion"
    print(H.slots)    
    print(H.data)
    H[17]="tiger"
    print(H.slots)    
    print(H.data)
    H[77]="bird"
    print(H.slots)    
    print(H.data)
    H[31]="cow"
    print(H.slots)    
    print(H.data)
    H[44]="goat"
    print(H.slots)    
    print(H.data)
    H[55]="pig"
    print(H.slots)    
    print(H.data)
    H[20]="chicken"
    print(H.slots)    
    print(H.data)
    H[20]='duck'
    print(H.slots)    
    print(H.data)
    H[66]='cat1'
    print(H.slots)    
    print(H.data)
    H[88]='cat2'
    print(H.slots)    
    print(H.data)    
    H[99]='cat3'
    print(H.slots)    
    print(H.data)    
    print H[99]

2. Chain hash table
class LinkedList:

    def push(self, new, prev = None):
        if prev == None:
            new.next = self.head
            self.head = new
        else:
            new.next = prev.next
            prev.next = new

    def pop(self, index = 0):
        cur = index
        prev_node = None
        cur_node = self.head
        while cur > 0:
            prev_node = cur_node
            cur_node = cur_node.next
            cur -= 1
            
        if prev_node == None:
            popped = self.head
            self.head = self.head.next
            return popped
        else:
            prev_node = cur_node.next
            return cur_node

    def insert(self, node, index = 0):
        if node == None:
            raise Exception("node is None Type")
            return
        cur = index
        prev_node = None
        cur_node = self.head
        while cur > 0:
            prev_node = cur_node
            cur_node = cur_node.next
            cur -= 1

        if prev_node == None:
            self.head = node
        else:
            prev_node.next = node

        node.next = cur_node

    def __str__(self):
        if self.head == None:
            return ""
        else:
            return str(self.head)

    def __init__(self, head = None):
        self.head = head


class Link:
    """ Link

        Used in the ChainedHashtable, a Link is a key, value pair for use in a linked list.
    """

    def __str__(self):
        if self.next == None:
            return str(self.value) + " "
        else:
            return str(self.value) + " " + str(self.next)

    def __init__(self, key = 0, value = 0, next = None):
        self.key = key
        self.value = value
        self.next = next

def DivisionHash(key, size):
    return key % size

class HashTable:

    size = 23

    # Init
    def __init__(self):
        self.links = [None] * HashTable.size

    def __str__(self):
        lines = []
        for i in range(len(self.links)):
            if self.links[i] is None:
                lines.append("" + str(i) + "\t")
            else:
                lines.append("" + str(i) + "\t" + str(self.links[i]))

        return "\n".join(lines)

    def put(self, key, value):
        llist = self.links[self.hash(key)]
        if llist is None:
            node = Link(key=key, value=value)
            llist = LinkedList(head=node)
            self.links[self.hash(key)] = llist
            return
        cur_node = llist.head
        while cur_node is not None:
            if cur_node.key == key:
                cur_node.value = value
                return
            else:
                cur_node = cur_node.next
        llist.push(Link(key=key, value=value))

    def get(self, key):
        llist = self.links[self.hash(key)]
        if llist is None:
            return None

        cur_node = llist.head
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node.value
            else:
                cur_node = cur_node.next
        return None

    def search1(self, key):
        llist = self.links[self.hash(key)]
        if llist is None:
            return str(self.hash(key)) 
        search_result = ""
        cur_node = llist.head
        search_result += str(self.hash(key)) + " "
        while cur_node is not None:
            search_result += str(cur_node.value) + " "
            if cur_node.key == key:
                return search_result
            else:
                cur_node = cur_node.next
        return search_result
    
    def search(self, key):
        llist = self.links[self.hash(key)]
        if llist == None:
            return str(self.hash(key))
        search_result = ""
        cur_node = llist.head
        search_result += str(self.hash(key)) + " " 
        while cur_node != None:
            search_result += str(cur_node.value) + " "
            if cur_node.key == key:
                return search_result
            else:
                cur_node = cur_node.next
        return search_result


    def insert(self,value):
        self.put(value, value)

    def hash(self, key):
        return DivisionHash(key, HashTable.size)

'''
0	
1	1 
2	
3	
4	
5	
6	
7	
8	100 
9	
10	
11	
12	12 81 35 
13	
14	
15	
16	
17	
18	
19	
20	
21	21 
22	
12
12 12 81 35 

'''
if __name__ == "__main__":
    theValues = [100, 1, 21, 35, 81, 12]
    htable = HashTable()
    for value in theValues:
        htable.insert(value)

    print htable
    print htable.get(12)
    print htable.search(35)

3. Liear hash table
import math 

class Entry:
    """ Entry

        Used in every hashtable but the ChainedHashtable, an Entry is a key, value pair
    """

    def __str__(self):
        return str(self.value)

    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        
def AuxiliaryHash(key, size):
    A = 0.618
    return int(math.floor(size * ((key * A) % 1)))

def LinearHash(key, i, size):
    return (AuxiliaryHash(key, size) + i) % size

class LinearHashtable:
    """
    Linear Hashtable
    Keys and values are stored in an associative array, and probed for values
    by searching linearly through the table
    """
    size = 32

    def __init__(self):
        self.entries = [None] * LinearHashtable.size

    def get(self, key):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while entry is None or entry.key != key:
            i += 1
            if i == LinearHashtable.size:
                return None
            entry = self.entries[self.hash(key, i)]
        return entry.value

    def search(self, key):
        i = 0
        search_result = ""
        entry = self.entries[self.hash(key, i)]
        search_result = str(self.hash(key, i)) + " "
        while entry is None or entry.key != key:
            i += 1
            if i == LinearHashtable.size:
                return search_result + "-1"
            entry = self.entries[self.hash(key, i)]
            search_result += str(self.hash(key, i)) + " "
        return search_result

    def put(self, key, value):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while entry is not None and entry.key != key:
            i += 1
            if i == LinearHashtable.size:
                return
            entry = self.entries[self.hash(key, i)]
        if entry is None:
            entry = Entry(key=key, value=value)
            self.entries[self.hash(key, i)] = entry
        else:
            entry.value = value

    def insert(self, value):
        self.put(value, value)

    def hash(self, key, i):
        return LinearHash(key, i, LinearHashtable.size)

    def __str__(self):
        lines = []
        for i in range(len(self.entries)):
            if self.entries[i] is None:
                lines.append("" + str(i) + "\t" + "-1")
            else:
                lines.append("" + str(i) + "\t" + str(self.entries[i].value))
        return "\n".join(lines)

'''
0    -1
1    81
2    -1
3    -1
4    -1
5    -1
6    -1
7    -1
8    -1
9    -1
10    -1
11    -1
12    -1
13    12
14    -1
15    -1
16    -1
17    -1
18    -1
19    1
20    35
21    -1
22    -1
23    -1
24    -1
25    100
26    -1
27    -1
28    -1
29    -1
30    -1
31    21
12
20 
'''
if __name__ == "__main__":
    theValues = [100, 1, 21, 35, 81, 12]
    htable = LinearHashtable()
    for value in theValues:
        htable.insert(value)

    print htable
    print htable.get(12)
    print htable.search(35)

4. Quadratic Hashtable
import math 

class Entry:
    """ Entry

        Used in every hashtable but the ChainedHashtable, an Entry is a key, value pair
    """

    def __str__(self):
        return str(self.value)

    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        
def AuxiliaryHash(key, size):
    A = 0.618
    return int(math.floor(size * ((key * A) % 1)))

def QuadraticHash(key, i, size):
    c_1 = 0.5
    c_2 = 0.5
    return int((AuxiliaryHash(key, size) + c_1 * i + c_2 * i * i) % size)

class QuadraticHashtable:

    size = 32

    def __init__(self):
        self.entries = [None] * QuadraticHashtable.size

    def get(self,  key):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while entry is None or entry.key != key:
            i += 1
            if i == QuadraticHashtable.size:
                return None

            entry = self.entries[self.hash(key, i)]
        return entry.value

    def put(self, key, value):
        i = 0
        entry = self.entries[self.hash(key, i)]
        while entry is not None and entry.key != key:
            i += 1
            if i == QuadraticHashtable.size:
                return
            entry = self.entries[self.hash(key, i)]
        if entry is None:
            entry = Entry(key = key, value = value)
            self.entries[self.hash(key, i)] = entry
        else:
            entry.value = value

    def search(self, key):
        i = 0
        search_result = ''
        entry = self.entries[self.hash(key, i)]
        search_result = str(self.hash(key, i)) + " "
        while entry is None or entry.key != key:
            i += 1
            if i == QuadraticHashtable.size:
                return search_result + "-1"
            entry = self.entries[self.hash(key, i)]
            search_result += str(self.hash(key, i)) + " "
        return search_result

    def hash(self, key, i):
        return QuadraticHash(key, i, QuadraticHashtable.size)

    def insert(self, value):
        self.put(value, value)

    def __str__(self):
        lines = []
        for i in range(len(self.entries)):
            if self.entries[i] is None:
                lines.append("" + str(i) + "\t" + "-1")
            else:
                lines.append("" + str(i) + "\t" + str(self.entries[i].value))
        return "\n".join(lines)

'''
0    -1
1    81
2    -1
3    -1
4    -1
5    -1
6    -1
7    -1
8    -1
9    -1
10    -1
11    -1
12    -1
13    -1
14    -1
15    -1
16    -1
17    -1
18    -1
19    1
20    35
21    -1
22    -1
23    -1
24    -1
25    100
26    -1
27    -1
28    -1
29    -1
30    -1
31    21
None
20 

'''
if __name__ == "__main__":
    
    theValues = [100, 1, 21, 35, 81]
    htable = QuadraticHashtable()
    for value in theValues:
        htable.insert(value)

    print htable
    print htable.get(12)
    print htable.search(35)

5. Double hash table
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

'''
0    -1
1    1
2    -1
3    -1
4    35
5    -1
6    -1
7    100
8    -1
9    -1
10    -1
11    -1
12    -1
13    -1
14    -1
15    -1
16    -1
17    -1
18    -1
19    81
20    -1
21    21
22    -1
23    -1
24    -1
25    -1
26    -1
27    -1
28    -1
29    -1
30    -1
None
4 
'''
if __name__ == "__main__":
    
    theValues = [100, 1, 21, 35, 81]
    htable = DoubleHashtable()
    for value in theValues:
        htable.insert(value)

    print htable
    print htable.get(12)
    print htable.search(35)
