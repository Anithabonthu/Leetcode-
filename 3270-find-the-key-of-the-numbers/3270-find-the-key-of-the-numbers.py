class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1=str(num1)
        num2=str(num2)
        num3=str(num3)
        n1=len(num1)
        n2=len(num2)
        n3=len(num3)
        if n1<4:
            num1=(4-n1)*'0'+num1
        if n2<4:
            num2=(4-n2)*'0'+num2
        if n3<4:
            num3=(4-n3)*'0'+num3
        ans=""
        for i in range(4):
            ans = ans + min(num1[i],num2[i],num3[i])
        return(int(ans))

        