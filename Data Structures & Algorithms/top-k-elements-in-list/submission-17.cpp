class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> breakdown;

        for (int num : nums) {
            breakdown[num]++;
        }

        std::vector<std::vector<int>> bucket(nums.size() + 1);
        for (auto& [key, value] : breakdown) {
            bucket[value].push_back(key);
        }

        std::vector<int> res;
        for (int i = nums.size(); i >= 0 && res.size() < k; i--) {
            for (int num : bucket[i]) {
                res.push_back(num);
            }

            if (res.size() == k) {
                break;
            }
        } 

        return res;
    }
};
