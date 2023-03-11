# Queue
'''
시퀀스의 한쪽 끝에는 엔티티를 추가하고, 다른 반대쪽 끝에는 제거할 수 있는 엔티티 컬렉션이다.
FIFO(First-In-First-Out) 선입선출로 처리되는, 줄을 서는 것에 비유할 수 있음.
너비 우선 탐색(Breadth-First Search, BFS)이나 캐시 등을 구현할 때 널리 사용된다.

push(x): 요소 x를 스택에 삽입한다.
pop(): 스택의 첫 번째 요소를 삭제한다.
top(): 스택의 첫 번째 요소를 가져온다.
empty(): 스택이 비어 있는지 여부를 리턴한다.
'''

import collections 

class Stack(object):
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
        '''
        self.q.insert(0, x)
        '''
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0 