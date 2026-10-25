class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []

        for num in range(n+1):
            ones = 0
            for i in range(num+1):
                if num>>i & 1:
                    ones+=1

            res.append(ones)

        return res
                    

        