if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    score_list = list(arr)
    score_set = set(score_list)
    s_list = sorted(list(score_set))
    rev_list = s_list[::-1]
    print(rev_list[1])


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna