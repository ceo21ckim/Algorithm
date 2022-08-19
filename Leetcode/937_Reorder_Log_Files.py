'''
937. Reorder Data in Log Files 
You are given an array of "logs". Each log is a space-delimited string of words, where the first word is the identifier.
There are two type of logs:
    - Letter-logs: All words (except the identifier) consist of lowercase English letters.
    - Digit-logs: All words (except the identifier) consist of digits.

Recorder these logs so that:
    1. The letter-logs come before all digit-logs.
    2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort tehm lexicographically by their identifiers.
    3. The digit-logs maintain their relative ordering.
'''

logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']


# solution 1
# Use lambda + sort operator
def reorderLogFiles(logs):
    digits, letters = [], []
    for logits in logs:
        if logits.split()[1].isdigit():
            digits.append(logits)
        else:
            letters.append(logits)

    letters.sort(key = lambda x: (x.split()[1], x.split()[0]))
    return letters + digits


# solution 2

def func(x):
    return x.split()[1], x.split()[0]

logs.sort(key = func)
