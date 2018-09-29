import random
count=0
#def myroll():
#   return random.randint(1,6)


while(count<=100):
	n=input("press r roll the dice")
	if(n==r):
		r=random.randint(1,6)
		count=count+r
		print("u got",r)
		print("new position is",count)

		if(count==8):
			count=37
			print("i got the ladder")

		elif(count==11):
			count=2
			print("sorry,u got snake")