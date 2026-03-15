#include <string>

using namespace std;

class Solution {
    public:
        string mergeAlternately(string word1, string word2) {
            string result;
            result.reserve(word1.size() + word2.size()); // Reserve space for the result string, and avoid unnecessary reallocations
            int i = 0, j = 0; // Pointers for word1 and word2
            while (i < word1.size() || j < word2.size()) {
                if (i < word1.size()) {
                    result += word1[i];
                    i++;
                }
                if (j < word2.size()) {
                    result += word2[j];
                    j++;
                }
            }
            return result;
        }
};
