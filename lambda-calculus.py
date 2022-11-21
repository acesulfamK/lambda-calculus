def deep_cut(string,d):
	'''
    argument 

	string : 操作したい文字列
	d : 取り出したい深さ

	return 
	
	文字列のリスト
	'''
	depth = 0
	ans_str = "" 
	ans_list =[] 
	for c in string:
		if c == "(":
			if depth >= d:
				ans_str = ans_str + c
			else:
				if ans_str != "":
					ans_list.append(ans_str)
					ans_str = ""
			depth = depth + 1
		elif c == ")":
			depth = depth - 1
			if depth >= d:
				ans_str= ans_str + c
			else:
				if ans_str != "":
					ans_list.append(ans_str)
					ans_str = ""
		else:
			if depth >=  d:
				ans_str= ans_str + c
	if ans_str != "":
		ans_list.append(ans_str)
		ans_str = ""
	
	return ans_list


def redex_analyzer(string):
	'''
	argument
	string : (Lx.(P))Qの形の文字列のみを入力すること
	return : (変数,代入されるラムダ式,代入するラムダ式)のタプル
	'''
	argument = string[2]
	p = deep_cut(string,2)[0]
	q = deep_cut(string,1)[1]
	return argument,p,q

def redex_reduction(string):
	x,p,q = redex_analyzer(string)
	return p.replace(x,q)


def step_reduction(string):
	if string[0] == '(':
		if string[1] == 'L':
			string = redex_reduction(string)
		else:
			mn =  deep_cut(string,1)
			string = '('+step_reduction(mn[0])+')'+'('+step_reduction(mn[1])+')'
	return string
                   
def reduction(string,n):
	i = 0
	for i in range(n):
		string = step_reduction(string)
	return string


def lambda_brakets_sugar(string):
	'''
        argument : Lx.Pの形の関数
		return : Lx.(P)
	'''
	list_string= list(string)
	list_string.insert(3,"(")
	list_string.append(")")
	return "".join(list_string)

def lambda_curry_sugar(string):
	'''
		argument : Lxy.Pの形の関数
		return : Lx.(Ly.(P))にして返す
	'''
	list_string = list(string)
	list_string.insert(2,".(L")
	list_string.append(")")
	return "".join(list_string)


true = 'Lx.(Ly.(x))'
false = 'Lx.(Ly.(y))'
                   
s = "(("+true+")"+"(a))(b))"

s = s.replace("\t","").replace(" ","").replace("\n","")
print(reduction(s,100))