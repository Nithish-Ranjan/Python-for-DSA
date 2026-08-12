class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

key = 60

if search(root, key):
    print("Element Found")
else:
    print("Element Not Found")