class Node:
	def __init__(self, item):
		self.item = item
		self.left = None
		self.right = None

class BinaryTree():
	def __init__(self):
		self.root = None
	def find(self, n, item):
		temp_right = None
		temp_left = None
		print("check", n.item)
		print(n.item == item)
		if n != None:
			if n.item == item:
				return n
			if n.left:
				temp_left = self.find(n.left, item)
			if n.right:
				temp_right = self.find(n.right, item)
		if (temp_left != None)
			return temp_left
		return temp_right
	def preorder(self, n):
		if n != None:
			print(n.item, '', end='')
			if n.left:
				self.preorder(n.left)
			if n.right:
				self.preorder(n.right)
	def postorder(self, n):
		if n != None:
			if n.left:
				self.postorder(n.left)
			if n.right:
				self.postorder(n.right)
			print(n.item,'',end = '')
	def midorder(self, n):
		if n != None:
			if n.left:
				self.midorder(n.left)
			print(n.item, '', end='')
			if n.right:
				self.midorder(n.right)

n = int(input())

tree = BinaryTree()
#tree.root = Node("A")

parent1, left1, right1 = map(Node, input().split())

tree.root = parent1
parent1.left = left1
parent1.right = right1

for i in range(1, n):
	parent, left, right = map(str,input().split())
	parent_node = tree.find(tree.root, parent)
	print(parent_node.item)
	if left != ".":
		parent_node.left = Node(left)
	if right != ".":
		parent_node.right = Node(right)

print(tree.root.item)
tree.preorder(tree.root)
print()
tree.midorder(tree.root)
print()
tree.postorder(tree.root)