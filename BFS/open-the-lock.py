# it's easy, and easy to use structure framework
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusOne(s: str, j: int):
            ch = list(s)
            if ch[j] == '9':
                ch[j] = '0'
            else:
                ch[j] = str(int(ch[j])+1)
            new_string = ''.join(map(str, ch))
            return new_string

        def minusOne(s: str, j: int):
            ch = list(s)
            if ch[j] == '0':
                ch[j] = '9'
            else:
                ch[j] = str(int(ch[j])-1)
            new_string = ''.join(map(str, ch))
            return new_string

        dead = set()
        for i in deadends:
            dead.add(i)
        q = []
        visited = set()
        step = 0
        q.append('0000')
        visited.add('0000')
        while len(q) > 0:
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                if cur in dead:
                    continue
                if cur == target:
                    return step
                for j in range(4):
                    up = plusOne(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = minusOne(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            step += 1
        return -1
