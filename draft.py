'''Draft version of CYOA.
This version contains some intentional errors and bad coding. Fix!'''
 
 
book={
'foyer' : {'text' : "You are in the spooky foyer! To the left is a creepy bathroom and straight ahead is a terrifying kitchen.", 
	'choices' : [('Go left into the bathroom','bathroom1'),('Head straight to the kitchen','kitchen'),], },
'bathroom1' : {'text':"The bathroom contains a scary looking toilet that keeps running no matter how many times you jiggle the handle. Think of all that wasted water! Al Gore's worse nightmare!" , 
	'choices' : [], },
'kitchen' : {'text':'The kitchen is dirty but on the rickety looking table is a delicious chocolate cake, a knife, and a plate with a fork.', 
	'choices' : [('Eat the cake','deathbychocolate'),("Don't eat the cake",'benice'),],},
'deathbychocolate':{'text':'You take a bite of the piece of cake you carefully cut. It is magnificent! You finish the first piece but still feel compelled to another... and another.. until the whole cake is gone. Unfortunately, you experience death by chocolate.',
	'choices':[]},
"benice":{'text':"Nice of you to not eat someone else's cake. You're so nice in fact that you take to tidying up the kitchen. Unfortunately, while washing the floor you slip and bang your head on the corner of the counter. You die from loss of blood. Never pays to be nice, eh?",
	'choices':[]},
}
 
import random
def grue_eats(position):
	if position=='bathroom':
		return random.random() > 0.80
	else:
		return False
 
def move(choices):
    ''' choices should be a list'''
    c=[]
    print choices
    for x in choices:
        print x[0]
        c.append(x[0])
    print ""
    text = "What next? "
    ans= raw_input(text)
    ans.lower().strip()
    while ans not in c:
        print "That answer,", ans, ", isn't in the choices"
        ans=raw_input(text)
    	ans.lower().strip()
    for x in choices:
    	if ans in x:
    		return x[1]
 
def play_game():
    position = 'foyer'  
    print book[position]['text']
    while book[position].get('choices',None):	
    	position = move(book[position]['choices'])
    	print "\n", book[position]['text'], "\n"
    if position=='bathroom':
		if grue_eats(position):
			print "You've been eaten by a Grue. Spot of bad luck eh chap!"
		else:
			print "You hear the rustling of a Grue! You run for your life, never to return!"
    print "You have reached the end of our adventures. Goodbye!"

play_game()