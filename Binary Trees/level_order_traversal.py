from queue import Queue
from binary_tree import BinaryTree, Node

def levelorder_print(start):
    if start is None:
        return 

    queue = Queue()
    queue.enqueue(start)

    traversal = ""
    while len(queue) > 0:
        traversal += str(queue.peek()) + "-"
        node = queue.dequeue()

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(levelorder_print(tree.root))