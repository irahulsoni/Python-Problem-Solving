class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        for p in range(len(nums)):
            if nums[p] != nums[current]:
                current +=1
                nums[current] = nums[p]
        return current+1
    
            