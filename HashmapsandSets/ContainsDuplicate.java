package HashmapsandSets;
import java.util.HashSet;

public class ContainsDuplicate {
    
    public static boolean containDuplicate(int[] nums){

        HashSet<Integer> elements = new HashSet<>();
        for (int number: nums){
            if (elements.contains(number)){
                return true;
            }
            elements.add(number);
        }
        return false;
    }

    public static void main(String[] args){
        int[] nums = {1,2,3,1};

        System.out.println(containDuplicate(nums));

    }
}
