# ref: #  https://www.youtube.com/watch?v=-5z9dimxxmI

class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        
        for i in range (0,32):
            output = output << 1
            
            if n & 1 == 1:
                output += 1 
            
            n = n >> 1
        return output


        class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

 