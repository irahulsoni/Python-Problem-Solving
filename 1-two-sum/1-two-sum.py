class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0 , len(nums)): #using for loop to check every element in list
            for j in range(i + 1, len(nums)): # next element on the list
                if nums[j] + nums[i]== target: # c = a + b or b = c - a
                    return [i,j]