class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        cleaned_str = "".join(filtered_chars)
        return cleaned_str == cleaned_str[::-1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna