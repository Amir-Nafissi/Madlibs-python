#start of code
list = """

When something is PLURAL, it means it is more than one. For example, door pluralized is doors.

A NOUN is the name of a person, a place, or a thing. An umbrella, toy, door, table, etc. 

A VERB is an action word. Run, pitch, jump, swim, etc.

An ADVERB tells how something is done. It’s a verb that usually ends with "ly." Modestly, stupidly, greedily, carefully, etc.

An ADJECTIVE describes something or someone. Soft, ugly, messy, short, etc.
"""



print("Welcome to Mad Libs!")
print("Today's theme: Ancient Greece and Iran")

while True: 
  answer = input("Do you know your grammer? " ).title()
  if answer.isalpha():
    if answer == "Yes":
      print("That's great! Here is the list anyway:")
      print(list)
      break #loop ends once desired input is achieved
  
    elif answer == "No":
      print("That's fine, here is the list:")
      print(list)  
      break #loop ends once desired input is achieved

    else:
      print('Invalid input, this is a yes/no question. Not a joke. Do not put spaces either.')
  
  else:
    print('Invalid input, this is a yes/no question. Not a joke. Do not put spaces either.')

while True:
  answer = input("Do you wish to start the game? " ).title()
  if answer.isalpha():
    if answer == "Yes":
      adjective1 = input("Enter an Adjective: " )
      adjective2 = input("Enter another Adjective: " )
      name1 = input("Enter the name of a person: " ).title()
      name2 = input("Enter the name of another person: " ).title()
      a_place1 = input("Enter the name of a place: " ).title()
      a_place2 = input("Enter the name of another place: " ).title()
      a_place3 = input("Enter the name of another place: " ).title()
      adverb = input("Enter an adverb: " )
      silly_word = input("Enter a silly word: " ) 
      creatures = input("Enter the plural name of a creature: " )
      a_drink = input("Enter the name of a drink: " )
      
      while True:
        an_age = input("Enter an age: " )
        if an_age.isdigit() or an_age.isdecimal():
          an_age = int(an_age) #prevents type error from happening
          if an_age < 20 or an_age > 100:
            print("The age you have entered is too young or too old!")
  
          else:
            correct_age = an_age #sets the input to the variable that will be used in the story
            print("The age you have entered is valid")
            break
  
        else:
          print("Invalid input!")
          
      part_of_the_human_body = input("Enter a part on the human body: " )
      a_saying = input("Enter a saying: " )
      
      print("here is the result:")
      print("Alexander the" + " " + adjective1 + " " + "was born in 356 B.C., in a region called" + " " + a_place1 + " " + "in northern Greece. When he was twenty years old, his father was murdered by" + " " + name1 + ", after which he became" + " " + adjective2 + " " + "of all Macedonia. In 334, he invaded Persia and defeated" + " " + name2 + " " + "at the battle of" + " " + a_place2 + ". Later, at" + " " + a_place3 + ", he won his most important victory over Darius the Third. This made him" + " " + adverb + " " + silly_word + ". He then marched to ancient India, and many of his" + " " + creatures + " " + "died. After that, Alexander began drinking too much" + " " + a_drink + ", and at the age of" + " " + str(correct_age) + " " + "he died of an infection in the" + " " + part_of_the_human_body + ". His last words are reported to have been," + " " + a_saying + ".") 
      break
      
    elif answer == "No":
      print("Too bad") #the game will start anyway
      adjective1 = input("Enter an Adjective: " )
      adjective2 = input("Enter another Adjective: " )
      name1 = input("Enter the name of a person: " ).title()
      name2 = input("Enter the name of another person: " )
      a_place1 = str(input("Enter the name of a place: " )).title()
      a_place2 = input("Enter the name of another place: " ).title()
      a_place3 = input("Enter the name of another place: " ).title()
      adverb = input("Enter an adverb: " )
      silly_word = input("Enter a silly word: " ) 
      creatures = input("Enter the plural name of a creature: " )
      a_drink = input("Enter the name of a drink: " )
      
      while True:
        an_age = input("Enter an age: " )
        if an_age.isdigit() or an_age.isdecimal():
          an_age = int(an_age)
          if an_age < 20 or an_age > 100:
            print("The age you have entered is too young or too old!")
  
          else:
            correct_age = an_age 
            print("The age you have entered is valid")
            break
  
        else:
          print("Invalid input!")
    
      part_of_the_human_body = input("Enter a part on the human body: " )
      a_saying = input("Enter a saying: " )
      
      print("here is the result:")
      print("Alexander the" + " " + adjective1 + " " + "was born in 356 B.C., in a region called" + " " + a_place1 + " " + "in northern Greece. When he was twenty years old, his father was murdered by" + " " + name1 + ", after which he became" + " " + adjective2 + " " + "of all Macedonia. In 334, he invaded Persia and defeated" + " " + name2 + " " + "at the battle of" + " " + a_place2 + ". Later, at" + " " + a_place3 + ", he won his most important victory over Darius the Third. This made him" + " " + adverb + " " + silly_word + ". He then marched to ancient India, and many of his" + " " + creatures + " " + "died. After that, Alexander began drinking too much" + " " + a_drink + ", and at the age of" + " " + str(correct_age) + " " + "he died of an infection in the" + " " + part_of_the_human_body + ". His last words are reported to have been," + " " + a_saying + ".")  
      break
      

    else:
      print('Invalid input, this is a yes/no question. Not a joke. Do not put spaces either.')
  
  else:
    print('Invalid input, this is a yes/no question. Not a joke. Do not put spaces either.')

