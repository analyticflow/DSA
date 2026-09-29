if __name__ == '__main__':
    scores = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores[name] = score

    unique_grades = sorted(set(scores.values()))
    second_lowest = unique_grades[1]

    result = sorted(name for name, s in scores.items() if s == second_lowest)
    for name in result:
        print(name)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna