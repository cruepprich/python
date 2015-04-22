import os, advClasses, random
import sys,time

os.system('clear')
ac = advClasses

foyer = ac.Location("Foyer",["east","west"], ["apple","candy"])
kitchen = ac.Location("kitchen",["west","south"],["cake","knife","glass"])

me = ac.Character("Christoph","Player",kitchen,20,5)
grue = ac.Character("Evil Weevil","Grue",kitchen,10,3)


knife = ac.Item("knife","weapon", 2)
sword = ac.Item("sword","weapon", 5)
nuclear = ac.Item("Nuclear Option","weapon", 50)
nutella = ac.Item("nutella","item", 0)

me.take(sword)
me.take(knife)
#me.take(nutella)
me.take(nuclear)
grue.take(knife)

me.listInventory
# print me.getCombatStats()
# print grue.getCombatStats()

fighters = [me,grue]
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


spinner = spinning_cursor()

def spin(duration):
	for _ in range(duration):
		sys.stdout.write(spinner.next())
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\b')

def getAttack(character):
	dieRoll = random.randint(1,6)
	attack = dieRoll + character.getAttack()
	return attack


def fight(fighters):
	a = fighters[0]
	b = fighters[1]

	print a.name, "vs.", b.name

	ans = raw_input("(A)ttack with %s or (F)lee? " % me.getTopWeapon())
	ans.lower()

	if ans == 'a':
		os.system('clear')
		print "Attacking with %s." % a.getTopWeapon()
		spin(8)
		dieRoll = random.randint(1,6)
		print "Rolled a %s." % dieRoll
		damage = round(max(dieRoll + a.getAttack() - b.armor,0),0)
		print "You damage %s with %d." % (b.name,damage)
		b.setHealth(b.health - damage)


		print "%s fights back with %s." % (b.name,b.getTopWeapon())
		print
		spin(8)
		dieRoll = random.randint(1,6)
		print "Rolled a %s." % dieRoll
		damage = round(max(dieRoll + b.getAttack() - a.armor,0),0)
		print "%s damages %s with %d." % (b.name,a.name,damage)
		a.setHealth(a.health - damage)

	else:
		print "%s wins because you're a coward!" % b.name
		return

	if a.health <= 0 or b.health <=0 :
		if a.health <= 0:
			loser  = a
			winner = b
		else:
			loser  = b
			winner = a

		print "%s is dead." % loser.name
		print "%s is the winner" % winner.name
	else:
		print "Next round. %s: %s, %s: %s" % (a.name,a.health,b.name,b.health)
		fight(fighters)



fight(fighters);