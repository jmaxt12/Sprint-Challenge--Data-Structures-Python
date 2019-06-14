import time

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value): #adds the input value to the binary search tree, 
                           #adhering to the rules of the ordering of elements in a binary search tree.
    if value >= self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)
    elif value < self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
        

  def contains(self, target): #searches the binary search tree for the input value, 
                              #returning a boolean indicating whether the value exists in the tree or not.
    if target == self.value:
      return True

    if target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False
    if target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        return False



  def get_max(self): #returns the maximum value in the binary search tree.
    if self.right:
      return self.right.get_max()
    else:
      return self.value

  def for_each(self, cb): #performs a traversal of _every_ node in the tree, 
                          #executing the passed-in callback function on each tree node value. 
                          #There is a myriad of ways to perform tree traversal; in this case any of them should work. 
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

