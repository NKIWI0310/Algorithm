class Solution {
    public long countFairPairs(int[] nums, int lower, int upper) {
        Arrays.sort(nums);
        long ans = 0;
        for(int i = 0 ; i < nums.length; i++){
            int lownum = lower - nums[i];
            int highnum = upper - nums[i];
            long low = lowsearch(nums, i+1, lownum);
            long high = highsearch(nums, i+1, highnum);
            ans += high - low;
        }
        return ans;
    }
    
    public long highsearch(int[] nums, int start, int high){
        int end = nums.length;
        while(start < end){
            int mid = (start + end) / 2;
            if(nums[mid] > high){
                end = mid;
            }else{
                start = mid + 1;
            }
        }
        return start;
    }
    
    public long lowsearch(int[] nums, int start, int low){
        int end = nums.length;
        while(start < end){
            int mid = (start + end) /2;
            if(nums[mid] < low){
                start = mid + 1;
            }else{
                end = mid;
            }
        }
            return start;
    }
}