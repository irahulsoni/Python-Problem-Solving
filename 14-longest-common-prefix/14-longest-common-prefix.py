class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
           # Check min length of word in given list
        min_num_char = min([len(word) for word in strs])

        # Create prefix variable for recieve each same character
        prefix = ""
        for idx in range(min_num_char):
            # Filter out if found empty string in given list
            if "" in strs:
                prefix = ""
            else:
                chars = [c[idx] for c in strs]
                if len(set(chars)) == 1:
                    prefix = prefix + chars[0]

                # If found more variance of char then break and return 
                else:
                    break
        return prefix