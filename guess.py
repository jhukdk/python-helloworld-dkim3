import random

print("What is your guess for the generated number?")
rando = random.randint(1,20)
print(rando)

for i in range(1,5):
	guessednum = int(input())
	if guessednum > rando:
		print("That is too high")
	elif guessednum < rando:
		print("That is too low")
	else:
		break

if guessednum == rando:
	print("You correctly guessed the number " + str(guessednum) + ". In " + str(i) + "tries!")
else:
	print("The correct number was " + str(rando))
