import random

while True:
	i=input("enter 'r' to roll ,the dice 'q' to quit")
	if(i=='q'):
		print("Bye!")
		exit()

	else:
		print("you got",random.randint(1,6))
