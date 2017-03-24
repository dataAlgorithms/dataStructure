# coding=utf-8

'''
/*
 ============================================================================
XOR Linked List – A Memory Efficient Doubly Linked List
 ============================================================================


      A        B       C         D
         <–>  A⊕C  <->  B⊕D  <->


Consider the above Doubly Linked List. Following are the Ordinary and XOR (or Memory Effiecient) representations of the Doubly Linked List.

XOR List Representation:
Let us call the address variable in XOR representation npx (XOR of next and previous)

Node A:
npx = 0 XOR add(B) // bitwise XOR of zero and address of B

Node B:
npx = add(A) XOR add(C) // bitwise XOR of address of A and address of C

Node C:
npx = add(B) XOR add(D) // bitwise XOR of address of B and address of D

Node D:
npx = add(C) XOR 0 // bitwise XOR of address of C and 0


Result:
10 9 8 7 6 1 2 3 4 5
8 7 6 1 2 3
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct node {
    int item;
    struct node *np;
} node;

node *head, *tail;

typedef unsigned int uintptr_t;

node *myxor(node *a, node *b)
{
    return (node*) ((uintptr_t) a ^ (uintptr_t) b);
}

void insert(int item, bool at_tail)
{
    node *ptr = (node*)malloc(sizeof(node));
    ptr->item = item;

    if (NULL == head) {
        ptr->np = NULL;
        head = tail = ptr;
    } else if (at_tail) {
        ptr->np = myxor(tail, NULL);
        tail->np = myxor(ptr, myxor(tail->np, NULL));
        tail = ptr;
    } else {
        ptr->np = myxor(NULL, head);
        head->np = myxor(ptr, myxor(NULL, head->np));
        head = ptr;
    }
}

int delete(bool from_tail)
{
    if (NULL == head) {
        printf("Empty list.\n");
        exit(1);
    } else if (from_tail) {
        node *ptr = tail;
        int item = ptr->item;
        node *prev = myxor(ptr->np, NULL);
        if (NULL == prev) head = NULL;
        else prev->np = myxor(ptr, myxor(prev->np, NULL));
        tail = prev;
        free(ptr);
        ptr = NULL;
        return item;
    } else {
        node *ptr = head;
        int item = ptr->item;
        node *next = myxor(NULL, ptr->np);
        if (NULL == next) tail = NULL;
        else next->np = myxor(ptr, myxor(NULL, next->np));
        head = next;
        free(ptr);
        ptr = NULL;
        return item;
    }
}

void list()
{
    node *curr = head;
    node *prev = NULL, *next;

    while (NULL != curr) {
        printf("%d ", curr->item);
        next = myxor(prev, curr->np);
        prev = curr;
        curr = next;
    }

    printf("\n");
}

void xorLinkedList()
{
    for (int i = 1; i<=10; i++)
        insert(i,  i<6);

    list();

    for (int i=1; i <= 4; i++)
        delete(i < 3);

    list();
}

int main(int argc, char *argv[])
{
    xorLinkedList();
}
'''

'''
使用Python的ctypes，我们可以直接调用由C直接编译出来的函数。其实就是调用动态链接库中的函数。为什么我们需要这样做呢，因为有些时候，
我们可能需要一个性能上比较讲究的算法，有些时候，我们可以在Python中使用已经有了的现成的被封闭在动态链接库中的函数。下面是如何调用的示例。

首先，我们用一个乘法来表示一个算法功能。下面是C的程序：

1
2
3
4
5
int
multiply(int num1, int num2)
{
    return num1 * num2;
}

如果在Windows下，你可能需要写成下面这个样子：

1
2
3
4
5
6
7
8
9
10
11
12
13
14
#include <windows.h>
 
 
BOOL APIENTRY
DllMain(HANDLE hModule, DWORD dwReason, LPVOID lpReserved)
{
    return TRUE;
}
 
__declspec(dllexport) int
multiply(int num1, int num2)
{
    return num1 * num2;
}
然后，自然是把这个C文件编成动态链接库：

Linux下的编译：

1
2
gcc -c -fPIC libtest.c
gcc -shared libtest.o -o libtest.so
Windows下的编译：

1
cl -LD libtest.c -libtest.dll
于是在我们的Python中可以这样使用：
(其中的libtest.so在Windows下改成libtest.dll即可)

1
2
3
4
5
>>> from ctypes import *
>>> import os
>>> libtest = cdll.LoadLibrary(os.getcwd() + '/libtest.so')
>>> print libtest.multiply(2, 2)
4
注意：上面的Python脚本中需要把动态链接库放到当前目录中。
'''
