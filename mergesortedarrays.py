# // Time Complexity : O(n) 
# // Space Complexity : O(1)   
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : No because i attended the class and then did the solution

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        print(p1,p2,p3)
        while p1 >= 0 and p2 >= 0:
            print(p1,p2,p3)
            if nums2[p2] >= nums1[p1]:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p3 -= 1
                p1 -= 1 
        
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1
    
# Approach:
# Same as taught in the class