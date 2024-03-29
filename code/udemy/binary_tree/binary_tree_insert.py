class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value) # Nodeオブジェクト生成    
    
    print("check node value", node.value, value)
    if value < node.value:
        node.left = insert(node.left, value)
    else: 
        node.right = insert(node.right, value)
    return node
     
def inorder(node: Node) -> None:
    # Inorder Left, Root, Right
    # Preorder Root, Left, Right
    # Postorder Left, Right, Root
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)
        
def search(node: Node, value: int) -> bool:
    if node is Node:
        return False
        
    if node.value == value:
        return True
    elif node.value > value:
        return search(node.left, value)
    elif node.value < value:
        return search(node.right, value)

def min_value(node: Node) -> Node:
    current = node 
    while current.left is not None:
        current = current.left
    return current
    
    
def remove(node: Node, value: int) -> Node:
    if node is None:
        return node
    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:
        # nodeの枝が片側の場合の処理
        if node.left is None:
            return node.right # value = 1 の時、node.left = remove(node.left, value)のremoveの戻り値で2を返す
        elif node.right is None:
            return node.left # rightの枝がない時は,leftの枝のnodeを削除した場所に渡す
        
        # nodeの枝が両側にある場合の処理
        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
    return node
        
            
        
    
if __name__ == '__main__':
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    # print(root.value)
    # print(root.right.value)
    # print(root.right.left.value)
    # print(root.left.value) ## valueはleftがNoneで呼び出すとerror
    # print(inorder(root))
    # print(search(root, 5))
    
    inorder(root)
    print("####### remove")
    root = remove(root, 6)
    inorder(root)
    
    