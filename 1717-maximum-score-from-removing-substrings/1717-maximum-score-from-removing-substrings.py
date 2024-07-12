class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans=0
        if y>x:
            top="ba"
            top_score=y
            bottom="ab"
            bottom_score=x
        else:
            top="ab"
            top_score=x
            bottom="ba"
            bottom_score=y
        stack=[]
        for char in s:
            if char==top[1] and stack and stack[-1]==top[0]:
                ans+=top_score
                stack.pop()
            else:
                stack.append(char)
        newstack=[]
        for char in stack:
            if char==bottom[1] and newstack and newstack[-1]==bottom[0]:
                ans+=bottom_score
                newstack.pop()
            else:
                newstack.append(char)

        return(ans)

        