"""
1. Input: [11, 2, 5, 9 ,10, 3], 12 => Output: (2, 10) or None

# Listの合計値の半分になる組み合わせを見つける
2. Input: [11, 2, 5, 9 ,10, 3]     => Output: (11, 9) or None ex) 11 + 9 = 2 + 5 + 10 + 3 
"""
from typing import List, Tuple, Optional

def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set() # 空のセットを生成(set([])) setは重複した値を持たない
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)
        
def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    # if sum_numbers % 2 != 0: # 奇数の場合はNone
    #     return 
    
    # half_sum = int(sum_numbers / 2) # Listの合計値の半分を計算
    # ↑ divmod(dividend, divisor)を使う方が楽 return -> Tuple(quotient ,remainder)
    half_sum, remainder = divmod(sum_numbers, 2) # half_sum:商 remainder:余り
    if remainder != 0:
        return
    
    
    cache = set()
    for num in numbers:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num
        
        
if __name__ == '__main__':
    l = [11, 2, 5, 9 ,10, 3]
    t = 12
    print(get_pair(l, t))
    
    l = [11, 2, 5, 9 ,10, 3]
    print(get_pair_half_sum(l))