from __future__ import annotations
from typing import Any


class Node(object):
    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.next = next_node
        
class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head
        
    # 先頭のnodeの右にnodeを追加
    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None: ## 最初のデータを入れて、headのnodeを作成
            self.head = new_node
            return 
        
        last_node = self.head
        while last_node.next: #last_nodeがNoneになるまでloop
            last_node = last_node.next
        last_node.next = new_node
        
    # headのnodeの左にnodeを追加
    def insert(self, data: Any) -> None:
        new_node= Node(data)
        new_node.next = self.head # headのnodeを右にずらす
        self.head = new_node # headに新しいnodeをinsert
        
    # 全てのnodeをprintする
    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    # headのnodeを削除する場合
    def remove(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
            
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            return 
            
        previous_node.next = current_node.next # 左からnodeをa, b, cとした時、 bを消してaとcをリンクさせる
        current_node = None
        
        
        
        
        
if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    # l.insert(0)
    # print(l.head.data) # headのNodeクラスのdataにアクセス
    # print(l.head.next.data)
    # print(l.head.next.next.data)
    # print(l.head.next.next.next.data)
    l.print()
    l.insert(0)
    print("### insert 0")
    l.print()
    
    l.remove(2)
    print("### remove 2")
    l.print()