class Solution {
    public long minimumReplacement(int[] nums) {
        int n = nums.length;
        int prevElement = nums[n-1];
        long operations = 0;
        
        for (int i = n-2; i >= 0; i--) {
            if (nums[i] <= prevElement) {
                prevElement = nums[i];
                continue;
            }
            
            int divisionTimes = nums[i] / prevElement;
            if (nums[i] % prevElement != 0) {
                divisionTimes++;
            }
            
            operations += divisionTimes - 1;
            prevElement = nums[i] / divisionTimes;
        }
        
        return operations;
    }	
}
