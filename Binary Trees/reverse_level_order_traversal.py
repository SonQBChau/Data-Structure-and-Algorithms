from queue import Queue
from stack import Stack
from binary_tree import BinaryTree, Node

def reverse_levelorder_print(start):
    if start is None:
        return

    queue = Queue()
    stack = Stack()
    queue.enqueue(start)

    traversal = ""
    while len(queue) > 0:
        node = queue.dequeue()

        stack.push(node)

        if node.right:
            queue.enqueue(node.right)
        if node.left:
            queue.enqueue(node.left)
    
    while len(stack) > 0:
        node = stack.pop()
        traversal += str(node.value) + '-'

    return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(reverse_levelorder_print(tree.root))