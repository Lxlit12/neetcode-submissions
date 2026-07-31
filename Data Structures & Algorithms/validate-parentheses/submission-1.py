class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if top != pairs[char]:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False