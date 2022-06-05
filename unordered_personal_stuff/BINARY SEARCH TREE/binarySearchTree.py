# EXPLANATION UPFRONT
# A binary tree means, there is a tree of nodes where the only conditions are:
	# 1. The top of the tree is the so called 'root node'
	# 2. Each node only has a maximum of 2 children
	# 3. If a child's value is LESS THAN its parents value, it goes to the left_child SIDE of the connecting edge
	# 4. If a child's value is GREATER THAN its parents value, it goes to the right_child SIDE of the connecting edge
useful_url = r"https://www.youtube.com/watch?v=f5dU3xoE6ms&t=659s"
# Let's code it up:

class Node:
	
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None

class BST:
	"""acts as a 'wrapper class' (or 'manager class') for our Node class and all its instances"""

	def __init__(self):
		self.root = None


	def insert(self, new_value): # IMPORTANT:
		"""checks if there even is a root node yet
		if not, it will instantiate a new one ond assign it as the BST's root node
		if a root DOES indeed exist, it will call the PRIVATE .__insert() method"""

		if self.root is None:
			self.root = Node(new_value)  # instantiate a node with the current_node value-input

		else:  # IF there already IS a root node, find out where to attach the new note according to:
			self.__insert(new_value, self.root)
	# IMPORTANT:
	# passing in 'self.root' as a parameter here is ESSENTIAL for our private method to even work!

	def __insert(self, new_value, current_node):  # the current_node param here will be passed in automatically by .insert()
		"""
		This is a PRIVATE(!) function -> can be told from the dunders in front of the method's name.
		What it does is:
		- Becoming aware of the node we're currently starting our insert-decision-traversal from,
		- Check the smaller/greater status of the node that was passed in vs. the current node's,
		- Whatever the leaf node is that we're ending up to insert at, check if a child is already in place
			if so, start the traversal from that very child
		"""
		if new_value < current_node.value:  # case: new node's value is smaller than the one we're currently looking at

			if current_node.left_child is None:  # case: the current node does not have a left child yet
				current_node.left_child = Node(new_value)  # initialize a left child
			else:
				# IMPORTANT: AT THIS POINT IT GETS RECURSIVE(!)
				self.__insert(new_value, current_node.left_child)
		# Now that we are actually calling the .__insert() method AGAIN,

		# we're demanding it to ask:
		# "alright, where do you want me to insert it this time?"
		# and responding to that with:
		# "yeah well, take what you already have but apply the .__insert method to its LEFT CHILD"

		elif new_value > current_node.value: # case: new node is greater than the one we're current_node looking at

			if current_node.right_child is None:  # case: the current node does not have a right child yet
				current_node.right_child = Node(new_value)
			else:
				# IMPORTANT: AT THIS POINT IT GETS RECURSIVE(!)
				self.__insert(new_value, current_node.right_child)
		# Now that we are actually calling the .__insert() method AGAIN,

		# we're demanding it to ask:
		# "alright, where do you want me to insert it this time?"
		# and responding to that with:
		# "yeah well, take what you already have but apply the .__insert method to its RIGHT CHILD"
		else:
			print(f"Value {new_value} could not be inserted; value already in tree!")



	def print_tree(self):
		"""checks if a root exists and if so, hands the actual logical check as well as the print job over to the private method"""
		if self.root is not None:
			self.__print_tree(self.root)

	def __print_tree(self, current_node):
		"""takes a node as input and uses it to print its <left_child>, its own <value>  and  its <right_child>"""
		if current_node is not None:
			self.__print_tree(current_node.left_child)  # which is equivalent of 'print the smallest of the trio'
			print(str(current_node.value))  # this gets printed in any case (depending on what node the private function receives as a param)
			self.__print_tree(current_node.right_child)  # which is equivalent of 'print the largest of the trio'



	def tree_height(self):
		"""lets us know how many levels/tiers of nodes there are within our BS tree"""
		if self.root is not None:
			return self.__tree_height(self.root, 0)  # 1st param here will be
		else:
			return 0

	def __tree_height(self, current_node, current_height):
		"""uses the node which was passed in by our public '.tree_height()' function as a parameter"""

		if current_node is None: return current_height # if there is no root, return a height of 0
		# when an input node (current node) is in place already, ...
		left_height = self.__tree_height(current_node.left_child, current_height +1)  # ...take it and check for the left arm
		right_height = self.__tree_height(current_node.right_child, current_height +1)  # ...take it and check for the right arm
		return max(left_height, right_height)  # return the 'depth' of whatever is greater

	def search(self, searched_value):
		if self.root is not None:
			return self.__search(searched_value, self.root)

	def __search(self, searched_value, current_node):
		if searched_value == current_node.value:
			return f"{True}, node with value {searched_value} was indeed found within BST! :)"

		# if we're not lucky enough of the quick win 'root being our desired node' but it has a left_child to check, ...
		elif searched_value < current_node.value and current_node.left_child is not None:
			return self.__search(searched_value, current_node.left_child)  # ... apply the method on that left_child recursively
		# or
		elif searched_value > current_node.value and current_node.right_child is not None:
			return self.__search(searched_value, current_node.right_child)  # ... apply the method on that right_child recursively
		# if we still haven't found the value anywhere in the tree
		else:
			return f"{False}, node with value {searched_value} nowhere to be found within our tree! :("



# Actually initialize a BST
tree = BST()

# GLOBAL FUNCTION (independent from our two classes above) -> just to play around and populate a BST with random nodes:
from random import randint
def populate_BST(target_BST, number_of_nodes_to_insert=100, largest_possible_node=1000):

	try:
		for i in range(number_of_nodes_to_insert):
			node = randint(0,largest_possible_node)
			target_BST.insert(node)

	except Exception as err:
		print(f"\n{err}\n the specified target you tried to insert into is not a binary tree!")
# call the populate function:
populate_BST(tree)

# show all the nodes of our tree
tree.print_tree()

# figure out of how many levels our tree consists of by now
print(f"Tree height is: {tree.tree_height()}")

# example of searching for a node with a certain value, e.g. =10
print(tree.search(10))

# show how long it took to run the script
import timeit
print(timeit.timeit())







