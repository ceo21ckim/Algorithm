'''
해시 함수란, 임의 크기 데이터를 고정 크기 값으로 매핑하는 데 사용할 수 있는 함수를 말한다.

Design a HashMap without using any built-in hash table libraries.

put(key, value): inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
get(key): returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key): removes the key and its corresponding value if the map contains the mapping for the key.
'''

# solution 1
from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value 
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000 
        self.table = defaultdict(ListNode)

    def put(self, key, value):
        idx = key % self.size 
        if self.table[idx].value is None:
            self.table[idx] = ListNode(key, value)
            return 
    
        p = self.table[idx]
        while p:
            if p.key == key:
                p.value = value 
                return 
            
            if p.next is None:
                break

            p = p.next 
        p.next = ListNode(key, value)
    
    def get(self, key):
        idx = key % self.size 
        if self.table[idx].value is None:
            return -1 
        
        p = self.table[idx]
        while p:
            if p.key == key:
                return p.value 
            
            p = p.next 
        return -1 
    
    def remove(self, key):
        idx = key % self.size 
        if self.table[idx].value is None:
            return 
        
        p = self.table[idx]
        if p.key == key:
            self.table[idx] = ListNode() if p.next is None else p.next 
            return 
    
        prev = p 
        while p:
            if p.key == key:
                prev.next = p.next 
                return 
            
            prev, p = p, p.next 