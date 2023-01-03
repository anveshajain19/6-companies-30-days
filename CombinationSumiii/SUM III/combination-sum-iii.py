class Solution:
        def combinationSum3(self, k: int, n: int) -> list[list[int]]:
            res = []
            if k > n:
                return res
            def f(i, total, cur):
                if len(cur) == k and total == n:
                    res.append(cur[:])
                    return
                if len(cur) == k:
                    return
                for j in range(i, 10):
                    f(j + 1, total + j, cur + [j])
            f(1, 0, [])
            return res