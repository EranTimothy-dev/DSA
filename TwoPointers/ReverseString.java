package TwoPointers;

public class ReverseString {
    
    public static void reverseString(char[] s){
        int left = 0;
        int right = s.length - 1;
        char temp;

        while(left<right){
            temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }

    public static void main(String[] args){

        char[] s = {'h','e','l','l','o'};
        reverseString(s);
        for ( char c : s){
            System.out.println(c);
        }
    }
    
}
