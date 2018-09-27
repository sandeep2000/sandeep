#using function

a=int(input("enter a number:"))
b=int(input("enter a number:"))

#defining addition
def add():
	return a+b
#defining substraction
def sub():
	return a-b

print("addition=")
r=add()
print(r)

print("sbstraction=")
q=sub()
print(q)


def mul():
	return a*b

print("multiplication=")
s=mul()
print(s)

def div():
	return a%b

print("division=")
t=div()
print(t)