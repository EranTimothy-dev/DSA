package StacksandQueues;
import java.util.ArrayList;

public class BaseballGame {


    public static int calPoints(String[] operations){
        ArrayList<Integer> stack = new ArrayList<>();
        // int[] stack = new int[operations.length];
        int scores = 0;
        int temp = 0;

        for (int i = 0; i < operations.length-1; i++){
            if (operations[i].equals("+")){
                temp = stack.indexOf(-1) + stack.indexOf(-2);
                stack.add(temp);
                scores += temp;
            } else if (operations[i].equals("D")){
                temp = stack.indexOf(-1) * 2;
                stack.add(temp);
                scores += temp;
            } else if (operations[i].equals("C")){
                scores -= stack.indexOf(-1);
                stack.remove(i);
            } else {
                temp = Integer.parseInt(operations[i]);
                stack.add(temp);
                scores += temp;
            }
        }
        return scores;
    }

    public static void main(String[] args){
        String[] operations = {"5","-2","4","C","D","9","+","+"};
        System.out.println(calPoints(operations));

    }
    
}
