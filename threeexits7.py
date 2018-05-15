
chance1 = "It will never happen!"
chance2 = "It will happen for sure!"

prompt = "\nTell me your dreams and I will tell you\
	if it will ever come true!"
prompt += "\n[Digite quit to end program!]"

while True:
	message = input(prompt)

	if 'z' in message:
		print(chance1)
	elif 'quit' in message:
		break
	else:
		print(chance2)


