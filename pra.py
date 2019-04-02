multiplication of matrix
def dimension(c):
	return len(c),len(c[0])
a=eval(input())
b=eval(input())
r1,c1=dimension(a)
r2,c2=dimension(b)
x=[]
if c1==r2:
	for i in range(c2):
		x.append(0)
	result=[x for i in range(r1)]
	for i in range(r1):
		for j in range(c2):
			for k in range(c1):
				result[i][j]=a[i][k]+b[k][j]
else:
	print('dimension not match')
for i in result:
	for j in i:
		print(j,end=' ')
	print()
#lambda function
f=lambda a:a+a
a=[1,2,3,4,5,6,7,8,9,10]
b=[f(i) for i in range(len(a)]
#initialisation of tuple with single integer
a=(1,)
#input 10 numbers and print the largest and smallest among them
s=[]
for i in range(10):
	a=int(input())
	s.append(i)
a=max(s)
b=min(s)
print(a)
print(b)
#four string methods
(a)isupper()
it check the each character of string, whether they are in uppercase 
(b)islower()
it check the each character of string,whether they are in lowercase
(c)sorted()
it sort the character of a string in ascending order of therir ascii value
a='naman'
b=sorted(a)
print(b)#aamnn
(d)lower()
it convert the character of string in lowercase
a='NAMAN'
b=lower(a)
print(b)#naman
# returning multiple values with function
def addition(a):
	return a*a,a+a,a-a
a=int(input())
print(addition(a))#if input is 2 then output is(4,4,0)
#create an empty list and add 5 element to that list
a=[]
for i in range(5):
	b=int(input()
	a.append(b)
#delete the first element from the list and print the list
b=[1,2,3,4,5]
a=b.pop(0)
print(len(b))
#replace the 4th element of the list by 100 and print list
a=[1,2,3,4,5]
a[3]=100
print(a)
#tuple problem
t=(2,[2,2],2)
t[1][1]=5
print(t)# output is (2,[2,5],2)
