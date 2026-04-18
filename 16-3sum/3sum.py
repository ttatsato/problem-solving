class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 値をソートする
        nums.sort()
        n = len(nums)
        #  結果
        res: List[List[int]] = []

        for i in range(n):
            # 一番左の値が0より大きい時、全てを足しても0を超えるので
            if nums[i] > 0:
                break

            # 数が重複している場合はスキップ
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 2ポインタで考える。
            # 3つの値の合計が0なら、2の値の和は -nums[i]になる
            target = -nums[i]

            # 2ポインタで考えていく
            # 添字が全て違うことから　[i, j, ....., k]と考えてく必要がある
            # right は最後の要素
            left = i + 1
            right = n - 1

            while  left < right:
                s = nums[left] + nums[right]
                if s == target:
                    left_val = nums[left]
                    right_val = nums[right]

                    res.append([nums[i], left_val, right_val])
                    # 同じ要素を使った組み合わせは一つだけでいいので、違う値がくるまでスキップする
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return res




