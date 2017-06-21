/*
Given a string, write a c function to check if it is palindrome or not. 
A string is said to be palindrome if reverse of the string is same as string. 
For example, “abba” is palindrome, but “abbc” is not palindrome.

Algorithm:  (iterative)
isPalindrome(str)
1) Find length of str. Let length be n.
2) Initialize low and high indexes as 0 and n-1 respectively.
3) Do following while low index ‘l’ is smaller than high index ‘h’.
…..a) If str[l] is not same as str[h], then return false.
…..b) Increment l and decrement h, i.e., do l++ and h–.
4) If we reach here, it means we didn’t find a mis
*/
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

//A function to check if a string str is palindrome
void isPalindromeIter(char str[])
{
    //Start from leftmost and rightmost corners of str
    int l = 0;
    int h = strlen(str) - 1;

    //Keep comparing characters while they are the same
    while (l < h)
    {
        if (str[l++] != str[h--])
        {
            printf("%s is not Palindrome\n", str);
            return;
        }
    }
    printf("%s is palindrome\n", str);
}

/*
A recursive function that check a str[s..e]

Algorithms: (recursive)
1) If there is only one character in string
   return true.
2) Else compare first and last characters
   and recur for remaining substring.
*/
//is palindrome or not
bool isPalRec(char str[], int s, int e)
{
    //If there is only one character
    if (s == e)
        return true;

    //If first and last characters do not match
    if (str[s] != str[e])
        return false;

    //If there are more than two characters
    //check if middle substring is also
    //palindrome or not
    if (s < e+1)
        return isPalRec(str, s+1, e-1);

    return true;

}

bool isPalindromeRec(char str[])
{
    int n = strlen(str);

    //An empty string is considereed as palindrome
    if (n == 0)
        return true;

    return isPalRec(str, 0, n-1);
}
// Driver program to test above function
int main()
{
    isPalindromeIter("abba");
    isPalindromeIter("abbccbba");
    isPalindromeIter("geeks");
    
    printf("%d\n", isPalindromeRec("abba"));
    printf("%d\n", isPalindromeRec("abbccbba"));
    printf("%d\n", isPalindromeRec("geeks"));
    
    return 0;
}

/*
abba is palindrome
abbccbba is palindrome
geeks is not Palindrome
1
1
0
*/
