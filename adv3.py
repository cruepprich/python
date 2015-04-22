book = {'The Beginning':{'desc':'It was a dark and stormy night and your car just died. You&#x27;re stranded on a lonely country road late at night.'
      ,'choices' : ['Start Engine'
      ,'Leave the car | Next to the car'
   ]},
   'Start Engine':{'desc':'You turn the key and...nothing. Not a hum or a click. All you hear is the rain splattering onto the car.'
      ,'choices' : ['Spend the night in the car'
      ,'Leave the car | Next to the car'
   ]},
   ' Next to the car':{'desc':'You look around, and as your eyes get adjusted to the darkness, you see a faint light up on a hill about two miles away.'
      ,'choices' : ['Stay here and wait for help'
      ,'Walk toward the house | Walking to the house'
   ]},
   'Spend the night in the car':{'desc':'As time passes on you notice how it gets colder and colder. You are afraid you may freeze out here.','choices' : ['Look for something to warm up '
      ,'Leave the car | Next to the car'
   ]},
   'Look for something to warm up ':{'desc':'There seems to be nothing that could help you fight the cold. You decide to get out of the car.','choices' : ['Leave the car | Next to the car'
   ]},
   'Stay here and wait for help':{'desc':'You wait in vain. The cold finally overtakes you. You get sleepy and fall asleep. A passing grue sniffs you and eats you for dinner.THE END'
   ]},
   ' Walking to the house':{'desc':'You decide to walk to the house. You&#x27;re glad you are moving as you finally get a bit warmer. After about an hour&#x27;s walk you get to the house. It looks run down. The front porch steps creak as you walk up to the door.'
      ,'choices' : ['Knock on the door'
      ,'Peek inside the window'
   ]}
   }

room = raw_input("Which room? ")
mychoices = book[room]['choices']