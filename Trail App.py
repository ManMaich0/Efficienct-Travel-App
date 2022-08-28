#Script for calculating the most efficient way to ferry passengers using
#cars and their carrying capacity as the parameters
#Bugs list:
# UNDER CONSTRUCTION All cars have to have the same carrying capacity
#FIXED Bug when 'BUSES' and 'CARS' values are equal
#FIXED Bug when all values equal
#FIXED Bug with 'CARS' > 'BUSES' > 'NO OF CARS' function when 'BUSES' = 'NO OF CARS'
#FIXED Bug when some values are zero.
from sys import exit

# creating variables
def integer_queries():
	"""Integer input prompts"""
	print "How many people are going?"
	people = int(raw_input("> "))
	
	# Multiple per_car value fix (ex30cnt) to be added here
	
	# integer input prompts continued
	print "How many cars are there?"
	cars = int(raw_input("> "))

	print "How many people can COMFORTABLY fit in the car?"
	per_car = int(raw_input("> "))

	print "How many buses are available for travel today?"
	buses = int(raw_input("> "))

	# string printing values
	if people >= 1 and buses >= 1 and cars >= 1:
		print """\n
	So there are %s car(s), %s people, %s people per car and %s bus(es) available.\n
		""" % (cars, people, per_car, buses)

	raw_input("""\n
	If this is not the case, press 'CTRL+Z' to reset and key in correct values.
	
	If it's all good press ENTER to continue
	""")
	
	return people, cars, per_car, buses

# maths for how many cars are needed and creation of new variable
def cars_needed(people, per_car):
	"""Math solutions for cars needed"""
	if people > 0 and people < per_car:
		print "Call travellers and ask them where they are?\n"
		exit(0)
	
	elif (people % per_car) == 0:
		no_cars = people / per_car
	
	elif (people % per_car) == 1:
		no_cars = people / per_car
		print "One of the cars is riding with an extra person.\n"
		
	elif (people % per_car) > 1:
		no_cars = people / per_car
		no_cars += 1
	
	print "We need %d cars.\n" % no_cars
	
	return no_cars

# function that checks for equal values in variables and solves problems that that creates
def equal_value_check(no_cars, buses, cars):
	"""Special set of logic arguments for equal values bug fix"""
	if no_cars >= 10:
		print "That's too many cars. Get bigger cars or use buses."
		exit(0)

	elif no_cars == 0 and buses == 0 and cars == 0:
		print "So there are no cars, no people and no buses.\n"

	elif no_cars == 0 and buses > 1 and cars > 1:
		print "Nothing to do here."

	elif no_cars > 1 and cars == 0 and buses == 0:
		print "No means of transport."

	elif no_cars == cars == buses:
		print "Take the cars."

	elif cars == buses:
		print "Hmm..."
		if no_cars > cars:
			print "Take the bus, dudes."
		elif no_cars < cars:
			print "Take the cars, my dudes."

# logic arguments for the program
def logic_arguments(no_cars, buses, cars):
	"""Logic arguments for program"""
	#(Buses fewer than cars fewer than no_cars)
	if no_cars > cars and  cars > buses:
		print "Take the bus."

	#(Cars fewer than buses fewer than no_cars)
	elif no_cars > buses and buses > cars:
		print "Take the bus."

	#(Cars fewer than buses/no_cars)
	elif no_cars > cars and cars < buses:
		print "Take the bus."

	#(no_cars fewer than buses fewer than cars)
	elif no_cars < buses and buses < cars:
		print "Take the bus."

	#(no_cars fewer than cars fewer than buses)
	elif no_cars < cars and cars < buses:
		print "Take the cars."

	#(Cars/no_cars fewer than buses)
	elif no_cars < buses and buses > cars:
		print "Take the cars."

	#(Buses/no_cars fewer than cars)
	elif no_cars < cars and cars > buses:
		print "Can't make up my mind."

	#(Buses fewer cars/no_cars)
	elif no_cars > buses and buses < cars:
		print "Can't make up my mind."

	else:
		print "Man, I don't know!!! Stay home and watch Netflix."

# explanation of the program's function
print """
Hi there!  This is a program that helps you decide how a group of people
to get to Vihiga using either buses or cars.
Follow the prompts as they appear and safe journey! :D

Note that the program prefers to send as few cars as possible in order to
increase economic and environmental efficiency
"""

people, cars, per_car, buses = integer_queries()
no_cars = cars_needed(people, per_car)

equal_value_check(no_cars, buses, cars)
logic_arguments(no_cars, buses, cars)
