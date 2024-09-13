package StacksandQueues;
import java.util.Stack;

public class ValidParentheses {

    private static Stack<Character> stack = new Stack<>();

    public static boolean isValid(String s){
        if (s.length() % 2 != 0){
            return false;
        } 
        for (char bracket: s.toCharArray()){
            if(bracket == '(' || bracket == '{' || bracket == '['){
               stack.push(bracket);
            } else {
                if (stack.isEmpty()){
                    return false;
                }
                if ((bracket == ')' && stack.pop() != '(' ) || (bracket == '}' && stack.pop() != '{') || (bracket == ']' && stack.pop() != '[')){
                    return false;
                }
            }   
        }
        return (stack.isEmpty());
    }

    public static void main(String[] args){

        String s = "()[]{}";
        System.out.println(isValid(s));
        String s1 = "(]";
        System.out.println(isValid(s1));
        String s2 = "([)]";
        System.out.println(isValid(s2));
        String s3 = "([])";
        System.out.println(isValid(s3));
        // System.out.println(s3);
        // System.out.println(s2.toCharArray());
        // System.out.println(s1.toCharArray());
    }
    
}
