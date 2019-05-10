import docx2txt
mytext = docx2txt.process("/path/fixed-format.docx")

mytext = mytext.replace("Student", '')
mytext = mytext.replace("Teacher", '') 
mytext = mytext.replace("School", '')
mytext = mytext.replace("City", '')
mytext = mytext.replace("State", '')
for x in range(0, 50):
	mytext = mytext.replace('\n\n\n', '\n')

#print (mytext)
##print(mytext)

middle = mytext


middle = middle.replace('.', ' ')

newtext = middle.replace('\n', '.')


#print(newtext)


'''
print("THIS IS THE CHARACTER")
print(newtext[80])

print("THIS IS THE INDEX")

print(newtext.find("Student"))
'''


name = []
teachername = []
city = []
state = []
school = []
i =0 


start = 0



while(i<10000):
	end = newtext.find('.', start)
	if(end == -1):
		break
	name.append(newtext[start:(end)])
	start = end+2
	end = newtext.find('.',start)
	if(end == -1):
		break
	teachername.append(newtext[start: (end)])
	start = end+2
	end = newtext.find('.',start)
	if(end == -1):
		break
	school.append(newtext[start: (end)])
	start = end+2
	end = newtext.find('.', start)
	if(end == -1):
		break
	city.append(newtext[start:(end)])
	start = end+2
	end = newtext.find('.', start)
	if(end == -1):
		break
	state.append(newtext[start:(end)])
	start = end+2


	i = i + 1

state.append("CT")

#for p in state: 
	#print(p)


def most(list):
	mydict   = {}
	cnt, itm = 0, ''
	for item in list:
	     mydict[item] = mydict.get(item, 0) + 1
	     if mydict[item] >= cnt :
	         cnt, itm = mydict[item], item
	return itm, cnt






themost , amount= most(school)

#print(themost)
#print(amount)

#print(len(name))



