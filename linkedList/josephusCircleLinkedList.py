'''
Question:
There are n people standing in a circle waiting to be executed. The counting out begins at some point in the circle and
 proceeds around the circle in a fixed direction. In each step, a certain number of people are skipped and the next 
 person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the 
 executed people are removed), until only the last person remains, who is given freedom. Given the total number
  of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle. 
  The task is to choose the place in the initial circle so that you are the last one remaining and so survive.

For example, if n = 5 and k = 2, then the safe position is 3. Firstly, the person at position 2 is killed, then
 person at position 4 is killed, then person at position 1 is killed. Finally, the person at position 5 is killed. 
 So the person at position 3 survives.
If n = 7 and k = 3, then the safe position is 4. The persons at positions 3, 6, 2, 7, 5, 1 are killed in order,
 and person at position 4 survives.

picture display:
http://thedailywtf.com/articles/Programming-Praxis-Josephus-Circle
'''

'''
Solution one:
  josephuse circle using number, any step
  refer:http://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
'''
def josephusCircleOne(n, k):

    if n == 1:
        return 1
    else:
        '''
        The position returned by josephus circle (n-1,  k) is 
        adjusted because the recursive call josephus(n-1, k) considers
        original position k%n + 1 as position 1
        '''
        return (josephusCircleOne(n-1, k) + k -1) % n +1

def mainOne():

    print ':::5 node, step is 2'
    print '''
        5 
            1
    4       2
        3
    '''
    n = 5
    k = 2
    print("The chosen place using soluation one is %d", josephusCircleOne(n, k))
    
    print '\r:::7 node, step is 3'
    print '''
        7 
            1
    6       2
    5       3
        4
    '''
    n = 7
    k = 3
    print("The chosen place using soluation one is %d", josephusCircleOne(n, k))

'''
 Solution two: any number, step is 2
 refer:http://www.geeksforgeeks.org/josephus-problem-set-2-simple-solution-k-2/
'''
def josephusCircleTwo(n):

    '''
    Find value of 2 ^ (1+floor(Log n))
    which is a power of 2 whose value
    is just above n
    '''
    p = 1
    while (p <= n):
        p *= 2

    '''
    Return 2n - 2^(1+floor(logn)) + 1
    '''
    return 2*n - p + 1

def mainTwo():

    print ':::5 node, step is 2'
    print '''
        5 
            1
    4       2
        3
    '''
    n = 5
    print("The chosen place uisng soluation two is %d", josephusCircleTwo(n))
    
    print '\r:::7 node, step is 3'
    print '''
        7 
            1
    6       2
    5       3
        4
    '''
    n = 16
    print("The chosen place using soluaton two is %d", josephusCircleTwo(n))
    
"""
:::5 node, step is 2

        5 
            1
    4       2
        3
    
('The chosen place using soluation one is %d', 3)

:::7 node, step is 3

        7 
            1
    6       2
    5       3
        4
    
('The chosen place using soluation one is %d', 4)
:::5 node, step is 2

        5 
            1
    4       2
        3
    
('The chosen place uisng soluation two is %d', 3)

:::7 node, step is 3

        7 
            1
    6       2
    5       3
        4
    
('The chosen place using soluaton two is %d', 1)
"""
if __name__ == "__main__":
    mainOne()
    mainTwo()
