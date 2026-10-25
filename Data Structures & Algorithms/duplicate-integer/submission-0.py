class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCounter = Counter(nums)
        # print(numsCounter)
        for num, count in numsCounter.items():
            if count > 1:
                return True
        return False
        