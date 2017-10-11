"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).
Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
------------------------------------------------Approach-----------------------------------------------
BFS
1. deque.popleft() is faster than list.pop(0),
because the deque has been optimized to do popleft() approximately in O(1), while list.pop(0) takes O(n)
2. deque: list-like container with fast appends and pops on either end
3. When the parentheses string is valid, num('(') == num(')'),
                                       ()())
first level                )())    (())   ()))   ()()  ()()    since the last two are duplicated, so we need visited in the code to record
second level

if a substring in first level is valid, then there cannot be valid substring in second level.
first level valid means for example: num('(') + 1 = num(')') in original string
so first level num('(') == num(')')-1, second level num('(')-1 < num(')')-1 or num('(') > num('(') - 2
so if there is one substring in first level is valid, i will set done to true, so the tree won't extend to third level from second level, since we are
supposed to remove minimum number of invalid parentheses
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isValid(s):
            cp = 0
            # when char < 0, which means num('(') < num(')'), the substring is already invalid
            for char in s:
                if cp < 0:
                    return False
                cp += {'(': 1, ')': -1}.get(char, 0)
            #since we already exclude cp < 0 case, if cp > 0, num('(') > num(')'), which is invalid
            return cp == 0

        visited = set([s])
        queue = collections.deque([s])
        ans = []
        done = False

        while queue:
            string = queue.popleft()
            if isValid(string):
                done = True
                ans.append(string)

            if done:
                continue
            for x in range(len(string)):
                if string[i] not in ('(', ')'):
                    continue
                kidStr = string[:x] + string[x+1:]
                if kidStr not in visited:
                    #set should use add not append
                    visited.add(kidStr)
                    queue.append(kidStr)
        return ans
