from operator import attrgetter
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

class Item(object):
    def __init__(self, name, type, attack):
        self.name = name
        self.type = type
        self.attack = attack

class Character(object):
    def __init__(self, name, species, location, maxHealth, maxArmor):
        self.name = name
        self.species = species
        self.inventory = []
        self.maxHealth = maxHealth
        self.health = self.maxHealth
        self.maxStrength = 100
        self.strength = self.maxStrength
        self.location = location
        self.maxArmor = maxArmor
        self.armor    = self.maxArmor

    def __str__(self):
        return "%s is a %s, with %s strength and %s health" \
        % (self.name, self.species, self.strength, self.health)

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def getHealth(self):
    	return self.health

    def setHealth(self, health):
        self.health = health

    def getLocation(self):
    	return self.location

    def setLocation(self,loc):
    	self.location = loc

    def take(self,item):
    	self.inventory.append(item)
        if (self.species == "Player"):
            print "You now have the %s." % (item.name)
        else:
            print "%s now has the %s." % (self.name,item.name)

    def drop(self,item):
    	self.inventory.remove(item)
    	print "You dropped the %s." % item.name

    def listInventory(self):
    	return self.inventory[0].name

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

    def getCombatStats(self):
        str = "Health: %s\nStrength: %s\nArmor: %s\nWeapons: \n" % (self.health,self.strength,self.armor)
        #List weapons with the strongest first
        for i in sorted(self.inventory,key=attrgetter('attack'),reverse = True):
            if i.type == 'weapon':
                str += "\t" + i.name + " +%s\n" % i.attack
        return str

    def getTopWeapon(self):
        #List weapons with the strongest first
        for i in sorted(self.inventory,key=attrgetter('attack'),reverse = True):
            if i.type == 'weapon':
                return i.name

    def getAttack(self):
        #List weapons with the strongest first
        for i in sorted(self.inventory,key=attrgetter('attack'),reverse = True):
            if i.type == 'weapon':
                return i.attack

