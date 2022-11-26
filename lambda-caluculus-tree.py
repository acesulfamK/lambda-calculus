'''
Node tree(string):
	string型でラムダ式を受け取り、構文構造を取って木構造にしそのルートノードを返す
print_tree(Node):
	ノードを受けると、そのノード以下の木構造をプリントする
print_expression(node,option = "casual"):
	ノードを受けると、そのノード以下の木構造をラムダ式に直してプリントする

node.assign("c",node):
	自由変数"c"をnodeの表すラムダ式に置き換える。

'''

import numpy as np

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
		
	def swap_node(self,node):
		if self.parent != None:
			if self.parent.left == self:
				self.parent.add_left(node)
			elif self.parent.right == self:
				self.parent.add_right(node)

	def swap_name(self,a,b):
		if self.name == a:
			self.name = b
		if self.left != None:
			self.left.swap_name(a,b)
		if self.right != None:
			self.right.swap_name(a,b)

	def characters_set(self,s = set({})):
		if self.name not in (s | set([".","*"])):
			s.add(self.name)
		if self.left != None:
			s = self.left.characters_set(s)
		if self.right != None :
			s = self.right.characters_set(s)
		return s
			
	def assign(self,a,node):
		if self.name == a:
			self.swap_node(node)
		elif self.name == ".":
			if self.left.name in node.characters_set(set()):
				self.swap_name(self.left.name,diff_char(self.characters_set(set())|node.characters_set(set())).pop())
			if self.left.name == a:
				return 
		if self.left != None:
			self.left.assign(a,node)
		if self.right != None:
			self.right.assign(a,node)

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
	if c in ["L","(",")",".","*"]:
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
	print('\n')

	
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
	if isvar(node.name):
		print(node.name,end = '')
	elif node.name == "*" :
			if(node.parent != None and node.parent.name == "*"  and node != node.parent.left):
				print("(", end = '')
			print_casual_expression(node.left)
			print_casual_expression(node.right)
			if(node.parent != None and  node.parent.name == "*" and node != node.parent.left):
				print(")", end = '')
	elif node.name == ".":
			if node.parent == None:
				print("L",end = "")
			elif(node.parent != None and not node.parent.name == "."):
				print("(L",end="")

			print_casual_expression(node.left)

			if(node.right.name != "."):
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


    
def diff_char(char_set):
	'''
		argument: char_set
		return: set
	'''
	s = np.array(range(97,123))
	character_set= set({})
	
	for i in s:
		character_set.add(chr(i))
	
	diff = character_set.difference(char_set)
	return diff

		
l = "(Lxypq.xp(ypq))(Lfx.f(fx))(Lfx.f(f(fx)))"
l2 = "(La.ba)(Lc.bac(Lc.ca))"
l3 = "Lab.cabacbd"
m = "Lz.z"

nodel2,i = tree(l2)
nodel3,i = tree(l3)
nodem,i = tree(m)
print_expression(nodel2,option = "formal")
print_expression(nodel3)
nodel3.assign("c",nodem)
print_expression(nodel3)