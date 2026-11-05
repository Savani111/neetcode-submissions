class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";

        for (string str: strs) {
            res += std::to_string(str.length()) + "#";
            res += str;
        }

        return res;
    }

    vector<string> decode(string s) {
        int i = 0;
        vector<string> results;
        while (i < s.length()) {
            string string_num = "";
            while (s[i] != '#') {
                string_num += s[i];
                i++;
            }
            i++;
            string result = "";
            
            int end = i + std::stoi(string_num);
            while (i < end) {
                result += s[i];
                i++;
            }
            results.push_back(result);
            
        }

        return results;
    }
};
