from typing import List, Iterator, Tuple

"""
Synmetric 
Input [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
Output [(5, 3), (7, 4)]
"""

def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = {} # {1 : 2, 3 : 5, 4 :7}
    for pair in pairs:
        first, second = pair[0], pair[1] #{5 : 3}の時はfirst = pair[0] = 5, second = pair[1] = 3
        value = cache.get(second)       # value = 5
        if not value: 
            cache[first] = second
        elif value == first:            # value = 5
            yield pair # for文の中のreturn値を配列として保持していく
            
if __name__ == '__main__':
    l = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    print(find_pair(l)) ## <generator object find_pair at 0x7fcf62358900>
    for r in find_pair(l):
        print(r)