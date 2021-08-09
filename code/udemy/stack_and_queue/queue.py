# Stackの基本はFIFO(First In First Out)
from collections import deque # Queueのライブラリ
from typing import Any

class  Queue(object):
    def __init__(self) -> None:
        self.queue = []
        
    ## 要素の追加
    def enqueue(self, data: Any) -> None:
        self.queue.append(data)
        
        
    ##　要素の削除
    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)
    
if __name__ == '__main__':
    # pythonのLibraryにはdequeというものが存在する
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    print(q.pop()) # stackと同じ動きをできる LIFO
    print(q.pop()) # stackと同じ動きをできる
    print(q.pop()) # stackと同じ動きをできる
    print(q.pop()) # stackと同じ動きをできる
    
    # print(q.popleft())
    # print(q.popleft())
    # print(q.popleft())
    # print(q.popleft())
    
    
    # q = Queue()
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)
    # q.enqueue(4)
    # print(q.queue)
    # q.dequeue()
    # print(q.queue)
    
