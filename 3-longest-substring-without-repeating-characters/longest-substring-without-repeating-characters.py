class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ""
        max_str = ""
        if len(s) == 0:
            return 0
        for char in s:
            if char not in curr:
                curr = curr + char
                if len(curr) > len(max_str):
                    max_str = curr
            else:
                curr = curr[curr.index(char)+1:]+char
        return len(max_str)


        #abcabcbb

        '''

        i =  0
        max_length = 0
        seen = set()
        for j in range(len(s)):
            if s[j] in seen:
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i+=1
                i+=1
            else:
                seen.add(s[j])
                max_length = max(max_length,j-i+1)

        return max_length
        '''
        
        