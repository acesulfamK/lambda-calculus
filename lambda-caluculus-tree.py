'''
Node tree(string):
	string型でラムダ式を受け取り、構文構造を取って木構造にしそのルートノードを返す
print_tree(Node):
	ノードを受けると、そのノード以下の木構造をプリントする
print_expression(node,option = "casual"):
	ノードを受けると、そのノード以下の木構造をラムダ式に直してプリントする

'''


class Node:
	def __init__(self,name):
		self.parent = None
		self.name = name
		self.right = None
		self.left = None
	def add_left(self,node):
		self.left = node
		node.parent = self

	def add_right(self,node):
		self.right= node
		node.parent = self

def print_tree(node,depth = 0):
	print("\t"*depth+str(node.name))
	if(node.right is not None):
		print("\t"*(depth+1)+"right:")
		print_tree(node.right,depth+1)
	if(node.left is not None):
		print("\t"*(depth+1)+"left:")
		print_tree(node.left,depth+1)
	return

def bracket_checker(string):
	count = 0
	i = 0
	for i in range(len(string)):
		if string[i] == "(":
			count += 1
		elif string[i] == ")":
			count -= 1
		if count<0:
			print("syntax error: brackets are wrong!")
			return 1
	if count != 0:
		print("syntax error: brackets are wrong!")
		return 1
	return 0
    
		
def isvar(c):
	if c in ["L","(",")","."]:
		return False
	else:
		return True

def tree(string,current=0):
	if bracket_checker(string)== 1:
		return "error"
	node = None
	while current < len(string) :
		if string[current] == "(":
			if node == None:
				node,current = tree(string,current+1)
			else:
				node2 = Node("*")
				node2.add_left(node)
				temp,current = tree(string,current+1)
				node2.add_right(temp)
				node = node2

		elif string[current] == ")":
			return node,current
		elif string[current] == "L":
			node,current = tree_abst(string,current+1)
		elif isvar(string[current]):
			if node == None :
				node = Node(string[current])
			else:
				node2 = Node("*")
				node2.add_left(node)
				node2.add_right(Node(string[current]))
				node = node2
		else:
			print("syntax error: maybe, there is wrong \".\"")
			return "error"
		current += 1
	return node,current


def tree_abst(string,current):
	if(string[current] == '.'):
		node,current = tree(string, current+1)
		if current != len(string) and string[current] == ")":
			current -= 1
		return node,current
	elif isvar(string[current]):
		node = Node(".")
		node.add_left(Node(string[current]))
		temp,current = tree_abst(string,current+1)
		node.add_right(temp)
		return node,current
	else:
		print("syntax error: there are something wrong after \"L\" before \".\"")
		return "error"
		
		
def print_expression(node,option = "casual"):
	'''
	option: "formal"では、省略をせずに出力する。"casual"をしていすると Lx.Ly.yx などは Lxy.yx とまとめられる。 
		Default is "casual"
	'''
	if option == "formal":
		print_formal_expression(node)
	elif option == "casual":
		print_casual_expression(node)
	else:
		print("error:an option of print_expression is wrong")
	
def print_formal_expression(node):
	if(node.right is None and node.left is None ):
		print(node.name,end = '')
	else:
		if node.name == "*" :
			print("(", end = '')
			print_formal_expression(node.left)
			print_formal_expression(node.right)
			print(")", end = '')
		elif node.name == ".":
			print("L", end = "")
			print_formal_expression(node.left)
			print(".(", end = "")
			print_formal_expression(node.right)
			print(")", end = "")
		else:
			print_formal_expression(node.left)
			print_formal_expression(node.right)
			
def print_casual_expression(node):
	if(node.right is None and node.left is None ):
		print(node.name,end = '')
	else:
		if node.name == "*" :
			if(node.parent != None and node.parent.name == "*"  and node != node.parent.left):
				print("(", end = '')
			print_casual_expression(node.left)
			print_casual_expression(node.right)
			if(node.parent != None and  node.parent.name == "*" and node != node.parent.left):
				print(")", end = '')
		elif node.name == ".":
			if(node.parent != None and not node.parent.name == "."):
				print("(L",end="")
			print_casual_expression(node.left)
			if(node.parent != None and not node.right.name == "."):
				print(".",end="")
			print_casual_expression(node.right)
			if(node.parent != None and not node.parent.name == "."):
				print(")",end="")


def bracket_checker(string):
	count = 0
	i = 0
	for i in range(len(string)):
		if string[i] == "(":
			count += 1
		elif string[i] == ")":
			count -= 1
		if count<0:
			print("syntax error: brackets are wrong!")
			return 1
	if count != 0:
		print("syntax error: brackets are wrong!")
		return 1
	return 0
    
		
l = "(Lxypq.xp(ypq))(Lfx.f(fx))(Lfx.f(f(fx)))"
node,i = tree(l,0)
print_tree(node,0)
print_expression(node,option = "casual")
