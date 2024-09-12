class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        allowed=set(allowed)
        for word in words:
            if all(w in allowed for w in word):
                count+=1
        return count
        