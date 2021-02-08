# 問題
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_D


# 制約
# 2 =< n =< 200,000 (Rangeの上限設定はpythonは動的なので不要)
# 1 =< Rt =< 10**9
n=int(input())
R=[int(input()) for _ in range(n)]

min_price = R[0] # 初期時価 
max_profit = -10**9  # 初期時価 R[0]が最大価格スタート = 初期最小損益(0yen - 10**9)とした場合　#実際はこれより1以上大きい最大損益しかあり得ない(1 - 10**9 以上)

for price in R[1:]:
    max_profit = max(max_profit, price - min_price)
    print("current_max_profit: ${s}", max_profit)
    min_price = min(price, min_price)
    print("current_min_price: ${s}", min_price)

print(max_profit)