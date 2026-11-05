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
        
        for (int i = nums.size() - 1; i >= 0; i--) {
            lefts[i] *= right;
            right *= nums[i];
        }


        return lefts;
    }
};
