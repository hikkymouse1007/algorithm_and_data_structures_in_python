import hashlib

class HashTable(object):
    
    def __init__(self, size=10) -> None:
        self.size = size
        """
        「for _ in range(4)」は「
        for i in range(4)」のように書いてもOKです。 
        変数名が「_」になっているだけです。
        変数名を「_」にすることによって、
        「その変数を使っていません」ということを
        表現しています（Pythonの習慣です）。
        """
        # rangeの回数だけ[]を[]の中に作成
        self.table = [[] for _ in range(self.size)]
        
        """
        hash tableについて:https://wa3.i-3-i.info/word11947.html
        ```
        補足として、ハッシュ関数さんは、とても真面目なやつです。
        同じ名前を入れると必ず同じ数字を返してくれます。
        そのため「愛媛みかん」は必ず「3」になります。
        「4」になったり「10」になったりはしません。
        「3」です。
        ```
        """
    def hash(self, key) -> int:
        return  int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size #　keyを16進数のhashに変換し, int型になおす, sizeでわってindexの数字を生成
        
    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]: #tableの特定のindexに格納しているデータを取得
            # 既存のデータは二重に追加しない
            if data[0] == key:  # dataのkeyが既存だった場合
                data[1] = value # 同じvalueで上書き
                break
        else: # table[index]が空の場合の処理
            self.table[index].append([key, value])
            
    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ')
            for data in self.table[index]:
                print('-->', end=(''))
                print(data, end=(''))
    
    from typing import Any
    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
                
if __name__ == '__main__':
    hash_table = HashTable()
    # print(hash_table.table) # [[], [], [], [], [], [], [], [], [], []]
    # print(hashlib.md5("car".encode()).hexdigest()) # e6d96502596d7e7887b76646c5f615d9
    # print(int(hashlib.md5("car".encode()).hexdigest(), base=16)) # 306851216158335538240511469114392712665
    print(hash_table.hash('car')) # 5
    hash_table.add('car', 'Tesla') 
    hash_table.add('car', 'Tesla') 
    hash_table.add('car', 'Toyota') 
    hash_table.add('pc', 'Mac') 
    hash_table.add('sns', 'Youtube') 
    hash_table.print()
    print(hash_table.table) # [[], [], [], [], [['pc', 'Mac'], ['sns', 'Youtube']], [['car', 'Toyota']], [], [], [], []]
    print(hash_table.get('sns'))
    