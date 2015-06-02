#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A program to to help the railroad provide its customers 
with information about the routes.
"""


class TrainRouteInfo:

	"""
	Class implementation of TrainRouteInfo. This class 
	contains the public methods through which one can
	1. compute the distance along a certain route,
	2. compute the number of different routes between two towns,
	3. and compute the shortest route between two towns.
	"""

	# Define constants

	NO_SUCH_ROUTE = 'NO SUCH ROUTE'
	INVALID_GRAPH_FORMAT = \
		"""Input provided is of invalid format. Please provide data as a collection of routes separated by ','. Each route consists of  
		   a start stop followed by a end stop and the distance between the two stops. The stops should be a valid character from A-Z 
		   and the distance should be a integer. The start and end node cannot be same. Sample Format AB5,CD6."""
	INVALID_NODE_FORMAT = \
		'Start Node and End Node are of one character and should be within A-Z'
	INVALID_NUMBER = ' should be a number.'
	CANNOT_BE_ZERO = ' cannot be zero.'
	CAN_ONLY_BE_INTEGER = ' can only be an integer.'
	INVALID_ROUTE_FORMAT = \
		'Routes can only be strings of minimum 2 characters consisting of A-Z'

	def __init__(self, graphInput):
		"""
		constructor of the class which takes the graph input as 
		a parameter. The graph input is splitted and stored in 
		dictionary for later retrieval.
		"""

		# Split the graph input as lists using , as a delimiter
		# and store it as a dictionary with route as key and distance
		# as value

		self.routes = {}

		for graphs in graphInput.split(','):
			graphs = str(graphs).upper().strip()
			TrainRouteInfo.checkInputFormat(graphs)
			self.routes[graphs[0:2]] = graphs[2:]
	@staticmethod
	def checkInputFormat(route):
		"""
		Function to validate the graph input
		"""

		import re

		# We are expecting the route to be of atleast 3 characters
		# We are expecting the first two characters as string and the rest as numbers

		if len(route) < 3 or route[0:1] == route[1:2] \
			or not re.match(r'[A-Z]{2}', route[0:2]) \
			or not re.match(r'[0-9]{' + str(len(route[2:])) + '}',
							route[2:]):

			# if wrong format show a message and quit

			print 'Erroneous route detected: ' + route
			print TrainRouteInfo.INVALID_GRAPH_FORMAT
			quit()

	@staticmethod
	def checkNodeFormat(startNode, endNode):
		"""
		Function to validate the start and end node
		"""

		import re

		# We are expecting the star and end node to be of 1 character
		# We are expecting the nodes to be a value within A-Z

		if len(startNode) != 1 or len(endNode) != 1 \
			or not re.match(r'[A-Z]', startNode) \
			or not re.match(r'[A-Z]', endNode):

			# if wrong format show a message and return

			print 'Start Node: ' + startNode + ' End Node: ' + endNode
			print TrainRouteInfo.INVALID_NODE_FORMAT
			return False
		return True

	@staticmethod
	def checkRouteFormat(route):
		"""
		Function to validate the route
		"""

		import re

		# We are expecting the route to be of atleast 2 characters
		# We are expecting the route to be a string consisting of within A-Z

		if not isinstance(route, str) or len(route) < 2 \
			or not re.match(r'[A-Z]{' + str(len(route)) + '}', route):

			# if wrong format show a message and return

			print 'Route: ' + str(route)
			print TrainRouteInfo.INVALID_ROUTE_FORMAT
			return False
		return True
		
	@staticmethod
	def checkNumberFormat(number, type):
		"""
		Function to validate numbers
		1. It cannot be zero and a non-integer
		"""

		try:
			int(number)
			if not isinstance(number, int):
				print str(number) + ': ' + type \
					+ TrainRouteInfo.CAN_ONLY_BE_INTEGER
				return None

			if int(number) == 0:
				print str(number) + ': ' + type \
					+ TrainRouteInfo.CANNOT_BE_ZERO
				return None
			return int(number)
		except Exception, e:
			print e
			print str(number) + ': ' + type \
				+ TrainRouteInfo.INVALID_NUMBER
			return None

	def computeDistance(self, route):
		"""
		Compute distance of the route provided or else return 
		NO SUCH ROUTE if the provided route is invalid.
		"""

		# Validate inputs

		if not TrainRouteInfo.checkRouteFormat(str(route).upper().strip()):
			return TrainRouteInfo.NO_SUCH_ROUTE

		route = route.strip()

		# Initialise distance as 0

		distance = 0

		# Initialise variables to slice the provided route to
		# determine stops

		startNode = 0
		endNode = 2

		# Keep on slicing the stops from the route until end is reached

		while endNode <= len(route):
			try:
				distance += \
					int(self.routes[route[startNode:endNode].upper()])
			except:

				# If there is a key error then return NO_SUCH_ROUTE

				return TrainRouteInfo.NO_SUCH_ROUTE

			# increment the slicing variables

			startNode += 1
			endNode += 1

		return distance
	
	@staticmethod
	def checkForRouteRepeatation(route):
		"""
		Function to prune a route if a given route A given route 
		appears more than once
		"""

		if len(route) > 3:

			# Initialise variables to slice the provided route to
			# determine stops

			startNode = 0
			endNode = 2

			# Keep on slicing the stops from the route until end is reached

			while endNode <= len(route) - 2:
				if route[startNode:endNode] == route[startNode
					+ 2:endNode + 2]:
					return False

				# increment the slicing variables

				startNode += 2
				endNode += 2
			return True
		else:
			return True

	def computePossibleRoutes(self, startNodes):
		"""
		Loops through the keys in the routes dictionary 
		to find routes that start with nodes in the startNodes
		list and returns back a list of routes
		"""

		# Initialise a list of possibleRoutes

		possibleRoutes = list()

		# Loop through the startNodes

		for node in startNodes:

			# Loop through the keys in routes dictionary
			# and if the routes begin with node then
			# add them to possibleRoutes list

			for (route, distance) in self.routes.items():
				if route[0:1] == node:
					possibleRoutes.append(route)
		return possibleRoutes

	def computeRoutesWithMaxStops(
		self,
		startNode,
		endNode,
		numberOfStops,
		):
		"""
		Function to compute route between two stops. startNode 
		specifies the starting stop and endNode specifies the end stop
		that constitutes the route. noOfStops is the max number of stops
		being allowed in the route
		"""

		# Validate inputs

		if not TrainRouteInfo.checkNodeFormat(str(startNode).upper().strip(),
				str(endNode).upper().strip()):
			return TrainRouteInfo.NO_SUCH_ROUTE
		if TrainRouteInfo.checkNumberFormat(numberOfStops,
				'Number of stops') == None:
			return TrainRouteInfo.NO_SUCH_ROUTE

		# initialse routesFound and stopCount as 0 and startNodes as
		# a list with startNode as the passed start stop of the route
		# to be computed

		routesFound = 0
		stopCount = 0
		startNodes = [startNode.upper().strip()]

		# Loop until stopCount is greater than numberOfStops

		while stopCount < numberOfStops:

			# Get the possible routes that start with the list of nodes

			possibleRoutes = TrainRouteInfo.computePossibleRoutes(self,
					startNodes)

			# Re-initialise the startNodes for the next iteration

			startNodes = []

			# Increment stopCount

			stopCount += 1

			# Loop through the possible routes that start with
			# nodes in the list startNodes

			for route in possibleRoutes:

				# if the end node matches with last stop in the route
				# then increment routesFound. Else add the last stop of the route
				# to the startNode list for the next iteration

				if route[1:2] == endNode.upper().strip():
					routesFound += 1
				else:
					startNodes.append(route[1:2])

		if routesFound == 0:
			return TrainRouteInfo.NO_SUCH_ROUTE
		else:
			return routesFound

	def computeRoutesWithExactStops(
		self,
		startNode,
		endNode,
		numberOfStops,
		):
		"""
		Function to compute route between two stops. startNode 
		specifies the starting stop and endNode specifies the end stop
		that constitutes the route. noOfStops is the exact number of stops
		that needs to be there in the computed route 
		"""

		# Validate inputs

		if not TrainRouteInfo.checkNodeFormat(str(startNode).upper().strip(),
				str(endNode).upper().strip()):
			return TrainRouteInfo.NO_SUCH_ROUTE
		if TrainRouteInfo.checkNumberFormat(numberOfStops,
				'Number of stops') == None:
			return TrainRouteInfo.NO_SUCH_ROUTE

		# initialse routesFound and stopCount as 0 and startNodes as
		# a list with startNode as the passed start stop of the route
		# to be computed

		routesFound = 0
		stopCount = 0
		startNodes = [startNode.upper().strip()]

		# Loop until stopCount is greater than numberOfStops

		while stopCount < numberOfStops:

			# Get the possible routes that start with the list of nodes

			possibleRoutes = TrainRouteInfo.computePossibleRoutes(self,
					startNodes)

			# Re-initialise the startNodes for the next iteration

			startNodes = []

			# Increment stopCount

			stopCount += 1

			# Loop through the possible routes that start with
			# nodes in the list startNodes

			for route in possibleRoutes:

				# if the end node matches with last stop in the route
				# and stoptype is max then increment routesFound. If
				# stopType is exact then increment RoutesFind if stopCount
				# matches noOfStops and if the endNode matches with the
				# last stop in the route. Else add the last stop of the route
				# to the startNode list for the next iteration

				if route[1:2] == endNode.upper().strip() and stopCount \
					== numberOfStops:
					routesFound += 1
				else:
					startNodes.append(route[1:2])
		if routesFound == 0:
			return TrainRouteInfo.NO_SUCH_ROUTE
		else:
			return routesFound

	def computeShortestRoute(self, startNode, endNode):
		"""
		Function to compute shortest distance between two stops
		"""

		# Validate inputs

		if not TrainRouteInfo.checkNodeFormat(str(startNode).upper().strip(),
				str(endNode).upper().strip()):
			return TrainRouteInfo.NO_SUCH_ROUTE

		# initialse routePaths and startNodes as
		# a list with startNode as the passed start stop of the route
		# to be computed. Also intialise the list that will contain
		# computedRoutes

		startNodes = [startNode.upper().strip()]
		routePaths = [startNode.upper().strip()]
		computedShortesDistance = -1
		stopCount = 0

		# Loop until all the routes have been traveresed

		while len(startNodes) > 0:

			# Get the possible routes that start with the list of nodes

			possibleRoutes = TrainRouteInfo.computePossibleRoutes(self,
					startNodes)

			# Re-initialise the startNodes for the next iteration

			startNodes = []

			# create a temporary list

			paths = list()

			# Loop through the possible routes that start with
			# nodes in the list startNodes

			for route in possibleRoutes:

				# Loop through routePaths and if the last node of path
				# in routePaths matches with first node of route in
				# possibleRoutes, append it in paths temp list only if the distance of
				# computedRoute is less than the observed min distance. If the completed route
				# has been calculated then only store it if it's distance is less than the
				# already observed min distance

				for path in routePaths:
					pathDistance = TrainRouteInfo.computeDistance(self,
							path + route[1:2])
					if str(pathDistance) \
						!= TrainRouteInfo.NO_SUCH_ROUTE and path[-1] \
						== route[0:1] and (computedShortesDistance
							== -1 or pathDistance
							< computedShortesDistance):
						if route[1:2] != endNode.upper().strip():
							paths.append(path + route[1:2])
							startNodes.append(route[1:2])
						else:
							if computedShortesDistance == -1 \
								or pathDistance \
								< computedShortesDistance:
								computedShortesDistance = pathDistance

			# Assign the temporary list paths to routePaths
			# after checking for route repeatations and pruning

			routePaths = paths

		# Return the shortest distance

		if computedShortesDistance != -1:
			return computedShortesDistance
		else:
			return TrainRouteInfo.NO_SUCH_ROUTE

	def computeRoutesWithMaxDistance(
		self,
		startNode,
		endNode,
		maxDistance,
		):
		"""
		Function to compute shortest distance between two stops
		"""

		# Validate inputs

		if not TrainRouteInfo.checkNodeFormat(str(startNode).upper().strip(),
				str(endNode).upper().strip()):
			return TrainRouteInfo.NO_SUCH_ROUTE
		if TrainRouteInfo.checkNumberFormat(maxDistance,
				'Maximum Distance') == None:
			return TrainRouteInfo.NO_SUCH_ROUTE

		# initialse routePaths and startNodes as
		# a list with startNode as the passed start stop of the route
		# to be computed. Also intialise the list that will contain
		# computedRoutes

		startNodes = [startNode.upper().strip()]
		routePaths = [startNode.upper().strip()]
		computedRoutes = list()
		stopCount = 0
		routeRepeatCount = 0

		# Loop until all the routes have been traveresed

		while len(startNodes) > 0:

			# Get the possible routes that start with the list of nodes

			possibleRoutes = TrainRouteInfo.computePossibleRoutes(self,
					startNodes)

			# Re-initialise the startNodes for the next iteration

			startNodes = []

			# create a temporary list

			paths = list()

			# Loop through the possible routes that start with
			# nodes in the list startNodes

			for route in possibleRoutes:

				# Loop through routePaths and if the last node of path
				# in routePaths matches with first node of route in
				# possibleRoutes and the distance of the route is less than
				# maxDistance, append it in paths temp list. If the route disccovered
				# is a complete route then append it in the computedRoutes list

				for path in routePaths:
					print startNodes
					pathDistance = TrainRouteInfo.computeDistance(self,
							path + route[1:2])
					if str(pathDistance) \
						!= TrainRouteInfo.NO_SUCH_ROUTE and path[-1] \
						== route[0:1] and pathDistance < maxDistance:
						# Dont duplicate routes
						if path + route[1:2] not in paths:
							paths.append(path + route[1:2])
							startNodes.append(route[1:2])
						if route[1:2] == endNode.upper().strip():
							# Dont duplicate computed routes
							if path + route[1:2] not in computedRoutes:
								computedRoutes.append(path + route[1:2])

			# Assign the temporary list paths to routePaths
			# after checking for route repeatations and pruning

			routePaths = paths

			# Initialize a list that holds the items to be pruned

			routesToBePruned = list()

			# Check whch items have routes repeated

			for route in routePaths:
				if not TrainRouteInfo.checkForRouteRepeatation(route):
					routesToBePruned.append(route)

			# Prune the items that have repeated routes

			for route in routesToBePruned:
				routePaths.remove(route)

		if len(computedRoutes) > 0:

			# return the length of the list

			return len(computedRoutes)
		else:
			return TrainRouteInfo.NO_SUCH_ROUTE


# Usage
# Create an object by passing the graph input

trainRouteInfo = TrainRouteInfo('AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7')

# Compute distance between routes

print trainRouteInfo.computeDistance('ABC')
print trainRouteInfo.computeDistance('AD')
print trainRouteInfo.computeDistance('ADC')
print trainRouteInfo.computeDistance('AEBCD')
print trainRouteInfo.computeDistance('AED')

# Compute routes

print trainRouteInfo.computeRoutesWithMaxStops('C', 'C', 3)
print trainRouteInfo.computeRoutesWithExactStops('A', 'C', 4)
print trainRouteInfo.computeShortestRoute('A', 'C')
print trainRouteInfo.computeShortestRoute('B', 'B')
print trainRouteInfo.computeRoutesWithMaxDistance('C', 'C', 30)

# Create an object by passing the graph input

trainRouteInfo = \
TrainRouteInfo('AB500,BC400,CD150,DC149,DE600,AD500,CE200,EB300,AE700'
			   )

# Compute distance between routes

print trainRouteInfo.computeDistance('ABC')
print trainRouteInfo.computeDistance('AD')
print trainRouteInfo.computeDistance('ADC')
print trainRouteInfo.computeDistance('AEBCD')
print trainRouteInfo.computeDistance('AED')

# Compute routes

print trainRouteInfo.computeRoutesWithMaxStops('C', 'C', 3)
print trainRouteInfo.computeRoutesWithExactStops('A', 'C', 4)
print trainRouteInfo.computeShortestRoute('A', 'C')
print trainRouteInfo.computeShortestRoute('B', 'B')
print trainRouteInfo.computeRoutesWithMaxDistance('C', 'C', 300)

			