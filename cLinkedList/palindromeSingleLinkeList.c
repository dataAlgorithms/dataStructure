#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*
Method One: Reverse way

This method takes O(n) time and O(1) extra space.
1) Get the middle of the linked list.
2) Reverse the second half of the linked list.
3) Check if the first half and second half are identical.
4) Construct the original linked list by reversing the second half 
again and attaching it back to the first half
*/

/* Link list node */
struct Node
{
    char data;
    struct Node* next;
};

void reverse(struct Node**);
bool compareLists(struct Node*, struct Node*);

/* Check if given linked list is palindrome or not*/
bool isPalindrome(struct Node *head)
{
    struct Node *slow_ptr = head, *fast_ptr = head;
    struct Node *second_half, *prev_of_slow_ptr = head;
    struct Node *midnode = NULL; //To handle odd size list
    bool res = true;  //initialize result

    if (head != NULL && head->next != NULL)
    {
        /* Get the middle of the list, move slow_ptr by 1
           and fast_ptr by 2, slow_ptr will have the middle node
        */
        while (fast_ptr != NULL && fast_ptr->next != NULL)
        {
            fast_ptr = fast_ptr->next->next;

            /* We need previous of the slow_ptr for
               linked list with odd elements*/
            prev_of_slow_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        /* fast_ptr would become NULL when there are even elements in list
           and not NULL for odd elements. we need to skip the middle node
           for odd case and store it somewhere so that we can restore the 
           original list
        */
        if (fast_ptr != NULL)
        {
            midnode = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        //Now reverse the second half and compare it with first half
        second_half = slow_ptr;
        prev_of_slow_ptr->next = NULL; // NULL terminate first half
        reverse(&second_half);
        res = compareLists(head, second_half);

        //Consturct the original list back
        reverse(&second_half);

        //If there was a mid node (odd size case) which was not part of
        //first half or second half
        if (midnode != NULL)
        {
            prev_of_slow_ptr->next = midnode;
            midnode->next = second_half;
        }
        else
            prev_of_slow_ptr->next = second_half;
    }

    return res;
}

//reverse the linked list
void reverse(struct Node** head_ref)
{
    struct Node* prev = NULL;
    struct Node* current = *head_ref;
    struct Node* next;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head_ref = prev;
}

//compare linked list
bool compareLists(struct Node* head1, struct Node* head2)
{
    struct Node* temp1 = head1;
    struct Node* temp2 = head2;

    while (temp1 && temp2)
    {
        if (temp1->data == temp2->data)
        {
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        else
            return 0;
    }

    //Both are empty 
    if (temp1 == NULL && temp2 == NULL)
        return 1;

    //when one is NULL and other is not
    return 0;
}

//Push
void push(struct Node** head_ref, char new_data)
{
    //allocate node
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));

    //put in the data
    new_node->data = new_data;

    //link the old list off the new node
    new_node->next = (*head_ref);

    //move the head to new node
    (*head_ref) = new_node;
}

//Print
void printList(struct Node* ptr)
{
    while (ptr != NULL)
    {
        printf("%c->", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}


/*
Method Two: Recursive way
Use two pointers left and right. Move right and left using 
recursion and check for following in each recursive call.
1) Sub-list is palindrome.
2) Value at current left and right are matching.

If both above conditions are true then return true.

The idea is to use function call stack as container. Recursively traverse
 till the end of list. When we return from last NULL, we will be at last node.
 The last node to be compared with first node of list.

Time Complexity: O(n)
Auxiliary Space: O(n) if Function Call Stack size is considered, otherwise O(1).
*/

//Initial parameters to this function are &head and head
bool isPalindromeUtil(struct Node **left, struct Node *right)
{
    //stop recursion when right becomes NULL
    if (right == NULL)
        return true;

    //If subList is not palindrome then no need to
    //check for current left and right, return false
    bool isp = isPalindromeUtil(left, right->next);
    if (isp == false)
        return false;

    //check values at current left and right
    bool isp1 = (right->data == (*left)->data);

    //move left to next node
    *left = (*left)->next;

    return isp1;
}

//A wrapper
bool isPalindromeRec(struct Node *head)
{
    isPalindromeUtil(&head, head);
}



//Driver program
int main()
{
    struct Node* head = NULL;
    char str[] = "abacaba";
    int i;

    for (i = 0; str[i] != '\0'; i++)
    {
        push(&head, str[i]);
        printList(head);
        isPalindrome(head)? printf("Is Palindrome\n"):
                            printf("Not Palindrome\n");
        isPalindromeRec(head)? printf("Is Palindrome\n"):
                            printf("Not Palindrome\n");
    }

    return 0;
}

/*
a->NULL
Is Palindrome
Is Palindrome
b->a->NULL
Not Palindrome
Not Palindrome
a->b->a->NULL
Is Palindrome
Is Palindrome
c->a->b->a->NULL
Not Palindrome
Not Palindrome
a->c->a->b->a->NULL
Not Palindrome
Not Palindrome
b->a->c->a->b->a->NULL
Not Palindrome
Not Palindrome
a->b->a->c->a->b->a->NULL
Is Palindrome
Is Palindrome
*/
