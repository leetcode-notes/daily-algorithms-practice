'''
Problem Statement for AlienOccupation


Problem Statement

There are N planets in the galaxy. The planets are numbered from 0 to N-1. Planet number A is the home planet of an aggressive alien race.

The alien race has decided to occupy as much of the galaxy as they can. The occupation will happen according to a pre-determined plan. The great shaman of the alien race has determined the data for the plan: two equally long int[]s X and Y.

The occupation will consist of zero or more years. In each year, the aliens will attack and occupy all planets that can be safely attacked from the planets they already control. The arrays X and Y are used to determine which planets can be safely attacked from where, as follows: If the aliens already control some planet p, they can use it as a home base from which they can safely attack each planet of the form(X[i] * p + Y[i]) modulo N.

Determine three numbers:

T = the total number of planets this alien race will eventually control
U = the number of years the occupation process will take
V = the maximum number of new planets occupied in some year
Return the int[] {T, U, V}.


Definition

Class:	AlienOccupation
Method:	getInfo
Parameters:	int, int, int[], int[]
Returns:	int[]
Method signature:	int[] getInfo(int N, int A, int[] X, int[] Y)
(be sure your method is public)


Notes
-	If no planets ever get occupied(see Example  # 2), V should be zero.

Constraints
- N will be between 1 and 1, 000, 000, inclusive.
- A will be between 0 and N-1, inclusive.
- X will have between 1 and 10 elements, inclusive.
- Y will have the same number of elements as X.
- Each element of X and Y will be between 0 and N-1, inclusive.

Examples
0)

7
4
{1}
{1}
Returns: {7, 6, 1}
There are 7 planets, the alien race starts on planet 4. There is only one rule: if you control some planet p, you can safely occupy planet(1*p + 1) modulo 7. The occupation will take six years. In those years, the aliens will occupy one planet each year, in the order 5, 6, 0, 1, 2, 3. In the end all planets will be occupied.
1)

100
47
{2, 14, 14}
{10, 2, 4}
Returns: {51, 5, 20}
In the end, planet 47 and all even-numbered planets will be occupied. The aliens will occupy three planets during the first year(these are planets 4, 60, and 62), 8 planets during the second year, 20 planets during the third year, 16 planets during the fourth year, and three planets during the last, fifth year of the campaign.
2)

100
47
{1, 11}
{0, 30}
Returns: {1, 0, 0}
Both formulas tell us the same thing: if we control planet 47, it is safe to occupy planet 47. Thus, there will be no occupation at all.
3)

123456
0
{3, 4, 55555}
{6, 7, 88888}
Returns: {123456, 20, 18004}
Watch out for integer overflow when computing the values(X[i] * p + Y[i]).
4)

230
23
{2, 2}
{0, 0}
Returns: {5, 4, 1}
The two rules these aliens have are identical. So, they will only occupy one planet each year.
'''
