import os
os.system('clear')

book={
       'foyer' : {'desc' : "You are in the foyer", 'choices' : ['bathroom','kitchen',], },
       'bathroom' : {'desc':"You are in the bathroom" , 'choices' : ['change toilet paper','leave'] },
       'kitchen' : {'desc':"You are in the kitchen", 'choices' : ['eat the cake', "not eat the cake"]},
       'eat the cake':{'desc':"You are in the eat",'choices':['have a glass of water','wash the plate']},
       "not eat the cake":{'desc':"You are in the dont",'choices':['put the cake in the fridge','sit down']},
       }

# for val in book.itervalues():
# 	print val

# for val in book.iterkeys():
# 	print val


# for b in book:
# 	print book[b]['desc'], book[b]['choices']

# for key, value in book.items():
# 	print key, value

# print book.get('foyer')['desc']

# print book['foyer']['desc']

room = raw_input("Which room? ")
mychoices = book[room]['choices']
cstr = ""
print book[room]['desc']
# print "Do you want to ", mychoices , "?"

for c in mychoices:
	cstr = cstr + " or %s" % c

print "You can",cstr.lstrip(" or")