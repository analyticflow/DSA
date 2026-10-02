# n = int(input())                    # number of elements
# t = tuple(map(int, input().split())) # create tuple
# print(hash(t))                      # get tuple's hash



n = int(input())
t = tuple(map(int, input().split()))

x = 0x345678
mult = 1000003
length = len(t)

for item in t:
    x = (x ^ hash(item)) * mult
    length -= 1
    mult += 82520 + 2 * length

x += 97531
x &= (1 << 64) - 1

if x >= (1 << 63):
    x -= (1 << 64)

print(x)





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna