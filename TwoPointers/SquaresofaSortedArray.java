package TwoPointers;

public class SquaresofaSortedArray {

    public static int[]sortedSquares(int[] nums){

        int left = 0;
        int right = nums.length -1 ;
        int[] result = new int[nums.length];
        int index = nums.length -1;

        while (left <= right){
            if (Math.abs(nums[left]) > Math.abs(nums[right])){
                result[index--] = (int) Math.pow(nums[left], 2);
                left++;
                // index--;
            } else {
                result[index--] = nums[right] * nums[right];
                right--;
                // index--;
            }
        }
        return result;

    }
    public static void main(String[] args){

        int[] nums = {-4,-1,0,3,10};
        int[] result = sortedSquares(nums);
        // System.out.println(result.toString());
        for (int i: result){
            System.out.println(i);
        }
    } 
}

