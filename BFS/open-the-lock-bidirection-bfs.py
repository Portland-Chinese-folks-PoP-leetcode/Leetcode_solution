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
        q1 = set()
        q2 = set()
        visited = set()
        step = 0
        q1.add('0000')
        q2.add(target)
        while len(q1) > 0 and len(q2) > 0:
            temp = set()
            for cur in q1:
                if cur in dead:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)
                for j in range(4):
                    up = plusOne(cur, j)
                    if up not in visited:
                        temp.add(up)
                    down = minusOne(cur, j)
                    if down not in visited:
                        temp.add(down)
            step += 1
            q1 = q2
            q2 = temp
        return -1
