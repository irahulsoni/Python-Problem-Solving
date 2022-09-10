class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans, seen = set(), set()
        for i in range(len(s) - 9):
            cur = s[i:i + 10]
            seen.add(cur) if cur not in seen else ans.add(cur)
        return list(ans)
