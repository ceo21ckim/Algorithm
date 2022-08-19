'''
49. Group Anagrams 
Given an array of strings "strs", group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# solution 1
from collections import defaultdict
def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

