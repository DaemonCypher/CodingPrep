package TwoSums;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int arr[]={0,0};
        int length = nums.length;
        for(int i = 0; i< length; i++)
        {
            for(int j=i+1;j<length; j++)           
            {
                if (  nums[i]+nums[j] == target)
                {
                    arr[0]=i;
                    arr[1]=j;
                }
            }

        }
        return arr;
    }
}