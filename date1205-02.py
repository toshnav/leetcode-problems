# 501. Find Mode in Binary Search Tree
# Easy

# Add to List
# Share
# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

# Follow up: Could you do that without using any extra space?
# (Assume that the implicit stack space incurred due to recursion does not count).
# --------------------------------------------------------------------------------------------------------------------------

# Solution 
def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashmap={}
        def inorder(root):
            if(root):
                inorder(root.left)
                if(root.val not in hashmap):
                    hashmap[root.val]=0
                hashmap[root.val]+=1
                inorder(root.right)
        inorder(root)
        maxvalue=1
        arr=[]
        value=root.val
        for i in hashmap:
            maxvalue=max(maxvalue,hashmap[i])
        for i in hashmap:
            if(hashmap[i]==maxvalue):
                arr.append(i)
        return arr
# my Solution :
 def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        k =[]
        def treeTraversal(root):
            if root :
                treeTraversal(root.left)
                k.append(root.val)
                treeTraversal(root.right)
        treeTraversal(root)
        j=[]
        for i in k :
            r = k.count(i)
            j.append(r) 
        l = max(j)
        res=[]
        for o in k :
            if k.count(o) == l :
                res.append(o)
        return set(res)