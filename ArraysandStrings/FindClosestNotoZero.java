package ArraysandStrings;

class Main {

    // get the absolute value
    public static float abs(float a){
        return (a <= 0.0F) ? 0.0F-a : a;
    }

    public static int findClosestNumber(int[] nums){
        int closest = nums[0];
        for (int i = 0; i < nums.length; i++){
            if(abs(nums[i]) < abs(closest) || (abs(nums[i]) == abs(closest) && nums[i] > closest)){
                closest = nums[i];
            }
        }
        return closest;
    }


    public static void main(String[] args){

        int[] nums = {-4,-2,1,4,8};
        int closestNumber = findClosestNumber(nums);
        System.out.println(closestNumber);
    }
}