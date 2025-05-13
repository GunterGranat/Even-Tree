# Compare two linked list
You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. If all data attributes are equal and the lists are the same length, return . Otherwise, return .

Example

llist1 = 1-> 2-> 3-> NULL

The two lists have equal data attributes for the first  nodes.  is longer, though, so the lists are not equal. Return .

Function Description

Complete the compare_lists function in the editor below.

compare_lists has the following parameters:

SinglyLinkedListNode llist1: a reference to the head of a list
SinglyLinkedListNode llist2: a reference to the head of a list
Returns

int: return 1 if the lists are equal, or 0 otherwise
Input Format

The first line contains an integer , the number of test cases.

Each of the test cases has the following format:
The first line contains an integer , the number of nodes in the first linked list.
Each of the next  lines contains an integer, each a value for a data attribute.
The next line contains an integer , the number of nodes in the second linked list.
Each of the next  lines contains an integer, each a value for a data attribute.

Constraints

1 <= t <= 10
1 <= n,m <= 1000
1 <= llist1[i], llist2[i] <= 1000

Output Format

Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to stdout/console.

The output is handled by the code in the editor and it is as follows:

For each test case, in a new line, print  if the two lists are equal, else print 0.
