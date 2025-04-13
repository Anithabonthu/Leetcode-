class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number=[]
        for i in s:
            val=str((ord(i)-ord('a'))+1)
            number.append(val)
        number="".join(number)
        print(number)
        for i in range(k):
            Sum=0
            for i in str(number):
                Sum+=int(i)
            number=Sum
        return Sum