class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = 0
        listt = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[j] < nums[i]):
                    counts = counts + 1
            listt.append(counts)
            counts= 0
        return listt
                