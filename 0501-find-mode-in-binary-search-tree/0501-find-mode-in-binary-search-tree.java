/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    private int maxcount = 0;

    public int[] findMode(TreeNode root) {
        Map<Integer, Integer> counts = new HashMap<>();
        List<Integer> ans = new ArrayList<>();
        maxcount = 0;
        DFS(root, counts, ans);

        int[] results = new int[ans.size()];

        for(int i = 0 ; i < ans.size(); i++){
            results[i] = ans.get(i);
        }
        return results;

    }

    public void DFS(TreeNode node, Map<Integer, Integer> counts, List<Integer> ans ){
        if(node == null){
            return;
        }

        DFS(node.left, counts, ans);

        int count = counts.getOrDefault(node.val, 0) + 1;
        counts.put(node.val, count);

        if(count > maxcount){
            maxcount = count;
            ans.clear();
            ans.add(node.val);
        }else if(count == maxcount){
            ans.add(node.val);
        }

        DFS(node.right, counts, ans);
        
    }
}