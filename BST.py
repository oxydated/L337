from dataclasses import dataclass
from collections import deque


@dataclass
class Node:
    value: int
    position: int
    left: 'Node' = None
    right: 'Node' = None


Node.key = lambda self: (self.value, self.position)

Node.posKey = lambda self: (self.position)


@dataclass
class rootBST:
    root: Node = None

    def addChildToRoot(self, value, pos):
        newNode = Node(value, pos)
        if self.root is None:
            self.root = newNode
        else:
            currentNode, nodeToInsert = None, None
            if self.root.key() > newNode.key():
                nodeToInsert = newNode
            else:
                nodeToInsert = self.root
                self.root = newNode

            currentNode = self.root

            while currentNode:
                if currentNode.posKey() > nodeToInsert.posKey():
                    if currentNode.left is None:
                        currentNode.left = nodeToInsert
                        currentNode = None
                        break

                    if currentNode.left.key() < nodeToInsert.key() or \
                        (currentNode.left.key() == nodeToInsert.key() and
                         currentNode.left.posKey() < nodeToInsert.posKey()):

                        nodeReplaced = currentNode.left
                        currentNode.left = nodeToInsert
                        nodeToInsert = nodeReplaced
                    currentNode = currentNode.left

                else:
                    if currentNode.right is None:
                        currentNode.right = nodeToInsert
                        currentNode = None
                        break

                    if currentNode.right.key() < nodeToInsert.key() or \
                        (currentNode.right.key() == nodeToInsert.key() and
                         currentNode.right.posKey() < nodeToInsert.posKey()):

                        nodeReplaced = currentNode.right
                        currentNode.right = nodeToInsert
                        nodeToInsert = nodeReplaced
                    currentNode = currentNode.right


tree = rootBST()

Arr = [1, 1, 3, 2, 4, 1, 2]

for pos, val in enumerate(Arr):
    tree.addChildToRoot(val, pos)
    # print(tree.root)

queue = deque([None]*len(Arr), len(Arr))
queue.clear()


def visitTreeBreadthFirst(aTree: rootBST, func=print):
    queue.append(aTree.root)
    while len(queue) > 0:
        currentNode = queue.popleft()
        func((currentNode.value, currentNode.position))
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)


visitTreeBreadthFirst(tree)


print("\n_____________________\n")


def visitTreeDepthFirst(aTree: rootBST, func=print):
    stack = []
    root = aTree.root
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        currentNode = stack.pop()
        func((currentNode.value, currentNode.position))
        root = currentNode.right


visitTreeDepthFirst(tree)
