

'''
Problem Statement for Egalitarianism

https://community.topcoder.com/stat?c=problem_statement&pm=12613
Problem Statement
    	A kingdom has n citizens. Each one has some amount of money, a number of dollars denoted by a non-negative integer.



Citizens are numbered from 0 to n-1. Some citizens have friends. Their friendship network is described by a String[] called isFriend, such that if isFriend[i][j] == 'Y', the citizens numbered i and j are friends, and if isFriend[i][j] == 'N', these citizens are not friends.



The king decrees the following:



Each citizen's amount of money must be within d dollars of the amount of money belonging to any of his friends. In other words, a citizen with x dollars must not have any friends with less than x-d dollars or more than x+d dollars.



Given the number of citizens and their friendship network, what is the greatest possible money difference between any two people (not necessarily friends) in this kingdom? If there is a finite answer, return it. Otherwise, return -1.
 
Definition
    	
Class:	Egalitarianism
Method:	maxDifference
Parameters:	String[], int
Returns:	int
Method signature:	int maxDifference(String[] isFriend, int d)
(be sure your method is public)
    
 
Constraints
-	n will be between 2 and 50, inclusive.
-	d will be between 0 and 1,000, inclusive.
-	isFriend will contain exactly n elements.
-	Each element of isFriend will contain exactly n characters, each of which is either 'Y' or 'N'.
-	For any i, isFriend[i][i] = 'N'.
-	For any i and j, isFriend[i][j] = isFriend[j][i].
 
Examples
0)	
    	
{"NYN",
 "YNY",
 "NYN"}
10
Returns: 20
The kingdom has three citizens. Citizens 0 and 1 are friends. Also, citizens 1 and 2 are friends. The greatest possible money difference between any two citizens is $20, as in the following configuration: citizen 0 has $100; citizen 1 has $110; citizen 2 has $120.
1)	
    	
{"NN",
 "NN"}
1
Returns: -1
Since citizens 0 and 1 are not friends, there are no constraints between them.
2)	
    	
{"NNYNNN",
 "NNYNNN",
 "YYNYNN",
 "NNYNYY",
 "NNNYNN",
 "NNNYNN"}
1000
Returns: 3000
3)	
    	
{"NNYN",
 "NNNY",
 "YNNN",
 "NYNN"}
584
Returns: -1
4)	
    	
{"NYNYYYN",
 "YNNYYYN",
 "NNNNYNN",
 "YYNNYYN",
 "YYYYNNN",
 "YYNYNNY",
 "NNNNNYN"}
5
Returns: 20
5)	
    	
{"NYYNNNNYYYYNNNN",
 "YNNNYNNNNNNYYNN",
 "YNNYNYNNNNYNNNN",
 "NNYNNYNNNNNNNNN",
 "NYNNNNYNNYNNNNN",
 "NNYYNNYNNYNNNYN",
 "NNNNYYNNYNNNNNN",
 "YNNNNNNNNNYNNNN",
 "YNNNNNYNNNNNYNN",
 "YNNNYYNNNNNNNNY",
 "YNYNNNNYNNNNNNN",
 "NYNNNNNNNNNNNNY",
 "NYNNNNNNYNNNNYN",
 "NNNNNYNNNNNNYNN",
 "NNNNNNNNNYNYNNN"}
747
Returns: 2988
6)	
    	
{"NY",
 "YN"}
0
Returns: 0
'''
