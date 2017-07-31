struct BinaryTreeNode {
    int data;
    struct BinaryTreeNode *left;
    struct BinaryTreeNode *right;
};

/*
Visit the root
Traverse the left subtree in Preorder
Traverse the right subtree in Preorder


Time Complexity: O(n)
Space Complexity: O(n)
*/
void PreOrder(struct BinaryTreeNode *root) {
    if (root) {
        printf("%d", root->data);
        PreOrder(root->left);
        PreOrder(root->right);
    }
}

/*
In the recursive version, a stack is required as we need to remember the current node so that after
completing the left subtree we can go to the right subtree. To simulate the same, first we process the
current node and before going to the left subtree, we store the current node on stack. After completing the
left subtree processing, pop the element and go to its right subtree. Continue this process until stack is
nonempty.


Time Complexity: O(n)
Space Complexity: O(n)
*/

void PreOrderNonRecursive(struct BinaryTreeNode *root) {
    struct Stack *S = createStack();

    while (1) {
        while (root) {
            //Process current node
            printf("%d", root->data);

            push(S, root);

            //If left subtree exists, add to stack
            root = root->left;
        }

        if (isEmptyStack(S))
            brerak;

        root = pop(S);

        //Indicates completion of left subtree and current node, now to g to right subtree
        root = root->right;
    }

    deleteStack(S);
}

/*
Algorithms:
Traverse the left subtree in Inorder
Visit the root
Traverse the right subtree in Inorder

Complexity:
Time: O(n)
Space: O(n)
*/
void InOrder(struct BinaryTreeNode *root) {
    if (root) {
        InOrder(root->left);
        printf("%d", root->data);
        InOrder(root->right);
    }
}

/*
Algorithms:

Complexity:
Time: O(n)
Space: O(n)
*/
void InOrderNonRecursive(struct BinaryTreeNode *root) {
    struct Stack *s = createStack();

    while (1) {
        while (root) {
            push(s, root);
            
            //Got left subtree and keep on adding to stack
            root = root->left;
        }

        if (isEmptyStack(s))
            break;

        root = pop(s);
        printf("%d", root->data);

        //Indicates completion of left subtree and current node
        //now to go to right subtree
        root = root->right;
    }

    deleteStack(s);
}

/*
Algo:
Traverse the left subtree in Postorder
Traverse the right subtree in Postorder
Visit the root

Complexity:
Time: O(n)
Space: O(n)
*/
void PostOrder(struct BinaryTreeNode *root) {
    if (root) {
        PostOrder(root->left);
        PostOrder(root->right);
        printf("%d", root->data);
    }
}

void PostOrderNonRecursive(struct BinaryTreeNode *root) {
    struct Stack *s = createStack();
    struct BinaryTreeNode *previous = NULL;

    do {
        while (root != NULL) {
            push(s, root);
            root = root->left;
        }

        while (root == NULL && !isEmptyStack(s)) {
            root = top(s);
            if(root->right == NULL || root->right == previous) {
                printf("%d ", root->data);
                pop(s);
                previous = root;
                root = NULL;
            }
            else
                root = root->right;
        }
    } while(!isEmptyStack(s));
}

/*
Algo:
Visit the root
While traversing level (, keep all the elements at level (+1 in queue
Go to next level and visit all the nodes at that level
Repeat this until all levels are completed

Complexity:
Time: O(n)
Space: O(n)
*/
void LevelOrder(struct BinaryTreeNode *root) {
    struct BinaryTreeNode *temp;
    struct Queue *q = createQueue();

    if (!root)
        return;

    enQueue(q, root);
    while (!isEmptyQueue(q)) {
        temp = deQueue(q);
        //Process current node
        printf("%d", temp->data);
        if (temp->left)
            enQueue(q, temp->left);
        if (temp->right)
            enQueue(q, temp->right);
    }

    deleteQueue(q);
}

/* Helper function that allocates a new node with the
   given data and NULL left and right pointers. */
struct BinaryTreeNode * newNode(int data)
{
     struct BinaryTreeNode * node = (struct BinaryTreeNode *)
                                  malloc(sizeof(struct BinaryTreeNode ));
     node->data = data;
     node->left = NULL;
     node->right = NULL;
 
     return(node);
}

/* Driver program to test above functions*/
int main()
{
     struct BinaryTreeNode *root  = newNode(1);
     root->left             = newNode(2);
     root->right           = newNode(3);
     root->left->left     = newNode(4);
     root->left->right   = newNode(5); 

     return 0;
}
