# arrayMatrix

import ctypes

class Array:
    # Init
    def __init__(self, size):
        assert size > 0, "size should be above than 0"

        PyObjects = ctypes.py_object * size
        self.slots = PyObjects()
        self.size = size
        self.clear(None)

    # Len
    def __len__(self):
        return self.size

    # Get item
    def __getitem__(self, index):
        assert index >= 0 and index < self.size, "index must be within the valid range."

        return self.slots[index]

    # Set item
    def __setitem__(self, index, value):
        assert index >= 0 and index < self.size, "index must be within the valid range."

        self.slots[index] = value

    # Clear
    def clear(self, value):
        for i in range(self.size):
            self.slots[i] = value

    # Iterator
    def __iter__(self):
        return ArrayIterator(self.slots)

class ArrayIterator:
    # Init
    def __init__(self, slots):
        self.slots = slots
        self.index = 0
    # Iter
    def __iter__(self):
        return self
    # Next
    def next(self):
        if self.index < len(self.slots):
            item = self.slots[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

class Array2D:
    # init
    def __init__(self, nrows, ncols):
        self._theRows = Array(nrows)

        for i in range(len(self._theRows)):
            self._theRows[i] = Array(ncols)

    # the number of rows
    def numRows(self):
        return len(self._theRows)

    # the number of cols
    def numCols(self):
        return len(self._theRows[0])

    # clear the array
    def clear(self, value):
        for i in range(self.numRows()):
            self._theRows[i].clear(value)

    # get the item
    def __getitem__(self, nTuple):
        assert len(nTuple) == 2, "The size of tuple should be 2."
        row = nTuple[0]
        col = nTuple[1]

        assert row >= 0 and row < self.numRows() and \
             col >= 0 and col < self.numCols(), "out of subscript"

        the1dArray = self._theRows[row]
        return the1dArray[col]

    # set the itme
    def __setitem__(self, nTuple, value):
        assert len(nTuple) == 2, "The size of tuple should be 2."
        row = nTuple[0]
        col = nTuple[1]

        assert row >= 0 and row < self.numRows() and \
             col >= 0 and col < self.numCols(), "out of subscript"

        the1dArray = self._theRows[row]
        the1dArray[col] = value

# Implement a matrix
class MyMatrix:

    # init
    def __init__(self, nrows, ncols):
        self._theGrid = Array2D(nrows, ncols)
        self._theGrid.clear(0)

    # return the number of rows in the matrix

    def numRows(self):
        return self._theGrid.numRows()

    # return the number of columns in the matrix
    def numCols(self):
        return self._theGrid.numCols()

    # return the value stored in the given matrix element
    def __getitem__(self, ndxTuple):

        return self._theGrid[ndxTuple[0],ndxTuple[1]]

    # set the matrix element 
    def __setitem__(self, ndxTuple, scalar):

        self._theGrid[ndxTuple[0],ndxTuple[1]] = scalar

    # scalar value
    def scaleBy(self, scalar):

        for row in range(self._theGrid.numRows()):
            for col in range(self._theGrid.numCols()):
                self._theGrid[row,col] *= scalar

    # transpose
    def transpose(self):
        
        theNewGrid = MyMatrix(self._theGrid.numCols(), self._theGrid.numRows())

        for row in range(self._theGrid.numRows()):
            for col in range(self._theGrid.numCols()):
                theNewGrid[col,row] = self._theGrid[row, col]

        return theNewGrid

    # add
    def __add__(self, rhsMatrix):
    
        assert rhsMatrix.numRows() == self._theGrid.numRows() and \
           rhsMatrix.numCols() == self._theGrid.numCols(), \
            "Matrix sizes not compatible"
            
        theNewGrid = MyMatrix(self._theGrid.numRows(), self._theGrid.numCols())

        for row in range(self._theGrid.numRows()):
            for col in range(self._theGrid.numCols()):
                theNewGrid[row,col] = self._theGrid[row,col] + rhsMatrix[row,col]

        return theNewGrid

    # sub
    def __sub__(self, rhsMatrix):

        assert rhsMatrix.numRows() == self._theGrid.numRows() and \
           rhsMatrix.numCols() == self._theGrid.numCols(), \
            "Matrix sizes not compatible"
                
        theNewGrid = MyMatrix(self._theGrid.numRows(), self._theGrid.numCols())

        for row in range(self._theGrid.numRows()):
            for col in range(self._theGrid.numCols()):
                theNewGrid[row,col] = self._theGrid[row,col] - rhsMatrix[row,col]

        return theNewGrid

    # mul
    def __mul__(self, rhsMatrix):

        assert self._theGrid.numCols() == rhsMatrix.numRows(), \
            "Matrix sizes not compatible"
            
        theNewGrid = MyMatrix(self._theGrid.numRows(), rhsMatrix.numCols())
        
        for row in range(self._theGrid.numRows()):
            for col in range(rhsMatrix.numCols()):
                total = 0
                
                for mid in range(self._theGrid.numCols()):
                    total += self._theGrid[row,mid] * rhsMatrix[mid,col]

                theNewGrid[row,col] = total

        return theNewGrid
    
def test_matrix():
   
    # Import
    import random

    # set default value for matrix
    aMatrix = MyMatrix(2,3)
    bMatrix = MyMatrix(2,3)
    fMatrix = MyMatrix(3,2)

    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            aMatrix[i,j] = random.randint(1,2)
            bMatrix[i,j] = random.randint(1,2)

    for i in range(fMatrix.numRows()):
        for j in range(fMatrix.numCols()):
            fMatrix[i,j] = random.randint(1,2)
                     
    print 'The primary value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            print '%s ' % aMatrix[i,j], 
        print '\r'   

    print '\nThe primary value of bmatrix'
    for i in range(bMatrix.numRows()):
        for j in range(bMatrix.numCols()):
            print '%s ' % bMatrix[i,j], 
        print '\r'  
        
    print '\nThe primary value of fmatrix'
    for i in range(fMatrix.numRows()):
        for j in range(fMatrix.numCols()):
            print '%s ' % fMatrix[i,j], 
        print '\r'    

    # add amatrix and bmatrix to cmatrix
    cMatrix = aMatrix + bMatrix
    
    print '\nThe value of cMatrix (aMatrix + bMatrix)'
    for i in range(cMatrix.numRows()):
        for j in range(cMatrix.numCols()):
            print '%s ' % cMatrix[i,j], 
        print '\r'   

    # sub amatrix and bmatrix to dmatrix
    dMatrix = aMatrix - bMatrix
    
    print '\nThe value of dMatrix (aMatrix - bMatrix)'
    for i in range(dMatrix.numRows()):
        for j in range(dMatrix.numCols()):
            print '%s ' % dMatrix[i,j], 
        print '\r'   
   
    # Mul amatrix and fMatrix to ematrix
    eMatrix = aMatrix * fMatrix
    
    print '\nThe value of eMatrix (aMatrix * fMatrix)'
    for i in range(eMatrix.numRows()):
        for j in range(eMatrix.numCols()):
            print '%s ' % eMatrix[i,j], 
        print '\r'  
                          
    # Scale the amatrix by 3
    aMatrix.scaleBy(3)
    
    print '\nThe scale value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            print '%s ' % aMatrix[i,j], 
        print '\r'   
        
    # Transpose the amatrix 
    dMatrix = aMatrix.transpose()
    
    print '\nThe transpose value of amatrix'
    for i in range(dMatrix.numRows()):
        for j in range(dMatrix.numCols()):
            print '%s ' % dMatrix[i,j], 
        print '\r'   
        
'''
The primary value of amatrix
1  1  1  
1  1  2  

The primary value of bmatrix
1  1  2  
1  1  2  

The primary value of fmatrix
1  2  
1  2  
2  2  

The value of cMatrix (aMatrix + bMatrix)
2  2  3  
2  2  4  

The value of dMatrix (aMatrix - bMatrix)
0  0  -1  
0  0  0  

The value of eMatrix (aMatrix * fMatrix)
4  6  
6  8  

The scale value of amatrix
3  3  3  
3  3  6  

The transpose value of amatrix
3  3  
3  3  
3  6  
'''
if __name__ == "__main__":
    test_matrix()

# listSpareMatrix
class SparseMatrix:

    # init
    def __init__(self, row, col):
        self._nrows = row
        self._ncols = col
        self._theElements = list()

    # get the row
    def numRows(self):
        return self._nrows

    # get the col
    def numCols(self):
        return self._ncols

    # set the item
    def __setitem__(self, nTuple, scalar):
        ndx = self._findPosition(nTuple[0], nTuple[1])
        if ndx is not None:
            if scalar != 0.0:
                self._theElements[ndx].value = scalar
            else:
                self._theElements.pop(ndx)
        else:
            if scalar != 0.0:
                element = _MatrixElement(nTuple[0], nTuple[1], scalar) 
                self._theElements.append(element)   

    # get the item
    def __getitem__(self, nTuple):
        ndx = self._findPosition(nTuple[0], nTuple[1])
        assert ndx is not None, "item is not exists or its value is 0."
        return self._theElements[ndx].value

    # scale
    def scaleBy(self, scalar):
        for item in self._theElements:
            item.value *= scalar

    # add
    def __add__(self, rhsMatrix):

        assert self.numRows() == rhsMatrix.numRows() and \
               self.numCols() == rhsMatrix.numCols(), "matrix is not compitable!"

        # Create a new matrix
        newSparseMatrix = SparseMatrix(self.numRows(), self.numCols())

        for element in self._theElements:
            dupElement = _MatrixElement(element.row, element.col, element.value)
            newSparseMatrix._theElements.append(dupElement)

        for element in rhsMatrix._theElements:
            value = newSparseMatrix[element.row, element.col]
            value += element.value
            newSparseMatrix[element.row, element.col] = value

        return newSparseMatrix
    
    # sub
    def __sub__(self, rhsMatrix):

        assert self.numRows() == rhsMatrix.numRows() and \
               self.numCols() == rhsMatrix.numCols(), "matrix is not compitable!"

        # Create a new matrix
        newSparseMatrix = SparseMatrix(self.numRows(), self.numCols())

        for element in self._theElements:
            dupElement = _MatrixElement(element.row, element.col, element.value)
            newSparseMatrix._theElements.append(dupElement)

        for element in rhsMatrix._theElements:
            value = newSparseMatrix[element.row, element.col]
            value -= element.value
            newSparseMatrix[element.row, element.col] = value

        return newSparseMatrix
    

    def __mul__(self, rhsMatrix):

        assert self.numCols() == rhsMatrix.numRows(), "Matrix is not matching!"

        # Create a new matrix
        newSparseMatrix = SparseMatrix(self.numRows(), rhsMatrix.numCols())

        # Do the loop
        for row in range(self.numRows()):
            for col in range(rhsMatrix.numCols()):
                sum_ = 0
                for mid in range(self.numCols()):
                    ndxA = self._findPosition(row, mid)
                    ndxB = rhsMatrix._findPosition(mid, col)
                    if ndxA is not None and ndxB is not None:
                        sum_ += self[row, mid] * rhsMatrix[mid, col]
                element = _MatrixElement(row, col, sum_)
                newSparseMatrix._theElements.append(element)

        return newSparseMatrix

    # find position
    def _findPosition(self, row, col):
        n = len(self._theElements)
        for i in range(n):
            if self._theElements[i].row == row and \
               self._theElements[i].col == col:
                return i
        return None

# Storage class
class _MatrixElement:
    # init
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        
def test_matrix():
   
    # Import
    import random

    # set default value for matrix
    aMatrix = SparseMatrix(2,3)
    bMatrix = SparseMatrix(2,3)
    fMatrix = SparseMatrix(3,2)

    aMatrix[0,0] = random.randint(1,10)
    aMatrix[1,1] = random.randint(1,10)
    
    bMatrix[0,0] = random.randint(1,10)
    bMatrix[1,1] = random.randint(1,10)
    
    fMatrix[0,0] = random.randint(1,10)
    fMatrix[1,1] = random.randint(1,10)
                     
    print 'The primary value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            ndx = aMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % aMatrix[i,j], 
        print '\r'   

    print '\nThe primary value of bmatrix'
    for i in range(bMatrix.numRows()):
        for j in range(bMatrix.numCols()):
            ndx = bMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % bMatrix[i,j], 
        print '\r'  
        
    print '\nThe primary value of fmatrix'
    for i in range(fMatrix.numRows()):
        for j in range(fMatrix.numCols()):
            ndx = fMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % fMatrix[i,j], 
        print '\r'    

    # add amatrix and bmatrix to cmatrix
    cMatrix = aMatrix + bMatrix
    
    print '\nThe value of cMatrix (aMatrix + bMatrix)'
    for i in range(cMatrix.numRows()):
        for j in range(cMatrix.numCols()):
            ndx = cMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % cMatrix[i,j], 
        print '\r'   

    # sub amatrix and bmatrix to dmatrix
    dMatrix = aMatrix - bMatrix
    
    print '\nThe value of dMatrix (aMatrix - bMatrix)'
    for i in range(dMatrix.numRows()):
        for j in range(dMatrix.numCols()):
            ndx = dMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % dMatrix[i,j], 
        print '\r'   
   
    # Mul amatrix and fMatrix to ematrix
    eMatrix = aMatrix * fMatrix
    
    print '\nThe value of eMatrix (aMatrix * fMatrix)'
    for i in range(eMatrix.numRows()):
        for j in range(eMatrix.numCols()):
            ndx = eMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % eMatrix[i,j], 
        print '\r'  
                          
    # Scale the amatrix by 3
    aMatrix.scaleBy(3)
    
    print '\nThe scale value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            ndx = aMatrix._findPosition(i, j)
            if ndx is None:
                print '0 ',
            else:
                print '%s ' % aMatrix[i,j], 
        print '\r'   
            
'''
The primary value of amatrix
8  0  0  
0  2  0  

The primary value of bmatrix
8  0  0  
0  6  0  

The primary value of fmatrix
8  0  
0  4  
0  0  

The value of cMatrix (aMatrix + bMatrix)
16  0  0  
0  8  0  

The value of dMatrix (aMatrix - bMatrix)
0  0  0  
0  -4  0  

The value of eMatrix (aMatrix * fMatrix)
64  0  
0  8  

The scale value of amatrix
24  0  0  
0  6  0  
'''    
if __name__ == "__main__":
    test_matrix()

# arrayLinkedSpareMatrix
from newarray import Array

class ArrayLinkedSpareMatrix:
    # Init
    def __init__(self, numRows, numCols):
        self._numCols = numCols
        self._listOfRows = Array(numRows)

    # The number of row
    def numRows(self):
        return len(self._listOfRows)

    # The number of col
    def numCols(self):
        return self._numCols

    # Get the item
    def __getitem__(self, nTuple):
        row = nTuple[0]
        col = nTuple[1]
        assert row >= 0 and row < self.numRows() and \
              col >= 0 and col < self.numCols(), "Out of subscript."
        
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            curNode = curNode.next

        if curNode is not None:
            return curNode.value

        return 0.0

    # Set the item
    def __setitem__(self, nTuple, value):
        row = nTuple[0]
        col = nTuple[1]
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Out of subscript."

        
        preNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            preNode = curNode
            curNode = curNode.next

        if curNode is not None and curNode.col == col:
            if value == 0.0:
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else:
                    preNode.next = curNode.next
            else:
                curNode.value = value
        elif value != 0.0:
            newNode = _MatrixElement(col, value)
            newNode.next = curNode
            if curNode == self._listOfRows[row]:
                self._listOfRows[row] = newNode
            else:
                preNode.next = curNode

    # Scale by
    def scaleBy(self, scalar):

        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                curNode.value *= scalar
                curNode = curNode.next

    # Add
    def __add__(self, rhsMatrix):
        assert self.numRows() == rhsMatrix.numRows() and \
             self.numCols() == rhsMatrix.numCols(), \
                  "Can not compitible!"

        newMatrix = ArrayLinkedSpareMatrix(self.numRows(), self.numCols())

        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next

        for row in range(self.numRows()):
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] += curNode.value
                curNode = curNode.next

        return newMatrix

    # Sub
    def __sub__(self, rhsMatrix):
        assert self.numRows() == rhsMatrix.numRows() and \
             self.numCols() == rhsMatrix.numCols(), \
                  "Can not compitible!"

        newMatrix = ArrayLinkedSpareMatrix(self.numRows(), self.numCols())

        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next

        for row in range(self.numRows()):
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] -= curNode.value
                curNode = curNode.next

        return newMatrix


    # Transpose
    def transpose(self):
        newMatrix = ArrayLinkedSpareMatrix(self.numCols(), self.numRows())
        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[curNode.col, row] = curNode.value
                curNode = curNode.next

        return newMatrix

    # Mulitply
    def __mul__(self, rhsMatrix):
        assert self.numCols() == rhsMatrix.numRows(), \
               "not compitible!"
        newMatrix = ArrayLinkedSpareMatrix(self.numRows(), rhsMatrix.numCols())

        for row in range(self.numRows()):
            for col in range(rhsMatrix.numCols()):
                sum_ = 0.0
                for mid in range(self.numCols()):
                    sum_ += self[row, mid] * rhsMatrix[mid, col]
                newMatrix[row, col] = sum_

        return newMatrix   
    
    # Iterator
    def __iter__(self):
        return _SparseMatrixIter(self._listOfRows)

