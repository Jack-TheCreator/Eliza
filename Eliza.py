from random import randrange
flag = True
prev = []


def rule1():
	r = ['Why the uncertain tone?', "Why are you so indecisive?"]
	choice = randrange(len(r))
	return r[choice]

def rule2():
	r = ['We were discussing you, not me.', "You're not really talking about me, are you?"]
	choice = randrange(len(r))
	return r[choice]

def rule3():
	r = ["Please don't apologize.", "Apologies are not necessary"]
	choice = randrange(len(r))
	return r[choice]

def rule4():
	r = ["Tell me more about your family..."]
	choice = randrange(len(r))
	return r[choice]

def rule5():
	r = ["Have you asked such questions before?", "What is it you really want to know"]
	choice = randrange(len(r))
	return r[choice]

def rule6():
	r = ["Does it make you feel strong to use that kind of language?"]
	choice = randrange(len(r))
	return r[choice]

def rule7():
	r = ['I am not interested in names.']
	choice = randrange(len(r))
	return r[choice]

def rule8():
	pre = ["Why do you think", "Did you come to me because"]
	choice = pre[randrange(len(pre))]


	r = []
	r.append(choice)
	for i, word in enumerate(text):
		if((word == "i") and (text[i+1]=="am")):
			r.append("you are")
			for word in text[i+2:]:
				r.append(word)

	return ' '.join(r)


def rule9():
	r = ['Are you sure?', 'You sound positive?']

	for word in text:
		if(word == "no"):
			r.append("You seem uncertain.")

	choice = randrange(len(r))
	return r[choice]

def rule10():
	r = ['Are you sure?', 'Why are you so negative?']

	for word in text:
		if(word == "yes"):
			r.append("You seem uncertain.")

	choice = randrange(len(r))
	return r[choice]

def rule11():
	pre = ["Why are you concerned about my", "What do you know about my"]
	choice = pre[randrange(len(pre))]

	r = []
	r.append(choice)
	for i, word in enumerate(text):
		if(word == 'your'):
			for word in text[i+1:]:
				r.append(word)

	return ' '.join(r)

def rule12():
	pre = ["Why are you interested in whether or not I am", "What makes you think I am"]
	choice = pre[randrange(len(pre))]

	r=[]
	r.append(choice)
	for i, word in enumerate(text):
		if(((word == "you")and(text[i+1]=="are"))or((word=="are")and(text[i+1]=="you"))):
			for word in text[i+2:]:
				r.append(word)

	return ' '.join(r)

def rule13():
	pre = ["What would it mean to you if you got"]
	choice = pre[randrange(len(pre))]

	r=[]
	r.append(choice)
	for i, word in enumerate(text):
		if(word == "i")and((text[i+1]=="need")or(text[i+1]=="want")):
			for word in text[i+2:]:
				r.append(word)

	return ' '.join(r)

def rule14():
	r = "What resemblance do you see?"
	return r

def rule15():
	pre = ["Do you wish to"]
	choice = pre[randrange(len(pre))]

	r=[]
	r.append(choice)
	for i, word in enumerate(text):
		if((word == "i")and(text[i+1]=="dont")):
			for word in text[i+2:]:
				r.append(word)

	return ' '.join(r)

def filler():
	r = ["Do go on", "Tell me more", "Elucidate your thoughts", "Please, go on"]
	choice = randrange(len(r))
	return r[choice]

def prevResponse():
	r=[]
	
	r.append("Earlier you said")
	r.append(prev[randrange(len(prev))])
	r.append("Can you elaborate on that")
	return ' '.join(r)

def question():
	pre = ['Why do you say', 'What makes you say']
	choice = pre[randrange(len(pre))]

	r=[]
	r.append(choice)
	r.append(userIn)

	return ' '.join(r)

def rule16():
	r = []
	r.append("What else comes to mind when you think of")
	r.append(text[0])
	return ' '.join(r)

while(flag):
	userIn = input("Input: ")
	userIn = userIn.lower()
	text = list(userIn.split(" "))
	responses = []

	for i, word in enumerate(text):
		if((word == "perhaps") or (word == "maybe")):
			responses.append(rule1())
		if(word == "you"):
			responses.append(rule2())
		if(word == "sorry"):
			responses.append(rule3())
		if((word == "mother")or(word == "father")or(word == "brother")or(word == "sister")):
			responses.append(rule4())
		if(word[-1] == "?"):
			responses.append(rule5())
		if((word == "gosh")or(word == "darn")):
			responses.append(rule6())
		if((word == "name")or(word == "names")or(word == "named")):
			responses.append(rule7())
		try:
			if((word == "i") and (text[i+1]=="am")):
				responses.append(rule8())
		except:
			pass

		if(word == "yes"):
			responses.append(rule9())
		if(word == "no"):
			responses.append(rule10())
		if(word == "your"):
			responses.append(rule11())

		try:
			if((word == "you") and (text[i+1]=="are")):
				responses.append(rule12())
		except:
			#index out of bounds catcher
			pass

		try:
			if((word == "are") and (text[i+1]=="you")):
				responses.append(rule12())
		except:
			pass

		try:
			if((word == "i") and (text[i+1]=="need")):
				responses.append(rule13())
		except:
			pass
		try:
			if((word == "i") and (text[i+1]=="want")):
				responses.append(rule13())	
		except:
			pass
		try:
			if((word == "you") and (text[i+1]=="are") and (text[i+2]=="like")):
				responses.append(rule14())
		except:
			pass
		try:
			if((word == "i") and (text[i+1]=="dont")):
				responses.append(rule15())
		except:
			pass


	# X is Y rule
	if((len(text)==3)and(text[1]=='is')):
		responses.append(rule16())

	if(len(responses)==0):
		responses.append(filler())
		if(len(prev)!=0):
			responses.append(prevResponse())
		responses.append(question())

	prev.append(userIn)
	resp = responses[randrange(len(responses))]
	print(resp)



