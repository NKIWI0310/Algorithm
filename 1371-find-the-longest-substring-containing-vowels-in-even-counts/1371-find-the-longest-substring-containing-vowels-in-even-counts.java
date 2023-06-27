class Solution {
    public int findTheLongestSubstring(String s) {
        char[] key = {1,0,0,0,2,0,0,0,4,0,0,0,0,0,8,0,0,0,0,0,16,0,0,0,0,0};
        
        int mask = 0, result = 0;
        int[] tmp = new int[32];
        
        Arrays.fill(tmp , -1);
        
        for(int i = 0 ; i < s.length(); i++){
            mask ^= key[s.charAt(i)-'a'];
            if(mask != 0 && tmp[mask] == -1){
                tmp[mask] = i;
            }
            result = Math.max(result, i - tmp[mask]);
            
        }
        
        return result;
    }
}