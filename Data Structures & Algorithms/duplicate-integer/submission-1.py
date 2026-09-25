class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ##duplicate_check = []
        ##for num in nums:
        ##    duplicate_check.append(nums.count(num) > 1)
        ##return True in duplicate_check
        return len(nums) != len(set(nums))

# The solution I added later is so much more elegant. 
