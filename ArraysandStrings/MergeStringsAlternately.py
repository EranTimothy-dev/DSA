class Solution():
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # usage of strings make it an O(n) solution since the whole string is copied when appending another letter to the end
        combined_word = ""
        for i in range(len(max(word2, word1))):
            if i < len(word1):
                combined_word += word1[i]
            if i < len(word2):
                combined_word += word2[i]
        
        return combined_word

    def mergeAlternatelyFixed(self, word1: str , word2: str) -> str:
        # appending to a list is an O(1) operation
        combined_word = []
        A,B = len(word1), len(word2)
        # value for index positions
        a,b = 0,0
        
        word = 1
        # keep appending words until the smallest one is exhausted
        while a < A and b < B:
            if word == 1:
                combined_word.append(word1[a])
                a += 1
                word = 2
            else:
                combined_word.append(word2[b])
                b += 1
                word = 1
        
       # append the rest of the word based on the condition that becomes true
        while a < A:
            combined_word.append(word1[a])
            a += 1
            
        while b < B:
            combined_word.append(word2[b])
            b += 1
            
        return "".join(combined_word) 
        
    def mergeAlternatelyOptimised(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        count = 0
        combined_word = []
        
        while(count < len1 and count < len2):
            combined_word.append(word1[count])
            combined_word.append(word2[count])
            count += 1
        
        if len1 > len2:
            combined_word.append(word1[count:])
        else:
            combined_word.append(word2[count:])
        
        return "".join(combined_word)



if __name__ == "__main__":
    merge = Solution()
    word1 = "abcd"
    word2 = "pq"

    merged_letter = merge.mergeAlternatelyOptimised(word1, word2) 
    print(merged_letter)