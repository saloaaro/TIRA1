from collections import namedtuple

Node = namedtuple("Node", ["children"], defaults=[[]])

def count(node):
    if not node.children:
        return 0
    max_children = max(count(child) for child in node.children)
    return max(max_children, len(node.children))

if __name__ == "__main__":
    tree1 = Node([
        Node(),
        Node([Node([Node(), Node()])]),
        Node([Node(), Node()])
    ])

    tree2 = Node([Node([Node(), Node()])])

    print(count(tree1))  # Output: 3
    print(count(tree2))  # Output: 2

