/*
方法一： 使用递归
×/
#include <iostream>
#include <queue>
using namespace std;

void reverse(queue <int> &q)
{
    if(q.empty())
        return;

    int num = q.front();
    q.pop();
    reverse(q);
    q.push(num);
}

int main()
{
    int arr[] = {1,4,6,8,2,5,10,12,14};
    queue<int> q;

    for (int i=0; i<9; i++)
    {
        q.push(arr[i]);        
    }
    reverse(q);
    for (int i=0; i<9; i++)
    {
        cout << q.front() << " ";
        q.pop();
    }
    return 0;
}

/×
方法二： 使用外部数据结构： Stack
×/
void ReverseQueue(struct Queue *Q) {
    struct Stack *S = CreateStack();
    while (!IsEmptyQueue(Q))
        Push(S, DeQueue(Q))
    while (!IsEmptyStack(S))
        EnQueue(Q, Pop(S));
}
