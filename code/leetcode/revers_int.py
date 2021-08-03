from typing import List
def reverse(x: int) -> int:
    """
    :type x: int
    :rtype: int
    """

    sign = [1,-1][x < 0]  # xが0より小さければ-1を代入   https://stackoverflow.com/questions/55917667/please-explain-1-1x-0
    rst = sign * int(str(abs(x))[::-1]) # [::-1]:文字列の反転 abs(x): 絶対値
    print(rst, -(2**31)-1 < rst < 2**31)
    return rst if -(2**31)-1 < rst < 2**31 else 0 # 条件の範囲外の桁数がinputされたら0を返す

x = 123
print(reverse(x))

x = -127934
print(reverse(x))

x = 0
print(reverse(x))