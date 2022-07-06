class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        integer_length = [1, 2, 3]
        if len(s) < 4:
            return []
        track = []
        res = []

        def backtrack(start, end, track):

            if len(track) == 4:
                if start == end+1:
                    res.append(list(track))
                return
            if start > end:
                return
            for length in integer_length:
                address = s[start:start+length]
                if len(address) > 1 and address[0] == "0":
                    continue
                if 0 <= int(address) <= 255:
                    track.append(address)
                    backtrack(start+length, len(s)-1, track)
                    track.pop(-1)
            return
        backtrack(0, len(s)-1, track)
        print(res)
        answer = []
        for item in res:
            answer.append(".".join(item))
        return answer
