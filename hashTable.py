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
