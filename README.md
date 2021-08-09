# algorithm_and_data_structures_in_python

バブルソート
https://codezine.jp/article/detail/12243

https://www.youtube.com/watch?v=kQDxmjfkIKY

# 会津オンラインジャッジ

http://judge.u-aizu.ac.jp/onlinejudge/index.jsp?lang=ja

## Udemy

https://www.udemy.com/course/python-algo/learn/lecture/20502342#overview

## LeetCode

https://leetcode.com/

## Recursion
https://www.programiz.com/python-programming/recursion


Example
```
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))
```

Output
```
The factorial of 3 is 6
```

How factorial(x) works when x=3 is given
```
factorial(3)          # 1st call with 3
3 * factorial(2)      # 2nd call with 2
3 * 2 * factorial(1)  # 3rd call with 1
3 * 2 * 1             # return from 3rd call as number=1
3 * 2                 # return from 2nd call
6                     # return from 1st call
```

## Life Cycle of function(x)
![Diagrams](https://cdn.programiz.com/sites/tutorial2program/files/python-factorial-function.png)

## generatorとは
https://qiita.com/keitakurita/items/5a31b902db6adfa45a70

```
簡潔に説明すると、「通常の関数の、return文をyieldに置き換えたもの」ととりあえずは思ってください。（色々と違いますが、とりあえず見逃してください）。
returnの代わりにyieldと書くと、呼び出しただけでは値を返さなくなります。
その代わり、for文などで呼び出して、順々に値を返すようになります。多分例を示したほうがわかりやすいと思います。
```