class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int i = 0;

        while (i < 9) {
            std::set<char> foundrow;
            std::set<char> foundcol;
            for (int j = 0; j < 9; j++) {
                char val = board[i][j];
                if (val == '.') {
                    continue;
                }
                
                if (foundrow.contains(val)) {
                    return false;
                } else {
                    foundrow.insert(val);
                }
            }

            for (int j = 0; j < 9; j++) {
                char val = board[j][i];
                if (val == '.') {
                    continue;
                }
                if (foundcol.contains(val)) {
                    return false;
                } else {
                    foundcol.insert(val);
                }
            }
            i++;
        }

        std::map<int, std::set<char>> found;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int val = (j / 3) + 1;
                int val2 = (i / 3) + 1;
                int box = (val * 3) + val2;
                char num = board[i][j];
                if (num == '.') {
                    continue;
                }
    
                if (found[box].contains(num)) {
                    return false;
                } else {
                    found[box].insert(num);
                }
                
            }
        }
        return true;
    }
};