#The while loop above is copy pasted twice below:
while True:
  answer = input("Do you wish to play again?: " ).title()
  if answer.isalpha():
    if answer == "Yes":
      adjective1 = input("Enter an Adjective: " )
      adjective2 = input("Enter another Adjective: " )
      name1 = input("Enter the name of a person: " ).title()
      name2 = input("Enter the name of another person: " )
      a_place1 = input("Enter the name of a place: " ).title()
      a_place2 = input("Enter the name of another place: " ).title()
      a_place3 = input("Enter the name of another place: " ).title()
      adverb = input("Enter an adverb: " )
      silly_word = input("Enter a silly word: " ) 
      creatures = input("Enter the plural name of a creature: " )
      a_drink = input("Enter the name of a drink: " )
      while True:
        an_age = input("Enter an age: " )
        if an_age.isdigit() or an_age.isdecimal():
          an_age = int(an_age)
          if an_age < 20 or an_age > 100:
            print("The age you have entered is too young or too old!")
  
          else:
            correct_age = an_age 
            print("The age you have entered is valid")
            break
  
        else:
          print("Invalid input!")
      
      part_of_the_human_body = input("Enter a part on the human body: " )
      a_saying = input("Enter a saying: " )
      
      print("here is the result:")
      print("Alexander the" + " " + adjective1 + " " + "was born in 356 B.C., in a region called" + " " + a_place1 + " " + "in northern Greece. When he was twenty years old, his father was murdered by" + " " + name1 + ", after which he became" + " " + adjective2 + " " + "of all Macedonia. In 334, he invaded Persia and defeated" + " " + name2 + " " + "at the battle of" + " " + a_place2 + ". Later, at" + " " + a_place3 + ", he won his most important victory over Darius the Third. This made him" + " " + adverb + " " + silly_word + ". He then marched to ancient India, and many of his" + " " + creatures + " " + "died. After that, Alexander began drinking too much" + " " + a_drink + ", and at the age of" + " " + str(correct_age) + " " + "he died of an infection in the" + " " + part_of_the_human_body + ". His last words are reported to have been," + " " + a_saying + ".") 
      break
      
    elif answer == "No":
      print("Have a nice day!")
      break
      

    else:
      print('Invalid input, this is a yes/no question. Not a joke. Do not put spaces either.')
  
  else:
    print('Invalid input, this is a yes/no question. Not a joke. Do not put spaces either.')

while True:
  answer = input("Are you sure you want to play again?: " ).title()
  if answer.isalpha():
    if answer == "Yes":
      adjective1 = input("Enter an Adjective: " )
      adjective2 = input("Enter another Adjective: " )
      name1 = input("Enter the name of a person: " )
      name2 = input("Enter the name of another person: " )
      a_place1 = input("Enter the name of a place: " ).title()
      a_place2 = input("Enter the name of another place: " ).title()
      a_place3 = input("Enter the name of another place: " ).title()
      adverb = input("Enter an adverb: " )
      silly_word = input("Enter a silly word: " ) 
      creatures = input("Enter the plural name of a creature: " )
      a_drink = input("Enter the name of a drink: " )
      
      while True:
        an_age = input("Enter an age: " )
        if an_age.isdigit() or an_age.isdecimal():
          an_age = int(an_age)
          if an_age < 20 or an_age > 100:
            print("The age you have entered is too young or too old!")
  
          else:
            correct_age = an_age 
            print("The age you have entered is valid")
            break
  
        else:
          print("Invalid input!")
      part_of_the_human_body = input("Enter a part on the human body: " )
      a_saying = input("Enter a saying: " )
      
      print("here is the result:")
      print("Alexander the" + " " + adjective1 + " " + "was born in 356 B.C., in a region called" + " " + a_place1 + " " + "in northern Greece. When he was twenty years old, his father was murdered by" + " " + name1 + ", after which he became" + " " + adjective2 + " " + "of all Macedonia. In 334, he invaded Persia and defeated" + " " + name2 + " " + "at the battle of" + " " + a_place2 + ". Later, at" + " " + a_place3 + ", he won his most important victory over Darius the Third. This made him" + " " + adverb + " " + silly_word + ". He then marched to ancient India, and many of his" + " " + creatures + " " + "died. After that, Alexander began drinking too much" + " " + a_drink + ", and at the age of" + " " + str(correct_age) + " " + "he died of an infection in the" + " " + part_of_the_human_body + ". His last words are reported to have been," + " " + a_saying + ".") 
      print("You played too many times now, go do something more productive.")
      break
      
    elif answer == "No":
      print("Fine then, have a nice day.")
      break
      

    else:
      print('Invalid input, this is a yes/no question. Not a joke. Do not put spaces either.')
  
  else:
    print('Invalid input, this is a yes/no question. Not a joke. Do not put spaces either.')

#end of code