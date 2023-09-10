class Solution:
    def isValid(self, s: str) -> bool:
        opened_brackets = []
        openers = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for i, char in enumerate(s):
            if char in '([{':
                opened_brackets.append(char)
            else:
                if self.last(opened_brackets) == openers[char]:
                    opened_brackets.pop()
                else:
                    # last opened bracket doesn't match the one we're closing
                    return False
        return len(opened_brackets) == 0


    # return last element of list, None if empty
    def last(self, li):
        return li[-1] if len(li) > 0 else None