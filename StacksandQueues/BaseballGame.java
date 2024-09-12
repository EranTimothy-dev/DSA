package StacksandQueues;
import java.util.Stack;

public class BaseballGame {


    public static int calPoints(String[] operations){
        Stack<Integer> stack = new Stack<>();
        int scores = 0;
        int temp = 0;
        

        for (int i = 0; i < operations.length; i++){
            if (operations[i].equals("+")){
                temp = stack.indexOf(stack.size() -1) + stack.indexOf(stack.size() -2);
                stack.push(temp);
                scores += temp;
            } else if (operations[i].equals("D")){
                temp = stack.peek() * 2;
                stack.push(temp);
                scores += temp;
            } else if (operations[i].equals("C")){
                int top = stack.pop();
                scores -= top;
            } else {
                temp = Integer.parseInt(operations[i]);
                stack.push(temp);
                scores += temp;
            }
            System.out.println(scores);
        }return scores;
    }

    public static void main(String[] args){
        String[] operations = {"5","-2","4","C","D","9","+","+"};
        System.out.println(calPoints(operations));

    }
    
}
