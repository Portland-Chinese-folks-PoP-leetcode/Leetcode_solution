/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    int maxdiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        traverse(root);
        return maxdiameter;
    }

    private int traverse(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftDepth = traverse(root.left);
        int rightDepth = traverse(root.right);
        // Utilize the post order traversal to calculate the diameter

        int curNodeDiameter = leftDepth + rightDepth;
        maxdiameter = Math.max(maxdiameter, curNodeDiameter);
        return Math.max(leftDepth, rightDepth) + 1;
    }
}