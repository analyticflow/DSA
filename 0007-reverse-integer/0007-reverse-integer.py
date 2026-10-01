class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = str(x)
            num = -int(s[:0:-1])
        else:
            s = str(x)
            num = int(s[::-1])

        if num < -2147483648 or num > 2147483647:
            return 0

        return num


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna