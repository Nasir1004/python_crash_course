# motorcycle = ["honda", "yamaha", "suzuki"]
# print(motorcycle)

# motorcycle[0] = 'NAERLS/ABU ADOPTED VILLAGE WOMEN FARMERS S/GARI'

# print(motorcycle)

# motorcycle = ['honda', 'yamaha', 'suzuki']
# print(motorcycle)

# popped_motorcycle = motorcycle.pop()
# print(motorcycle)
# print(popped_motorcycle)

# # 
# cars = ['bmw', 'audi', 'suzuki', 'toyota', 'subaru']
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nhere is the original list again")
# print(cars)

# motorcycle = ['honda', 'yamaha', 'suzuki']
# print(motorcycle[-1])


# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# 	print(magician)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# 	print(f"{magician.title()}, that was a great trick!")
# 	print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("thank u everyone that was g great magic show")

# for value in range(1, 5):
# 	print(value)

# even_numbers = list(range(1, 11, 2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
# 	square = value ** 2
# 	squares.append(square)
# print(squares)

# player = ['charles', 'martin', 'michel', 'florence', 'eli']
# print(player[0:4])

# players = ['charles', 'martin', 'florence', 'eli']

# print('Here are the first three player on my team')
# for player in players[:3]:
# 	print(player.title())

# dimension = (200, 50)
# dimension[0] = 250
# print(dimension[0])
# print(dimension[1])

# dimension = (200, 50)
# print("original dimension: ")
# for dimension in dimension:
# 	print(dimension)

# dimension = (400, 100)
# print("\nModified dimension")
# for dimension in dimension:
# 	print(dimension)

# answer = 17

# if answer != 42:
# 	print("that is not the correct answer. Please try again!")

# 	

# banned_user = ['andrew', 'carolina', 'david']

# user = 'marie'

# if user not in banned_user:
# 	print(f"{user.title()}, you can post a response if u wish." )

# requested_topping = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_topping:
# 	print("Adding mushrooms")

# available_topping = ['mushrooms', 'olive', 'grren peppeers,'

#                       'pepperoni', 'pineeaple', 'extra cheese']

# requested_topping = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_topping:
# 	if requested_topping in available_topping:
# 		print(f"Adding {requested_topping}.")
# 	else:
# 		print(f"Soory, we don't have {requested_topping}.")

# 		print("\nFinished making your pizza")


# alien_0 = {'color': 'green', 'point': 5}

# new_point = alien_0['point']
# print(f"You just earned {new_point} points!")


# alien_0 = {'color': 'green', 'point': 5}
# print(alien_0)

# alien_0['x_position'] = 0 
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['point'] = 5

# print(alien_0)


#Move the alien to the right.
#Determine how far to move the alien based on it current speed

# if alien_0['speed'] == 'slow':
# 	x_increment = 1
# elif alien_0['speed'] == 'medium':
# 	x_increment = 2
# else:
# 	# this must be a fast alien
# 	x_increment = 3

# # the original position is the old positon the increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_increment']}")

# alien_0 = {'color': 'green', 'point': 5}
# print(alien_0)

# del alien_0['point']
# print(alien_0)

# alien_0 = {'color': 'green', 'point': 5}
# point_value = alien_0.get('point', 'no point value assigned')
# print(point_value)


# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#  print(language.title())


# alien_0 = {'color': 'green', 'point': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_1]
# for alien in aliens:
# 	print(alien)

#Make an empty list for storing aliens.
# aliens = []

# #make 30 green aleins

# for alien_number in range(30):
# 	new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
# 	aliens.append(new_alien)

# 	# show the first 5 aliens
# 	for alien in aliens[:5]:
# 		print(alien)
# 	print("......")	


# favorite_languages = {
# 	'jen': ['python', 'ruby'],
# 	'sarah': ['c'],
# 	'edward': ['python', 'haskell']
# }

# for name, languages in favorite_languages.items():
# 		print(f"{name.title()}'s favorite_languages are:")
# 		for language in languages:
# 			print(f"\t{language.title()}")

# users = {
# 	'aeintein': {
# 	    'first': 'albert',
# 	    'last': 'enstien',
# 	    'location': 'princetion'
# 	},

# 	'mcurie': {
# 	'first': 'marie',
# 	'last': 'curie',
# 	'location': 'paris',
# 	},
# }

# for username, user_info in users.items():
# 	print(f"\nusername: {username}")
# 	full_name = f"{user_info['first']} {user_info['last']}"

# 	location = user_info['location']

# 	print(f"\tFull name: {full_name.title()}")
# 	print(f"\tLocation: {location.title()}")

# message = input("Tell me something and i will repeat it back for you")
# print(message)

# height = input("how tall are you, in inches? ")
# height = int(height)

