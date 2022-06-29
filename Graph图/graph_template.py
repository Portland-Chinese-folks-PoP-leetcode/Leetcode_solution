visited = [False for node in graph]
onPath = [False for node in graph]


def traverse(graph, s):  # graph 题目输入的test case的图，s是当前的节点
    if visited[s]:
        return
    # 经过节点 s，标记为已遍历
    visited[s] = True
    # 做选择：标记节点 s 在路径上
    onPath[s] = True
    for node in graph[s]:  # 递归遍历s node所有的neighbour node
        traverse(graph, s)
    # 撤销选择：节点 s 离开路径
    onPath[s] = false


# onPath 数组的操作很像前文 回溯算法核心套路 中做「做选择」和「撤销选择」，区别在于位置：回溯算法的「做选择」和「撤销选择」在 for 循环里面，而对 onPath 数组的操作在 for 循环外面。
