import os
os.system('clear')

class Food(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health


class Character(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.inventory = []
        self.maxHealth = 100
        self.health = self.maxHealth
        self.maxStrength = 100
        self.strength = self.maxStrength

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



me = Character("Christoph","Person");
apple = Food("delicious apple",20)
candy = Food("chocolate candy",-10)
poison = Food("green poison",-100)

me.setLocation("kitchen")
print "You're in the %s." % me.getLocation()

me.take("knife")
me.take("fork")
me.take("spoon")
print me.inventory
me.drop("fork")
print me.inventory

me.eat(apple)
me.eat(candy)
me.eat(apple)
me.eat(poison)
print me


