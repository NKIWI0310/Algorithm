class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < mat.length; i++) {
            int count = 0;
            for(int j = 0; j < mat[i].length && mat[i][j] == 1; j++) {
                count++;
            }
            map.put(i, count);
        }
        
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());
        
        list.sort((a, b) -> {
            if (a.getValue().equals(b.getValue())) {
                return a.getKey().compareTo(b.getKey());
            }
            return a.getValue().compareTo(b.getValue());
        });
        
        
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = list.get(i).getKey();
        }
        
        return result;
    }
}
