class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
        
        
class BinarySearchTree(object):
    
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value: int) -> None:   
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: int) -> Node:
            if node is None:
                return Node(value) # Nodeオブジェクト生成    
            
            if value < node.value:
                node.left = _insert(node.left, value)
            else: 
                node.right = _insert(node.right, value)
            return node
        print("root", self.root)
        _insert(self.root, value)
        
    def inorder(self) -> None:
        def _inorder(node: Node) -> None:       
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)
        
    def search(self, value: int) -> bool:
        def _search(node: Node, value: int) -> bool:
            if node is None:
                return False
                
            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)
        return _search(self.root, value)

    def min_value(self, node: Node) -> Node:
        current = node 
        while current.lef t is not None:
            current = current.left
        return current
    
    
    def remove(self, value: int) -> None:
        def _remove(node: Node, value: int) -> Node:
            if node is None:
                return node
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                # nodeの枝が片側の場合の処理
                if node.left is None:
                    return node.right # value = 1 の時、node.left = remove(node.left, value)のremoveの戻り値で2を返す
                elif node.right is None:
                    return node.left # rightの枝がない時は,leftの枝のnodeを削除した場所に渡す
                
                # nodeの枝が両側にある場合の処理
                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        _remove(self.root, value)
        
            
        
    
if __name__ == '__main__':
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(10)
    binary_tree.insert(2)
    binary_tree.inorder()
    print(binary_tree.search(8))
    binary_tree.remove(6)
    print("##### Remove")
    binary_tree.inorder()
    