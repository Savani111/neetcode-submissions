class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int left = 1;
        vector<int> lefts;
        
        for (int num : nums) {
            lefts.push_back(left);
            left *= num;
        }

        int right = 1;
        vector<int> rights(nums.size());

        for (int i = nums.size() - 1; i >= 0; i--) {
            rights[i] = right;
            right *= nums[i];
        }

        vector<int> result;

        for (int i = 0; i < lefts.size(); i++) {
            int val = lefts[i] * rights[i];
            result.push_back(val);
        }

        return result;
    }
};
