package HashmapsandSets;
import java.util.HashSet;

public class JewelandStones {

    public static int numJewelsInStones(String jewels, String stones){

        // time complexity: O(n + m); where n is amount of stones and m is the amount of jewels
        // space complexity: O(m): where m is the jewels 
        int count = 0;

        HashSet<Character> jewelSet = new HashSet<>();
        for (char j : jewels.toCharArray()){
            jewelSet.add(j);
        }

        for (char stone : stones.toCharArray()){
            if (jewelSet.contains(stone)){
                count++;
            }
        }
        return count;
    }


    public static void main(String[] args){
        String Jewels = "aA";
        String Stones = "aAAbbbb";

        System.out.println(numJewelsInStones(Jewels, Stones));

    }
    
}
