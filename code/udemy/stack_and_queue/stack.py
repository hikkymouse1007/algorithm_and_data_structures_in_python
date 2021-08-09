# Stackの基本はLIFO(Last In First Out)
from typing import Any

class Stack(object):
    def __init__(self) -> None:
        self.stack = []
        
    ## 要素の追加
    def push(self, data) -> None:
        self.stack.append(data)
        
        
    ##　要素の削除
    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()
    
if __name__ == '__main__':
    stack = Stack()
    print(stack.stack)
    stack.push(1)
    print(stack.stack)
    stack.push(2)
    print(stack.stack)
    stack.pop()
    print(stack.stack)
    