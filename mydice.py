import random



while True:
	i=input("enter 'n' to quit")
	if(i=='n'):
		print("Bye!")
		exit()

	else:
		print("You got",random.randitn(1,6))