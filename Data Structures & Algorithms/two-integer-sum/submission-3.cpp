class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> comps;

        for (int i = 0; i < nums.size(); i++) {
            int comp = target - nums[i];
            if (comps.contains(comp)) {
                return {comps[comp], i};
            } else {
                comps[nums[i]] = i;
            }
        }
        
    }
};
