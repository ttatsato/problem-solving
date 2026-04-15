class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # 文字列が渡される。
        # その文字列の中に、連続した文字列で回文になる組み合わせは何個あるか
        # 1文字の場合も回文とする。

        # 中央拡張法を使う(Center Expansion)
        def expand(s, left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # 回文の数をカウントする
                count +=1
                # この範囲は回文なので次の組み合わせをみる
                left -=1
                right +=1


        for i in range(len(s)):
            # 奇数長
            expand(s, i, i)
            # 偶数長
            expand(s,i,i+1)


        return count
