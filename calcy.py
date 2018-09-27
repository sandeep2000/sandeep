#printing caluclations

i=int(input("enter value of i:"))
j=int(input("enter value of j:"))
o=input("what you want to do +,-,*,/")

def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	return a/b
	

print("addition=",add(i,j))
print("substraction=",sub(i,j))
print("multiplication=",mul(i,j))
print("division=",div(i,j))
