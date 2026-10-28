class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::map<char, int> sbreak;

        for (char c : s) {
            sbreak[c]++;
        }

        for (char c : t) {
            if (sbreak[c] <= 0) {
                return false;
            } else {
                sbreak[c]--;
            }
        }
        return true;
    }
};
