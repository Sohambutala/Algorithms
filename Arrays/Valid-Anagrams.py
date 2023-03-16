class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        arr = [0 for i in range(0,26)]
        index = 0
        while index < len(s):
            arr[ord(s[index])%26] += 1
            arr[ord(t[index])%26] -= 1
            index += 1
        
        for num in arr:
            if num > 0:
                return False

        return True
