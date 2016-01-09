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



x=[2,6,3,4]
x.sort()
print(x)