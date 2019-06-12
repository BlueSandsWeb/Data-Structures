"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is pointing to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

# ==================================================Doubly Linked List========================================================== #

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # if theres a value create new node
    new_head = ListNode(value)
    if self.head is None:
      self.head = new_head
      self.tail = new_head
    else:
      # add new node before current head node
      self.head.insert_before(value)
      # change head node to new node
      self.head = self.head.prev
      # increment count
    self.length += 1

  def remove_from_head(self):
    if self.head == None:
      return None

    current_head = self.head
    if self.head.next == None:
      self.head = None
      self.tail = None
    else:
      new_head = self.head.next
      self.head.delete()
      self.head = new_head
    self.length -= 1
    return current_head.value


  def add_to_tail(self, value):
    # if theres a value create new node
    if self.tail is None:
      new_tail= ListNode(value)
      if self.head is None:
        self.head = new_tail
      self.tail = new_tail
    else:
      # add new node before current head node
      self.tail.insert_after(value)
      # change head node to new node
      self.tail = self.tail.next
      # increment count
    self.length += 1

  def remove_from_tail(self):
    if self.tail == None:
      return None
    
    current_tail = self.tail
    if self.tail.prev == None:
      self.head = None
      self.tail = None
    else:
      new_tail = self.tail.prev
      self.tail.delete()
      self.tail = new_tail
    self.length -= 1
    return current_tail.value

  def move_to_front(self, node):
    if node is self.tail:
      self.remove_from_tail()
      self.add_to_head(node)
    else:
      self.delete(node)
      self.add_to_head(node)

  def move_to_end(self, node):
    print("Move to end")
    print("node: ", node.value)
    print("head: ", self.head.value)
    print("tail: ", self.tail.value)
    # if node is self.head:
    #   print("if")
    #   self.remove_from_head()
    #   print("step1")
    #   print("node: ", node.value)
    #   print("head: ", self.head.value)
    #   print("tail: ", self.tail.value)
    #   self.add_to_head(node)
    #   print("step2")
    #   print("node: ", node.value)
    #   print("head: ", self.head.value)
    #   print("tail: ", self.tail.value)
    # else:
      print("else")
      self.delete(node)
      print("node: ", node.value)
      print("head: ", self.head.value)
      print("tail: ", self.tail.value)
      self.add_to_tail(node)
      print("node: ", node.value)
      print("head: ", self.head.value)
      print("tail: ", self.tail.value)

  def delete(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev
    return node.value
    
  def get_max(self):
    current_max = self.head.value
    current_node = self.head
    while current_node is not None:
      if current_node.value > current_max:
        current_max = current_node.value
      current_node = current_node.next
    return current_max



# # test add to head initial
# test_list = DoublyLinkedList()
# test_list.add_to_head(1)
# print("list length: ", test_list.length)
# # test add to head after head has one item
# test_list.add_to_head(2)
# print("list length: ", test_list.length)

# print()
# # test remove from head
# print("REMOVE HEAD")
# print("removed head: ", test_list.remove_from_head())
# print("new head: ", test_list.head.value)
# print("list length: ", test_list.length)

# print()
# # test add to tail
# print("ADD TO TAIL")
# test_list.add_to_tail(3)
# print("list length: ", test_list.length)
# print("add 3 to tail: ", test_list.tail.value)

# print()
# # test remove from head
# print("REMOVE TAIL")
# print("old tail: ", test_list.tail.value)
# print("removed tail: ", test_list.remove_from_tail())
# print("new tail: ", test_list.tail.value)
# print("list length: ", test_list.length)

# test_list.add_to_tail(2)
# test_list.add_to_tail(3)
# test_list.add_to_tail(4)
# test_list.add_to_tail(5)

# print()
# print("created list of 1 to 5")

# print("test_list")
# print(test_list.head.value)
# print(test_list.head.next.value)
# print(test_list.head.next.next.value)
# print(test_list.head.next.next.next.value)
# print(test_list.head.next.next.next.next.value)

# print()
# print("test_list.delete(3): ", test_list.delete(test_list.head.next.next))

# print()
# print(test_list.head.value)
# print(test_list.head.next.value)
# print(test_list.head.next.next.value)
# print(test_list.head.next.next.next.value)

# print("max: ", test_list.get_max())