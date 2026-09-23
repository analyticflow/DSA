class Solution:
    def isPalindrome(self, s: str) -> bool:
        space = ""
        for c in s:
            if c.isalnum():
                space += c.lower()
        return space == space[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna