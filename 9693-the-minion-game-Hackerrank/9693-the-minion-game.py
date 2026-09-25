def minion_game(string):
    
    stuart = 0
    kevin = 0    
    
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            kevin += len(string) - i
        else:
            stuart += len(string) - i
            
    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna