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
