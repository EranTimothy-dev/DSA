package ArraysandStrings;

public class MergeStringsAlternately {
    
    public static String mergeString(String word1, String word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        int count = 0;
        String combinedString = "";
        // use ternary operator to find the shorter word
        for(int i = 0; i < (len1 < len2 ? len1 : len2); i++) {
            // use concatenation to combine the words
            combinedString += word1.charAt(i);
            combinedString += word2.charAt(i);
            count += 1;
        }
        
        if (len1 < len2){
            for(int i =count; i < len2; i++){
                combinedString += word2.charAt(i);
            }
        } else {
            for(int i =count; i < len1; i++){
                combinedString += word1.charAt(i);
            }
        }

        return combinedString;
    }
    
    public static void main(String[] args) {
        String word1 = "abcd";
        String word2 = "pqr";
        System.out.println(mergeString(word1, word2));
    }
}
