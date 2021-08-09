"""
Input {'Key1': 'value1', 'key2': [1, 2, 3], 'key3' : (1, 2, 3)} Output True カッコが対になっているか
Input {'Key1': ['value1', 'key2': [1, 2, 3], 'key3' : (1, 2, 3)} Output False
"""

# stringに開いたカッコを見つけたら、stackに閉じカッコを入れる
def validate_format(chars: str) -> bool:
    lookup = {
        '{': '}', 
        '[': ']', 
        '(': ')'
    }
    stack = []
    # 文字列を一文字ずつ確認
    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char]) # keyのvalueをstackに追加
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False
        # print(stack)
                
    if stack: 
        return False
    
    return True
    
if __name__ == '__main__':
    j = "{'Key1': 'value1', 'key2': [1, 2, 3], 'key3' : (1, 2, 3)}"
    print(validate_format(j)) # True
    j = "{'Key1': ['value1', 'key2': [1, 2, 3], 'key3' : (1, 2, 3)}"
    print(validate_format(j)) # False