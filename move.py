def move(dir):
	for x in dir:
		print x

	print ' '

	ans = raw_input("> ")
	ans.lower().strip()

	if ans in dir:
		print "You moved %s." % ans
		return move(["up","down","left","right"])
	else:
		print "What?"
		return move(["up","down","left","right"])

move(["up","down","left","right"])