# Array linked matrix node
class _MatrixElement:
    # Init
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None     
        
# Defines a Python iterator for the Sparse Matrix ADT 
# implemented using an array of linked lists
class _SparseMatrixIterator:
    def __init__(self, rowArray):
        self._rowArray = rowArray
        self._curRow = 0
        self._curNode = None
        self._findNextElement()
        
    def __iter__(self):
        return self

    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            value = self._curNode.value
            self._curNode = self._curNode.next
            if self._curNode is None:
                self._findNextElement()
            print 'value:', value
            return value

    def _findNextElement(self):
        i = self._curRow
        while i < len(self._rowArray) and \
                 self._rowArray[i] is None:
            i += 1

        self._curRow = i
        if i < len(self._rowArray):
            self._curNode = self._rowArray[i]
        else:
            self._curNode = None         
            
        print 'find:', self._curNode
        
class _SparseMatrixIter:
    # Init
    def __init__(self, listOfRows):
        self.ndx = 0
        self.listOfRows = listOfRows

        self.items = list()
        for row in range(len(listOfRows)):
            curNode = listOfRows[row]
            while curNode is not None:
                self.items.append(curNode.value)
                curNode = curNode.next

    def __iter__(self):
        return self
    def next(self):
        if self.ndx < len(self.items):
            value = self.items[self.ndx]
            self.ndx += 1
            return value
        else:
            raise StopIteration

