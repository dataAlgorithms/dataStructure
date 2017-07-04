//方法一
/*
Question:
Recursively remove all adjacent duplicates

Example:
Input:  azxxzy
Output: ay
First "azxxzy" is reduced to "azzy". The string "azzy" contains duplicates, 
so it is further reduced to "ay".

Input: geeksforgeeg
Output: gksfor
First "geeksforgeeg" is reduced to "gksforgg". The string "gksforgg" contains 
duplicates, so it is further reduced to "gksfor".

Input: caaabbbaacdddd
Output: Empty String

Input: acaaabbbacdddd
Output: acac

Algorithms:
A simple approach would be to run the input string through multiple passes. 
In every pass remove all adjacent duplicates from left to right. 
Stop running passes when there are no duplicates.

Time complexity:
 The worst time complexity of this method would be O(n^2).

*/

#include <iostream>
#include <string.h>
using namespace std;

// remove duplicates and returns modified string
char* removeDup(char *str, int n)
{
    int len = strlen(str);
    int k = 0; // store index of result
    int i;

    // start from second character and add unique ones
    for (i = 1; i < len; i++)
    {
        // If different, increment k and add previous character
        if (str[i-1] != str[i])
            str[k++] = str[i-1];
        else
            // Keep skipping (removing) characters
            // while they are same
            while (str[i-1] == str[i])
                i++;
    }

    // Add last character and terminator
    str[k++] = str[i-1];
    str[k] = '\0';

    // Recur for string if there were some removed character
    if (k != n)
        removeDup(str, k); // Shlemial Painter's Algorithms

    // If all characters were unique
    else
        return str;
}

/*
gksfor
ay

g
a

qrq
acac
a
*/
int main()
{
    char str1[] = "geeksforgeeg";
    cout << removeDup(str1, strlen(str1)) << endl;
 
    char str2[] = "azxxxzy";
    cout << removeDup(str2, strlen(str2)) << endl;
 
    char str3[] = "caaabbbaac";
    cout << removeDup(str3, strlen(str3)) << endl;
 
    char str4[] = "gghhg";
    cout << removeDup(str4, strlen(str4)) << endl;
 
    char str5[] = "aaaacddddcappp";
    cout << removeDup(str5, strlen(str5)) << endl;
 
    char str6[] = "aaaaaaaaaa";
    cout << removeDup(str6, strlen(str6)) << endl;
 
    char str7[] = "qpaaaaadaaaaadprq";
    cout << removeDup(str7, strlen(str7)) << endl;
 
    char str8[] = "acaaabbbacdddd";
    cout << removeDup(str8, strlen(str8)) << endl;
 
    char str9[] = "acbbcddc";
    cout << removeDup(str9, strlen(str9)) << endl;
}

//方法二
/*
Question:
Recursively remove all adjacent duplicates
Given a string, recursively remove adjacent duplicate characters from string. 
The output string should not have any adjacent duplicates. See following examples.

Input:  azxxzy
Output: ay
First "azxxzy" is reduced to "azzy". The string "azzy" contains duplicates, 
so it is further reduced to "ay".

Input: geeksforgeeg
Output: gksfor
First "geeksforgeeg" is reduced to "gksforgg". The string "gksforgg" contains 
duplicates, so it is further reduced to "gksfor".

Input: caaabbbaacdddd
Output: Empty String

Input: acaaabbbacdddd
Output: acac

Algorithms:
1) Start from the leftmost character and remove duplicates at left corner if there are any.
2) The first character must be different from its adjacent now. Recur for string of length n-1 (string without first character).
3) Let the string obtained after reducing right substring of length n-1 be rem_str. There are three possible cases
……..a) If first character of rem_str matches with the first character of original string, remove the first character from rem_str.
……..b) Else if the last removed character in recursive calls is same as the first character of the original string.
 Ignore the first character of original string and return rem_str.
……..c) Else, append the first character of the original string at the beginning of rem_str.
4) Return rem_str.

Time Complexity:
 The time complexity of the solution can be written as T(n) = T(n-k) + O(k) 
where n is length of the input string and k is the number of first characters 
which are same. 
Solution of the recurrence is O(n)

*/

#include <iostream>
#include <string.h>
using namespace std;

// Recursively removes adjacent duplicates from str and returns
// new string, las_removed is a pointer to last_removed character
char *removeUtil(char *str, char * last_removed)
{
    // If length of string is 1 or 0
    if (str[0] == '\0' || str[1] == '\0')
        return str;

    // Remove leftmost same characters and recur for remaining string
    if (str[0] == str[1])
    {
        *last_removed = str[0];
        while (str[1] && str[0] == str[1])
            str++;
        str++;

        return removeUtil(str, last_removed);
    }

    // At this point, the first character is definitely different
    // from its adjacent. Ignore first character and recursively
    // remove characters from remaining string
    char * rem_str = removeUtil(str+1, last_removed);

    // Check if the first character  of the rem_string matches with
    // the first character of the original string
    if (rem_str[0] && rem_str[0] == str[0])
    {
        *last_removed = str[0];
        return (rem_str+1); // remove first character
    }

    // If remaining string becomes empty and last removed character
    // is same as first character of original string, this is needed
    // for a string like acbbdddc
    if (rem_str[0] == '\0' && *last_removed == str[0])
        return rem_str;

    // If the two first characters of str and rem_str donot match
    // append first character of str before the first character of rem_str
    rem_str--;
    rem_str[0] = str[0];
    return rem_str;
}

char *remove(char *str)
{
    char last_removed = '\0';
    return removeUtil(str, &last_removed);
}

// Driver program to test above functions
int main()
{
    char str1[] = "geeksforgeeg";
    cout << remove(str1) << endl;

    char str2[] = "azxxxzy";
    cout << remove(str2) << endl;

    char str3[] = "caaabbbaac";
    cout << remove(str3) << endl;

    char str4[] = "gghhg";
    cout << remove(str4) << endl;

    char str5[] = "aaaacddddcappp";
    cout << remove(str5) << endl;

    char str6[] = "aaaaaaaaaa";
    cout << remove(str6) << endl;

    char str7[] = "qpaaaaadaaaaadprq";
    cout << remove(str7) << endl;

    char str8[] = "acaaabbbacdddd";
    cout << remove(str8) << endl;

    char str9[] = "acbbcddc";
    cout << remove(str9) << endl;

    return 0;
}

/*
gksfor
ay

g
a

qrq
acac
a
*/
