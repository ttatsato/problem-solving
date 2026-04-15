"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        # 元ノード
        visited = {}

        # Depth-First Search (深さ優先探索)
        def dfs(n):
            # すでにコピー済みなら返す。
            if n in visited:
                return visited[n]

            clone = Node(n.val)
            # ここでvisitedに登録しないと、無限ループになる
            visited[n] = clone

            # neighborsもコピーする。
            for neighbors in n.neighbors:
                clone.neighbors.append(dfs(neighbors))
            return clone

        return dfs(node)
   
