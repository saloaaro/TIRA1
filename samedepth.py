from collections import namedtuple

def check(node):
    def get_depth(node):
        if not node.children:
            return 0
        return 1 + max(get_depth(child) for child in node.children)

    depths = set()
    queue = [(node, 0)]

    while queue:
        current, depth = queue.pop(0)

        if not current.children:
            depths.add(depth)
        else:
            queue.extend((child, depth + 1) for child in current.children)

    return len(depths) <= 1

if __name__ == "__main__":
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree1 = Node([
        Node(),
        Node([Node([Node(), Node()])]),
        Node([Node(), Node()])
    ])

    tree2 = Node([Node([Node()]), Node([Node(), Node()])])

    print(check(tree1))  # Output: False
    print(check(tree2))  # Output: True
