#include <iostream>

#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Solution
{
public:
    int numIdenticalPairs(vector<int> &nums)
    {
        int ans = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (nums[i] == nums[j])
                {
                    ans++;
                }
            }
        }
        return ans;
    }
};

// Success
// Details
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of Good Pairs.
// Memory Usage: 7.2 MB, less than 99.40% of C++ online submissions for Number of Good Pairs.
// Next challenges:
// Maximum Size Subarray Sum Equals k
// Minimize Rounding Error to Meet Target
// Angle Between Hands of a Clock