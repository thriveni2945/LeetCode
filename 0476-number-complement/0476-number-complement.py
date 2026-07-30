class Solution:
    def findComplement(self, num: int) -> int:
        bits=len(bin(num))-2
        mask=(1<<bits)-1
        return num^mask
        
        