class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for item in nums:
            if item in count:
                return True
            else:
                count[item]=1
        return False