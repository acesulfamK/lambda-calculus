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


	
def appl_tree(string):
	node = Node(string[0])
	for i in range(1,len(string)):
		if string[i] == "(":
			node2 = Node("*")
			node2.left = node
			node2.right = appl_tree(string[i+1:])
			node = node2
		elif string[i] == ")":
			return node
		else:
			node2 = Node("*")
			node2.left = node
			node2.right = Node(string[i])
			node.parent = Node(node2)
			node = node2
	return node






root = Node("10")
root.left = Node("9")
root.right = Node("8")
root.right.left = Node("6")
print_tree(root,0)

l = "abcde"
node = appl_tree(l)
print_tree(node,0)
