#dictionary
import random
a={1:'r',2:'p',3:'s'}
while(True):

	c=a[random.randint(1,3)]	

	user_input=input("enter rock paper or scissor")
	print("computer puts",c)


	#conditions
	if(user_input=='r'and c=='s' or user_input=='p'and c =='r' or user_input=='s'and c =='r'):
		print("you wins")
	else:
		print("you lose!!!!")
	t=input("press q to exit")
	if(t=='q'):
		exit()



