class Solution(object):
    def countOdds(self, low, high):
        count = 0
        if low % 2 == 1 and high % 2 ==1:
            count += 2
            count += (high - 1 - low-1) // 2
        elif low%2 == 1 or high%2 ==1:
            count+=1
            count+=(high - 1 - low)//2
        else:
            count+=(high - low)//2
        return count

        