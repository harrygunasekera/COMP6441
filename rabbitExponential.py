def cycle(lR, nR, cycle):
	lR.append([nR, cycle])
	new = 0
	for c in lR:
		c[1] = c[1] - 1
		if c[1] == 0:
			new = new + c[0]
	lR = [x for x in lR if x[1] != 0]
	return new

ogRabbits = 2
litterSize = 6
cyclesTillMature = 3
cyclesTillDeath = 9*12
month = 0
alive = ogRabbits
mature = ogRabbits
maturingRabbits = []
dyingRabbits = [[2, cyclesTillDeath - cyclesTillMature]]
dead = 0
command = 0
while True:
	if (not isinstance(command, int)) or (isinstance(command, int) and command <= 0):
		command = input("Press Enter for another breeding cycle, a number greater than the current number of months to skip to that point or CTRL C to quit! : ")
		while command.isnumeric() and int(command) <= month:
			command = input("Press any key (except numbers) for another breeding cycle, a number greater than the current number of months to skip to that point or CTRL C to quit! : ")
		if command.isnumeric():
			command = int(command)
			command = command - month
	newRabbits = (mature/2)*litterSize
	newMature = cycle(maturingRabbits, newRabbits, cyclesTillMature)
	mature = mature + newMature
	newDead = cycle(dyingRabbits, newRabbits, cyclesTillDeath)
	dead = dead + newDead
	mature = mature - newDead
	alive = alive + newRabbits - newDead
	month = month + 1
	if isinstance(command, int):
		command = command - 1
		if command != 0:
			continue
	print("Month " + str(month))
	print("Alive: " + str(alive))
	print("Mature: " + str(mature))
	print("Dead: " + str(dead))
