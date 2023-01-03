class Solution(object):
    def evalRPN(self, tokens):
        ans = []
        for t in tokens:
            if t not in "+-*/":
                ans.append(int(t))
            else:
                r, l = ans.pop(), ans.pop()
                if t == "+":ans.append(l+r)
                elif t == "-":ans.append(l-r)
                elif t == "*":ans.append(l*r)
                else:ans.append(int(l/r))
        return ans.pop()