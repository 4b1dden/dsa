
from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        

#first digit is the vertical level, floating point is the horiz level
root = Node(0)

left_subtree = Node(5.1)
left_subtree.left = Node(15.1)
left_subtree.right = Node(15.2)
left_subtree.left.left = Node(25.1)

right_subtree = Node(8.1)
right_subtree.right = Node(18.1)
right_subtree.left = Node(18.1)
right_subtree.right.right = Node(28.1)

root.left = left_subtree
root.right = right_subtree

def dfs(root: Node):
    if root is None:
        return []

    visited, stack = [], [root]

    while stack:
       curr = stack.pop()
       visited.append(curr)
       print('visited {}'.format(curr.data))
    
       # append right first so we traverse to left first
       if curr.right != None:
           stack.append(curr.right)

       if curr.left != None:
           stack.append(curr.left)

    return visited


def bfs(root: Node):
    if root is None:
        return []

    visited, queue = [], [root]

    while queue:
        # same as dfs, however, instead of popping from the stack, we take the first from the queue
        curr = queue.pop(0)
        visited.append(curr)
        print('visited {}'.format(curr.data))

        if curr.left != None:
            queue.append(curr.left)

        if curr.right != None:
            queue.append(curr.right)

    return visited

dfs_visited = dfs(root)
print('--------------')
bfs_visited = bfs(root)
