'''
819. Most Common Word 
Given a string "paragraph" and a string array of the banned words "banned", return the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in "paragraph" are case-insensitive and the answer should be returned in lowercase.
'''

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']

# solution 1
# List comprehension + Counter
from collections import Counter 
import re 
def mostCommonWord(paragraph):
    paragraph = paragraph.lower()
    paragraph = re.sub('[^a-z0-9]', ' ', paragraph)
    sample = paragraph.split()
    for key, _ in Counter(sample).most_common():
        if key in banned:
            pass 
        else:
            return key

mostCommonWord(paragraph)

# solution 2
from collections import Counter 
import re 
def mostcommonWord(paragraph):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split() 
             if word not in banned]
    counts = Counter(words)
    return counts.most_common(1)[0][0]
