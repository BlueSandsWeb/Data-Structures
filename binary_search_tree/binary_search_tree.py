class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current_node = self
    if value >= current_node.value:
      if current_node.right is not None:
        current_node.right.insert(value)
        print("insert right")
      else:
        current_node.right = BinarySearchTree(value)
        return "Done"
    else:
      if current_node.left is not None:
        print("insert left")
        current_node.left.insert(value)
      else:
        current_node.left = BinarySearchTree(value)
        return "Done"

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass

tree = BinarySearchTree(5)
print(tree.value)

tree.insert(3)
print(tree.left.value)
tree.insert(8)
print(tree.right.value)
tree.insert(4)
print(tree.left.right.value)
tree.insert(6)
print(tree.right.left.value)
