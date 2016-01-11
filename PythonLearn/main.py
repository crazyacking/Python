# from Tools.scripts.treesync import raw_input
#
# name=raw_input("input your name")
# print(name)


# print("Hello World!")
# a='Hello World!'
# print(a)


# a=str("10000000")
# print(a)

# print(repr(100000))

# temp=42
# print("one is " + str(temp))

# name=input("What's your name?")
# print("Hello,"+name)


# print("My name is Devin,\
# I like code,\
# and i like make friends.\
# ")


# print(r"C:\\users\\crazyacking\\Desktop")

# print(u"Hello World!")

# from Tools.scripts.treesync import raw_input
#
# name=input("hehe")
# print(name)
#
# name=raw_input("hebe")
# print(name)


# edward=['Edward Gumby',42]
# john=['John Smith',50]
# database=[edward,john]
# print(database)
# print(edward[0])
# print(edward[-1])
#
#
# print("Hello"[1])


# four=input("")[3]
# print(four)





#####################################
# month_en=[
# 	"January","February","March","April",
# 	"May","June","July","August",
# 	"September","October","November","December"]
#
# day_en=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
#
#
# year=int(input("Year"))
# month=int(input("Month"))
# day=int(input("Day"))
#
# day_name=repr(day)+day_en[int(day-1)]
#
# print(month_en[month-1]+" "+day_name+","+repr(year))


######################################

# num= '123456789'
# print(num[1:3])		#23
# print(num[5:-2])	#67
# print(num[-3:])		#789
# print(num[:3])		#123
# print(num[:])
# print(num[0:10:2])

# num1=[1,2,3,4]
# num2=[5,6,7,8]
# num3=num1+num2
# print(num3)

# sequence=[None]*10
# print(sequence)



# content='rw'
# print('r' in content)
# print('x' in content)


# content='abcdefg'
# print('def' in content)	#True
# print('abs' in content)	#False


# database=[
# 	['albert','1235'],
# 	['dilbert','2323'],
# 	['smith','1235'],
# 	['joins','4584']
# ]
#
# username=input("user name:")
# pin=input("PIN　CODE:")
#
# if[username,pin] in database:
# 	print("Yes")

# num=[2,3,4,5,6,7]
# length=len(num)
# print(length)
# maxnum=max(num)
# print(maxnum)
# minnum=min(num)
# print(minnum)

# li=list("Hello World!")
# print(li)
#
# str=''.join(li)
# print(str)

# num=[1,2,3]
# print(num)
#
# num[2]=0
# print(num)
#
# del(num[2])
# print(num)


# name=list('Perl')
# print(name)
#
# name[2:]=list('ar')
# print(name)


# name=list('Perl')
# name[1:]=list('ython')
# print(name)

# num=[1,5]
# num[1:1]=[2,3,4]
# print(num)


# num=[1,2,3,4,5]
# num[1:4]=[]
# print(num)


# num=[1,2,3]
# num.append(4)
# print(num)


# word=['to','be','ro','not','to','be','be']
# n=word.count('to')
# print(n)



# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)
# print(a)


# knights=['we','are','the','knights','who','say','ni','who']
# idx=knights.index('who')
# print(idx)


# num=[1,2,3,5,6,7]
# num.insert(3,'four')
# num[3:3]=['four']
# print(num)


# num=[1,2,3]
# x=num.pop()
# print(x)
# print(num)

# x=['to','be','or','not','to','be']
# x.remove('be')
# print(x)



# x=[2,6,3,4]
# x.sort()
# print(x)

# x=[2,6,3,4]
# y=sorted(x)
# print(x)
# print(y)

# x=['aardvark','abalone','acme','add','aerate']
# x.sort(key=len)
# print(x)

# x=(1,2,3)
# print(x)

# string='Hello'
# tupl=tuple(string)
# print(tupl)

# string="Hello,%s. todday is %s"
# values=("crazyacking","Friday")
# print(string%values)


# format="Pi with three decimals:%.3f"
# from math import pi
# print( format % pi)


# from string import Template
# s=Template("$x, nice $x!")
# print(s.substitute(x='girl'))

# from string import Template
# s=Template("It's ${x}ful")
# print(s.substitute(x="wonder"))

# string=" %s plus %s equal %s" % (1,1,2)
# print(string)


# print("Price of eggs: $%d" %42)

# print("Hexadeciaml price of eggs:%x" %42)