def test_matrix():
   
    # Import
    import random

    # set default value for matrix
    aMatrix = ArrayLinkedSpareMatrix(2,3)
    bMatrix = ArrayLinkedSpareMatrix(2,3)
    fMatrix = ArrayLinkedSpareMatrix(3,2)

    aMatrix[0,0] = random.randint(1,10)
    aMatrix[1,1] = random.randint(1,10)
    
    bMatrix[0,0] = random.randint(1,10)
    bMatrix[1,1] = random.randint(1,10)
    
    fMatrix[0,0] = random.randint(1,10)
    fMatrix[1,1] = random.randint(1,10)
                     
    print 'The primary value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            print '%s ' % aMatrix[i,j], 
        print '\r'   

    print '\nThe primary value of bmatrix'
    for i in range(bMatrix.numRows()):
        for j in range(bMatrix.numCols()):
            print '%s ' % bMatrix[i,j], 
        print '\r'  
        
    print '\nThe primary value of fmatrix'
    for i in range(fMatrix.numRows()):
        for j in range(fMatrix.numCols()):
            print '%s ' % fMatrix[i,j], 
        print '\r'    

    # add amatrix and bmatrix to cmatrix
    cMatrix = aMatrix + bMatrix
    
    print '\nThe value of cMatrix (aMatrix + bMatrix)'
    for i in range(cMatrix.numRows()):
        for j in range(cMatrix.numCols()):
            print '%s ' % cMatrix[i,j], 
        print '\r'   

    # sub amatrix and bmatrix to dmatrix
    dMatrix = aMatrix - bMatrix
    
    print '\nThe value of dMatrix (aMatrix - bMatrix)'
    for i in range(dMatrix.numRows()):
        for j in range(dMatrix.numCols()):
            print '%s ' % dMatrix[i,j], 
        print '\r'   
   
    # Mul amatrix and fMatrix to ematrix
    eMatrix = aMatrix * fMatrix
    
    print '\nThe value of eMatrix (aMatrix * fMatrix)'
    for i in range(eMatrix.numRows()):
        for j in range(eMatrix.numCols()):
            print '%s ' % eMatrix[i,j], 
        print '\r'  

                              
    # Scale the amatrix by 3
    aMatrix.scaleBy(3)
    
    print '\nThe scale value of amatrix'
    for i in range(aMatrix.numRows()):
        for j in range(aMatrix.numCols()):
            print '%s ' % aMatrix[i,j], 
        print '\r'   
        
    print '\nCheck the iterator'
    for i in aMatrix:
        print i,
                
'''
The primary value of amatrix
4  0.0  0.0  
0.0  5  0.0  

The primary value of bmatrix
4  0.0  0.0  
0.0  8  0.0  

The primary value of fmatrix
4  0.0  
0.0  6  
0.0  0.0  

The value of cMatrix (aMatrix + bMatrix)
8  0.0  0.0  
0.0  13  0.0  

The value of dMatrix (aMatrix - bMatrix)
0.0  0.0  0.0  
0.0  -3  0.0  

The value of eMatrix (aMatrix * fMatrix)
16.0  0.0  
0.0  30.0  

The scale value of amatrix
12  0.0  0.0  
0.0  15  0.0  

Check the iterator
12 15
'''
if __name__ == "__main__":
    test_matrix() 
