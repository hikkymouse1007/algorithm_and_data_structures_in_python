# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_D
# O(n**2)のプログラムを書かないように注意

n=int(input())
R=[int(input()) for _ in range(n)]

# dp的な考え方？
# 各時刻における損益の最大値は、前の時刻における損益の最大値と現時刻の最小値から計算可能
# 最小値にぶち当たるたびに、そこにひっつきながら収益がもっと上がるか見張る感じ
r_min = R[0]
ans = -10**9  
for r in R[1:]:
    ans = max(ans, r-r_min)
    r_min = min(r, r_min)

print(ans)