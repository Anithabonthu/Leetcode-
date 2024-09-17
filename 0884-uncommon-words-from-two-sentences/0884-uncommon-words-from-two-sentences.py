class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        S=s1+s2
        counter=Counter(S)
        return [word for word in counter if counter[word]==1]
        