class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map={}
        count=0
        for i in arr:
            if i in map:
                map[i]='False'
            else:
                map[i]='True'
        for item in arr:
            if map[item]=='True':
                count+=1
            if count==k:
                return item
        return ""
        