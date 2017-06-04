/*
Question:
 Given a list, List1 = {A1, A2, ...An-1, An} with data, reorder it to 
        {A1, An, A2, An-1} without using any extra space

Algorithms:
1) Find the middle point using tortoise and hare method
2) Split the linked list in two halves using found middle point in step 1
3) Reverse the second half
4) Do alternate merge of first and second halves

Time Complexity:
O(n)

Output:
1 -> 2 -> 3 -> 4 -> 5
1 -> 5 -> 2 -> 4 -> 3
*/
//Rearrance a linked list in-place
using namespace std;

//Linkedlist node structure
struct Node
{
    int data;
    struct Node *next;
};

//Create newNode in a linkedlist
Node* newNode(int key)
{
    Node* temp = new Node;
    temp->data = key;
    temp->next = NULL;
    return temp;
}

//Reverse the linked list
void reverseList(Node **head)
{
    //Initialize prev and curret pointers
    Node *prev = NULL, *curr = *head, *next;

    while(curr)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    *head = prev;
}

// Print the linked list
void printList(Node *head)
{
    while (head != NULL)
    {
        cout << head->data << " ";
        if(head->next) cout << "-> ";
        head = head->next;
    }
    cout << endl;
}

//Rearrange a linked list
void rearrange(Node **head)
{
    //1) Find the middle point using tortoise and hare method
    Node *slow = *head, *fast = slow->next;
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    //2) Split the linked list in two halves
    //head1, head of first half 
    //head2, head of second half
    Node *head1 = *head;
    Node *head2 = slow->next;
    slow->next = NULL;

    //3) Reverse the second half
    reverseList(&head2);

    //4) Merge alternate nodes
    *head = newNode(0);  //Assignn dummy node

    //curr is the pointer to this dummy Node, which will
    // be used to form the new list
    Node *curr = *head;

    while (head1 || head2)
    {
        //First add the element from list
        if (head1)
        {
  
            curr->next = head1;
            curr = curr->next;
            head1 = head1->next;
        }

        //Then add the element from second list
        if (head2)
        {
            curr->next = head2;
            curr = curr->next;
            head2 = head2->next;
        }
    } 

    //Assign the head of the new list to head pointer
    *head = (*head)->next;
}

//Driver program
int main()
{
    Node *head = newNode(1);
    head->next = newNode(2);
    head->next->next = newNode(3);
    head->next->next->next = newNode(4);
    head->next->next->next->next = newNode(5);

    printList(head);   //Print original list
    rearrange(&head);  //Modify the list
    printList(head);   //Print modified list

    return 0;
}
