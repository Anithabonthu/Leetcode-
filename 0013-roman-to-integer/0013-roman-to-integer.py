class Solution:
    def romanToInt(self, s: str) -> int:
        map={'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        count=0
        for st in range(len(s)):
            if st<len(s)-1 and map[s[st]] < map[s[st+1]]:
                count = count-map[s[st]]
            else:
                count=count+map[s[st]]
        return count
            
        