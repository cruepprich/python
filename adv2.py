import os
os.system('clear')

class Location(object):
	def __init__(self, name, exits, items):
		self.name = name
		self.exits = exits
		self.items = items
		self.monsterType = ""
		self.monsterProbability =""

	def __str__(self):
		return "%s has the following exits: %s. And these items %s." \
		% (self.name,self.exits,self.items)

class Food(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health


class Character(object):
    def __init__(self, name, species, location):
        self.name = name
        self.species = species
        self.inventory = []
        self.maxHealth = 100
        self.health = self.maxHealth
        self.maxStrength = 100
        self.strength = self.maxStrength
        self.location = location

    def __str__(self):
        return "%s is a %s, with %s strength and %s health" \
        % (self.name, self.species, self.strength, self.health)

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def getHealth(self):
    	return self.health

    def getLocation(self):
    	return self.location

    def setLocation(self,loc):
    	self.location = loc

    def take(self,item):
    	self.inventory.append(item)
    	print "You now have the %s." % item

    def drop(self,item):
    	self.inventory.remove(item)
    	print "You dropped the %s." % item

    def listInventory(self):
    	return self.inventory[0]

    def eat(self, item):
    	if (self.health + item.health > self.maxHealth):
    		self.health = self.maxHealth
    		print "You can't eat the %s because you're full. Your health is %s." % (item.name,self.health)
        elif (self.health + item.health <= 0):
        	self.health = 0
        	print "%s, you're dead from eating %s." % (self.name,item.name)
    	else:
	    	self.health += item.health
	        print "The %s tastes great. Your health is now %s." % (item.name, self.health)



foyer = Location("Foyer",["east","west"], ["apple","candy"])
kitchen = Location("kitchen",["west","south"],["cake","knife","glass"])

me = Character("Christoph","Person",kitchen)

apple = Food("delicious apple",20)
candy = Food("chocolate candy",-10)
poison = Food("green poison",-100)



print "%s is in the %s. There is a %s." % (me.name,me.location.name,me.location.items)

if "apple" in kitchen.items:
	print "There is an apple"

# inp = raw_input('> ')

# arr = inp.split()

# if arr[0] == 'eat':
# 	print "i'm eating",arr[1]

# 	if arr[1] == 'apple':
# 		me.eat(apple)
# 	elif arr[1] == 'candy':
# 		me.eat(candy)
# 	elif arr[1] == 'poison':
# 		me.eat(poison)
	
# elif arr[0] == 'take':
# 	me.take(arr[1])
# 	print "i'm taking"
# else:
# 	print "what?"



