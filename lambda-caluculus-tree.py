class Node:
	def __init__(self,name):
		self.parent = None
		self.name = name
		self.right = None
		self.left = None
		
def print_tree(node,depth):
	print("\t"*depth+str(node.name))
	if(node.right is not None):
		print("\t"*(depth+1)+"right:")
		print_tree(node.right,depth+1)
	if(node.left is not None):
		print("\t"*(depth+1)+"left:")
		print_tree(node.left,depth+1)
	return

	
def tree(string,current):
	node = None
	while current < len(string) :
		if string[current] == "(":
			if node == None:
				node,current = tree(string,current+1)
			else:
				node2 = Node("*")
				node2.left = node
				node2.right,current = tree(string,current+1)
				node = node2

		elif string[current] == ")":
			return node,current
		elif string[current] == "L":
			node,current = tree_abst(string,current+1)
		else:
			if node == None :
				node = Node(string[current])
			else:
				node2 = Node("*")
				node2.left = node
				node2.right = Node(string[current])
				node = node2
		current += 1
	return node,current


def tree_abst(string,current):
	if(string[current] == '.'):
		node,current = tree(string, current+1)
		if current != len(string) and string[current] == ")":
			current -= 1
		return node,current
	else:
		node = Node(".")
		node.left = Node(string[current])
		node.right,current = tree_abst(string,current+1)
		return node,current
		
def print_expression(node):
	if(node.right is None and node.left is None ):
		print(node.name,end = '')
	else:
		if node.name == "*" :
			print("(", end = '')
			print_expression(node.left)
			print_expression(node.right)
			print(")", end = '')
		elif node.name == ".":
			print("L", end = "")
			print_expression(node.left)
			print(".(", end = "")
			print_expression(node.right)
			print(")", end = "")
		else:
			print_expression(node.left)
			print_expression(node.right)

l = "Lxypq.xp(ypq)"
node,i = tree(l,0)
print_tree(node,0)
