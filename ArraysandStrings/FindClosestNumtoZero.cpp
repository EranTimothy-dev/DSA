#include <vector>
#include <cmath>
#include <algorithm>

// using namespace std;

class Solution {
    public:
        int findClosestNumber(const std::vector<int>& nums) {
            int closest = nums[0];
            for (int x: nums) {
                if (std::abs(x) < std::abs(closest)) {
                    closest = x;
                }
            }

            // If there are two equally close to zero, return the positive one.
            if (closest < 0 && std::find(nums.begin(), nums.end(), abs(closest)) != nums.end()) {
                return std::abs(closest);
            } else {
                return closest;
            }
        }
};