# from math import pi
# print("Pi is %.3f" %pi)

# from math import pi
# print("%10.3f" %pi)

# from math import pi
# print("%-10.2f" % pi)


# print("%+d"%10+'\n' + "%+d"%-10)


# width=int(input('Please enter width:'))
# price_width=10
# item_width=width-price_width
# header_format='%-*s%*s'
# format		 ='%-*s%*.2f'
# print("="*width)
# print(header_format%(item_width,'Item',price_width,'Price'))
# print('-'*width)
# print(format%(item_width,'Apples',price_width,0.4))
# print(format%(item_width,'Pears',price_width,0.5))
# print(format%(item_width,'Cantaloupes',price_width,1.93))
# print(format%(item_width,'Dried Apricots(16 0z.)',price_width,9))
# print(format%(item_width,'Prunes(4 1bs.',price_width,12))
# print('='*width)




# str='With a moo-moo here,and a moo-moo there'
# print(str.find('moo'))

# str='With a moo-moo here,and a moo-moo there'
# print(str.find('moo',20,25))

# seq='My name is Devin'
# a=seq.split()
# print(a)
# b=''.join(seq)
# print(b)
# c='+'.join(seq)
# print(c)


# str="123ABCdef"
# a=str.lower()
# print(a)
# b=str.upper()
# print(b)

# str="that's all,folks"
# a=str.title()
# print(a)
# b=str.capitalize()
# print(b)

# str='This is a test'
# a=str.replace('is','eez')
# print(a)

# str='         Hello World!        '
# a=str.strip()
# print(a)

# phonebook={"Alice":"123","Beth":"234","Cecil":"345"}
# print(phonebook["Alice"])
# print(phonebook["Beth"])
# print(phonebook["Cecil"])


# items=[("name","Gumby"),("age",42)]
# d=dict(items)
# print(d)
# print(d['name'])
# print(d["age"])
# del d["name"]

#简单的key/value数据库
# people={
# 	"Alice":
# 		{
# 			"phone":"123",
# 			"add":"Foo dirve 23"
# 		},
# 	"Beth":
# 		{
# 			"phone":"234",
# 			"add":"Bar street 42"
# 		},
# 	"Cecil":
# 		{
# 			"phone":"345",
# 			"add":"Baz avenue 90"
# 		}
# }
#
# labels={
# 	"phone":"phone number",
# 	"add":"address"
# }
#
#
# name=input("name:")
# request=input("Please input Phone number(p) or address(a)?")
#
# if(request=='p'):key='phone'
# elif(request=='a'):key='add'
# if(name in people):
# 	print("%s's %s is %s."% (name,labels[key],people[name][key]))

# phonebook={"Alice":"123","Beth":"234","Cecil":"345"}
# print("Cecil's phone is %(Cecil)s." %phonebook)


# template=\
# """<html>
# <head><title>%(title)s</title></head>
# <body>
# <h1>%(title)s</h1>
# <p>%(text)s</p>
# </body>
# """
#
# data={"title":"My Home Page","text":"Welcome to my home page!"}
# print(template%data)


# phonebook={"Alice":"123","Beth":"234","Cecil":["345","456","567"]}
# y=phonebook.copy()
# print(y)
# y["Cecil"].remove("345")
# print(y)
# print(phonebook)

# from copy import deepcopy
# phonebook={"Alice":"123","Beth":"234","Cecil":["345","456","567"]}
# y=deepcopy(phonebook)
# print(y)
# y["Cecil"].remove("345")
# print(y)
# print(phonebook)

# d={}.fromkeys(['name','age'])
# d=dict.fromkeys(['name','age'])
# print(d)

# d=dict.fromkeys(['name','age'],'unknown')
# print(d)


# phonebook={"Alice":"123","Beth":"234","Cecil":"345"}
# print(phonebook["Devin"])

# phonebook={"Alice":"123","Beth":"234","Cecil":"345"}
# print(phonebook.get("Devin","N/A"))

# d={"a":1,"b":2,"c":3,"d":4}
# while(len(d)>0):
# 	v=d.popitem()
# 	print(v)

# d={"Alice":"123","Beth":"234","Cecil":"345"}
# print(d.setdefault("Devin","495"))
# print(d)

# d={"Alice":"123","Beth":"234","Cecil":"345","Devin":"123"}
# print(d.keys())
# print(d.values())


