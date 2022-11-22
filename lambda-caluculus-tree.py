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


	
def tree(string):
	i = 0
	if string[0] == "L" :
		return abst_tree(string[1:])
	while(i < len(string)):
		if string[i] == "(":
			if string[i+1] == "L":
				if(i == 0):
					node,x = abst_tree(string[i+2:])
					i += x + 2
					
				else:
					node2 = Node("*")
					node2.left = node
					node2.right,x = abst_tree(string[i+2:])
					node = node2
					i += x + 2
			else:
				node2 = Node("*")
				node2.left = node
				node2.right,x = tree(string[i+1:])
				i += x + 1
				node = node2
		elif string[i] == ")":
			return node,i
		else:
			if i == 0:
				node = Node(string[0])
			else:
				node2 = Node("*")
				node2.left = node
				node2.right = Node(string[i])
				node.parent = Node(node2)
				node = node2
		i = i+1
	return node,i


def abst_tree(string):
	if(string[0] == "."):
		pre,l = tree(string[1:])
		return pre,l+1
	node = Node(".")
	node.left = Node(string[0])
	node.right,l= abst_tree(string[1:])
	return node,l+1
		

l = "Lxypq.xp(ypq)"
node,i = tree(l)
print_tree(node,0)