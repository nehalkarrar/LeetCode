'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = {}
        for x in nums1:
            freq1[x] = freq1.get(x,0) + 1
        
        freq2 = {}
        for x in nums2:
            freq2[x] = freq2.get(x,0) + 1
        
        res = []
            
        for num in freq1.keys():
            if num in freq2.keys():
                for i in range(min(freq1[num],freq2[num])):
                    res.append(num)
        return res
        