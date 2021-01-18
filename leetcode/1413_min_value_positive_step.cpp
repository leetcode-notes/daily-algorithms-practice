#include <vector>;
using namespace std;

class Solution
{
public:
    int minStartValue(vector<int> &nums)
    {
        int run_min = nums[0];
        int cur = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            cur = cur + nums[i];
            if (cur < run_min)
            {
                run_min = cur;
            }
        }
        if (run_min > 0)
        {
            return 1;
        }
        else
        {
            return -run_min + 1;
        }
    }
};