package TwoPointers;

public class SquaresofaSortedArray {

    public static int[]sortedSquares(int[] nums){

        int left = 0;
        int right = nums.length -1 ;
        int[] result = new int[nums.length];
        int index= nums.length -1;

        while (left < right){
            if (Math.abs(nums[left]) < Math.abs(nums[right])){
                result[index--] = nums[left] * nums[left];
                left++;
            } else {
                result[index--] = nums[right] * nums[right];
                right--;
            }
        }
        return result;

    }
    public static void main(String[] args){

        int[] nums = {-4,-1,0,3,10};
        System.out.println(sortedSquares(nums));
    } 
}

