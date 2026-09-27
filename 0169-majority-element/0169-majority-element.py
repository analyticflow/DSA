
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        log = len(nums) // 2

        for key, value in count.items():
            if value > log:
                return key
       
               



        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna