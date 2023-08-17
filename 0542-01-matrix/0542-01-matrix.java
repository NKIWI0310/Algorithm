class Solution {
    public int[][] updateMatrix(int[][] mat) {

        if (mat == null || mat.length == 0 || mat[0].length == 0)
            return new int[0][0];

        int m = mat.length, n = mat[0].length;

        int[][] result = new int[m][n];
        Queue<int[]> queue = new LinkedList<>();

        // Initialize the result matrix and queue
        for(int i = 0 ; i < m ; i++){
            for(int j = 0 ; j < n ; j++){
                if(mat[i][j] == 0)
                    queue.offer(new int[]{i, j});
                else{
                    result[i][j] = n*m;
                }
            }
        }

        int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int x = cell[0], y = cell[1];

            for (int[] d : dir) {
                int newX = x + d[0];
                int newY = y + d[1];

                if (newX >= 0 && newX < m && newY >= 0 && newY < n) {
                    if (result[newX][newY] > result[x][y] + 1) {
                        queue.offer(new int[]{newX, newY});
                        result[newX][newY] = result[x][y] + 1;
                    }
                }
            }
        }
        return result;
    }
}
