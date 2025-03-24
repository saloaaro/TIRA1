from collections import namedtuple

Node = namedtuple("Node", ["children"], defaults=[[]])

def check(node):
    if not node.children:
        return True
    elif len(node.children) > 1:
        return False
    else:
        return all(check(child) for child in node.children)

if __name__ == "__main__":
    tree1 = Node([
        Node(),
        Node([Node([Node(), Node()])]),
        Node([Node(), Node()])
    ])

    tree2 = Node([Node([Node([Node()])])])

    print(check(tree1))  # Output: False
    print(check(tree2))  # Output: True
