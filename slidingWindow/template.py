def slidingWindow(s, t):
    need = dict()
    window = dict()
    for c in t:
        if c in t:
            need[c] += 1
        else:
            need[c] = 1
    left, right, valid = 0, 0, 0
    while right < len(s):
        # c是将要被一如窗口的字符
        c = s[right]
        right += 1
        # 接下来进行窗口内数据的一系列更新

        """debug 输出的位置
        print(left,right)
        """
        # 判断左侧窗口是否要收缩
        while(window needs shrink):
            d = s[left]
            left += 1
            # ....
