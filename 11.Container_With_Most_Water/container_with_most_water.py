# 模範解答: 双方向ポインタ 縮小法
# 29.77MB Beats19.58%
# Runtime 59ms | Beats 52.14%

class Solution:
     def maxArea(self, height: List[int]) -> int:
            max_water = 0
            left = 0
            right = len(height) - 1
            
            # ポインタの位置は常にleft が rightよりも右側にくること
            while left < right:
                #  低い方の高さ * 底辺の長さ
                water = min(height[left], height[right]) * (right - left)
                max_water = max(max_water, water)
    
                # より良い条件を探すためにそれぞれの高さを比較
                if height[left] < height[right]:
                    left += 1
                else:
                    right -=1
            
            return max_water



# より早く双方向ポインタ 縮小法 + 現在の高さと比較させる
# 29.76MB Beats19.58%
# Runtime 13ms | Beats 99.15%
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:

            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)

            if height[left] < height[right]:
                curr = height[left]
                while left < right and height[left] <= curr:
                    left += 1
            else:
                curr = height[right]
                while left < right and height[right] <= curr:
                    right -= 1

        return max_water
