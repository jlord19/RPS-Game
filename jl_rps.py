from random import choice

print "Hi, I am your computer. My name is Jim. We are going to play Rock-Paper-Scissors today. Make your move (r, p, s or q to quit/end game)."

def choice2(s, computer, you):
	x = choice("rps")

	if move == "r" and  x == "r":
		print "I play Rock!"
		print "We Tie!"
		return computer, you
	elif move == "r" and x == "s":
		print "I play Scissors!"
		print "You Win!"
		return computer, you + 1
	elif move == "r" and x == "p":
		print "I play Paper!"
		print "I win!"
		return computer + 1, you
	if move == "p" and x == "p":
		print "I play Paper!"
		print "We Tie!"
		return computer, you
	elif move == "p" and x == "r":
		print "I play Rock!"
		print "You Win!"
		return computer, you + 1
	elif move == "p" and x == "s":
		print "I play Scissors!"
		print "I Win!"
		return computer + 1, you
	elif move == "s" and x == "s":
		print "I play Scissors!"
		print "We Tie!"
		return computer, you
	elif move == "s" and x == "p":
		print "I play Paper!"
		print "You Win!"
		return computer, you + 1
	elif move == "s" and x == "r":
		print "I play Rock!"
		print "I Win!"
		return computer + 1, you

x = 0
y = 0

move = raw_input("Make your move: ")
while move != "q":
	x, y = choice2(move, x, y) 
	print (x, y)

	move = raw_input("Make your move: ") 


print "Game Over! Final Score is Jim: %d, You: %d" %(x, y)