# if height >= 48:
# 	print("\nYou 're tall enough to ride")
# else:
# 	print("\nYou 'll be able to ride when you' are little older")

# current_number = 1
# while current_number <= 5:
# 	print(current_number)
# 	current_number += 1

# prompt = "\nTell me something and i will repeat it for you:"
# prompt += "\n enter 'quit' to end the program"

# active = True
# while active:
# 	message = input(prompt)

# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(message)

# current_number = 0
# while current_number < 10:
# 	current_number +=1
# 	if current_number % 2 == 0:
# 		continue
# 	print(current_number)



# Start with user that need to be verified,
# and an empty list to hold conformed users.
# unconfirmed_users = ['alice', 'brain', 'candace']
# confirmed_users = []

# Verified each user untill there are no more unconfirmed users.
# move each verified user into the list of confirmed user

# while unconfirmed_users:
# 	current_user = unconfirmed_users.pop()

# 	print(f"Verified user:  {current_user.title()}")
# 	confirmed_users.append(current_user)
# #
# #Display all confirmed user 

# print("\nthe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
# 	print(confirmed_user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
# 	pets.remove('cat')

# 	print(pets)

# response = {}

# # set a flag to indicate that polling is active.
# polling_active = True

# while polling_active:
# 	# prompt for the person name and response.
# 	name  = input("\nwhat is ur name? ")
# 	responses = input("which mpountain would you like to climb somedays? ")

# 	# store the response in dictionary
# 	responses[name] = response

	# find out if anyone else is going to take the poll
	# repeat = input("woulkd you like to let another person response? (yes/no) ")
	# if repeat == 'no':
	# 	polling_active = False
	# # polling is complete. show the results.
	# print("\n--- poll result ----")
	# for name, response in responses.items():
	# 	print(f"{name} would you like to climb {response}")

# def get_formated_name(first_name, midlle_name, last_name):
# 	if midlle_name:
# 		full_name = f"{firs_name} {midlle_name} {last_name}"
# 	else:
# 		full_name = f"{first_name} {last_name}"
# musician  = get_formated_name('jimi', 'hendrix')
# print(musician)

# musician = get_formated_name('john', 'hooker', 'lee')
# print(musician)	














      # FUNCTIONS

# def greet_user(username):
# 	"""Display a simple greeting """
# 	print(f"Hello, {username.title()}!")
# greet_user('nasir')	

# def describe_pet(animal_type, pet_name):
# 	"""Display information about pet."""
# 	print(f"\nI have a {animal_type}.")
# 	print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type = 'hamster', pet_name = 'harry')

# def get_formatted_name(firs_name, last_name):
# 	"""Return a full name, neatly formated."""
# 	full_name = f"{firs_name} {last_name} "
# 	return full_name.title()
# musician = get_formatted_name('jimi', 'hendrex')
# print(musician)	

# def get_formated_name(first_name, midlle_name, last_name):
# 	"""Return a full name, neatly formated """
# 	full_name = f"{first_name} {midlle_name} {last_name}"
# 	return full_name.title()

# musician = get_formated_name('john', 'lee', 'hooker')
# print(musician)

# def build_person(first_name, last_name):
#  """ Return a dictionary of information about a person """
#  person = {'first': first_name, 'last': last_name}
#  return person

# musician = build_person('jimi', 'hendrix')
# print(musician)


# def get_formated_name(firs_name, last_name):
# 	"""return a full name, neatly formated """
# 	full_name = f"{firs_name} {last_name} "
# 	return full_name.title()

# 	#this is an infinite loop
# 	while True:
# 		print("\nPlease tell me your name:")
# 		f_name = input("firs_name")
# 		l_name = input("last_name")

# 		formated_name = get_formated_name(f_name, l_name)
# 		print(f"\nHello, {formated_name}")

# def greet_users(names):
# 	"""print a simple greeting to each user in the list"""
# 	for name in names:
# 		msg = f"Hello, {name.title()}!"
# 		print(msg)
# username = ['hannah', 'ty', 'margot']
# greet_users(username)

# # start with some design that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dedecahedron']
# completed_models = []

# # simulated printe each design untill none are left.
# # move each design to completed_model after printing 

# while unprinted_designs:
# 	current_design = unprinted_designs.pop()

# 	print(f"Printing model: {current_design}")
# 	completed_models.append(current_design)
# # display all completed design
# print("\nthe following models have been printed")
# for completed_model in completed_models:
# 	print(completed_model)

# def make_pizza(*toppings):
#  """Print the list of toppings that have been requested."""
#  print("\nMaking a pizza with the following toppings:")
#  for topping in toppings:
#  	print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know ABOUT A user."""
	user_info['firs_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstien', 
	                          location='princetion',
	                          field='physics')
print(user_profile)
