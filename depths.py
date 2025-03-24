class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_nodes(node, depth):
    if depth == 0:
        return 1

    x = 0
    for y in node.children:
        x += count_nodes(y, depth - 1)
    return x

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])

    print(count_nodes(tree1, 0)) # 1
    print(count_nodes(tree1, 1)) # 3
    print(count_nodes(tree1, 2)) # 3
    print(count_nodes(tree1, 3)) # 0

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])

    print(count_nodes(tree2, 0)) # 1
    print(count_nodes(tree2, 1)) # 1
    print(count_nodes(tree2, 2)) # 1
    print(count_nodes(tree2, 3)) # 1
    print(count_nodes(tree2, 4)) # 0

    tree3 = Node(1, [Node(2), Node(3), Node(4)])

    print(count_nodes(tree3, 0)) # 1
    print(count_nodes(tree3, 1)) # 3
    print(count_nodes(tree3, 2)) # 0

