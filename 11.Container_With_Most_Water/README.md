# 11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.


## 問題の概要
高さの配列 height が与えられる。各要素は垂直な壁の高さを表す。
2本の壁を選んで作られる「容器」に入る水の量を最大化せよ。


## Examples
Input: height = [1,8,6,2,5,4,8,3,7]  
Output: 49  
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.  


Input: height = [1,1]  
Output: 1


# ダメな解答例
ブルーフォースで解いてみる。  
Time Limit Exceeded になる。

```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_water = max(max_water, min(height[i], height[j]) * (j - i))
        return max_water

```

# 考え方
- まず求めるのは2次元
- 総当たりじゃない
- ポインタを指定して体積を算出する
- 高さの値が大きい組み合わせがより体積を大きくする

→ Two Pointerで解く
縮小型がいいと思う



