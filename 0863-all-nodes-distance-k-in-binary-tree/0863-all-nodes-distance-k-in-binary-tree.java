class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        List<Integer> ans = new ArrayList<>();
        search(root, target, k, ans);
        return ans;
    }

    private int search(TreeNode node, TreeNode target, int k, List<Integer> result) {
        if (node == null)
            return -1;
        if (node == target) {
            collectNodesAtDistanceK(node, k, result);
            return 0;
        }

        int left = search(node.left, target, k, result);
        int right = search(node.right, target, k, result);

        if (left != -1) {
            if (left + 1 == k) {
                result.add(node.val);
            } else {
                collectNodesAtDistanceK(node.right, k - left - 2, result);
            }
            return left + 1;
        } else if (right != -1) {
            if (right + 1 == k) {
                result.add(node.val);
            } else {
                collectNodesAtDistanceK(node.left, k - right - 2, result);
            }
            return right + 1;
        } else {
            return -1;
        }
    }

    private void collectNodesAtDistanceK(TreeNode node, int k, List<Integer> result) {
        if (node == null || k < 0)
            return;
        if (k == 0) {
            result.add(node.val);
        } else {
            collectNodesAtDistanceK(node.left, k - 1, result);
            collectNodesAtDistanceK(node.right, k - 1, result);
        }
    }
}
