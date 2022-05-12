# 88. Merge Sorted Array
# Easy

# 4536

# 440

# Add to List

# Share
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        total_len = m+n-1
       
        m -= 1 #m = m-1
        n -= 1 #n = n-1
       
        while m >=0 and n >=0:
           
            if nums1[m] > nums2[n]:
               
                nums1[total_len] = nums1[m]
                m-=1
                total_len -= 1
               
            else:
               
                nums1[total_len] = nums2[n]
                n-=1
                total_len-=1
               
        while n >= 0: #Check second array has still pending
            nums1[total_len] = nums2[n]
            n-=1
            total_len-=1
