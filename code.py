class Solution:
    def maximum69Number (self, num: int) -> int:
        f=list(str(num))
        n=len(f)
        for i in range(n):
            if  f[i]=='6':
                f[i]='9'
                break
        return int(''.join(f))
        
        
