# Find Palindrome
# ---------------
# Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).
# Example Input: 'racecar'
# Example Output: True

def palindrome():
    test = "racecar"
    backtest = test[-1::-1]
    print(test)
    print(backtest)
    if test == backtest:
        print(True)
    else:
        print(False)
    test2 = "bobby"
    backtest2 = test2[-1::-1]
    print(test2)
    print(backtest2)
    if test2 == backtest:
        print(True)
    else:
        print(False)


palindrome()
