class Calculator():
	#we don't need any other parameters
	#but every class needs an __init__ method
	#creator parameter isn't necessary, just an example of how parameters
	#in init will work
	def __init__(self, creator):
		self.creator = creator

	#addition function
	def add(self, x, y):
		#add 1 to x y # of times
		for i in range(y):
			x=x+1
		return x

	#subtraction function
	def sub(self, x, y):
		#subtract 1 from x y # of times
		for i in range(y):
			x=x-1
		return x

	#multiplication function
	'''if you wanted to add directly to x, the outer loop
	would be for i in range(y-1) since x has already been added to 
	the final value once'''
	def mult(self, x, y):
		#number to return
		retnum = 0
		#add x y number of times
		for i in range(y):
			#here is where we actually add x
			for j in range(x):
				retnum = retnum + 1
		return retnum

	#division function
	'''to find the answer we need to count how many times we subtract
	y from x until x is 0.  ex. x = 15, y = 3 ---> 15-3-3-3-3-3, we
	have subtracted the number three a total of five times from 15'''
	def div(self, x, y):
		#number to return
		subtractCounter = 0
		while(x >= y):
			subtractCounter = subtractCounter + 1
			x = x-y
		return subtractCounter
			
		


#even though self is included in the above function definitions,
#you don't include 'self' when you call the function

#create an instance of the class Calculator which I arbitrarily called 'calcInstance'
#because I included var 'creator' in the init, I pass in some value when I create the instance
#of the class
calcInstance = Calculator("Rachel")

#getting user input
#we use int to turn the user input into an integer rather than the default, string
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))


print("Given ", x, " and ", y)
print()
print("addition is ", calcInstance.add(x, y))
print("subtraction is ", calcInstance.sub(x, y))
print("multiplication is ", calcInstance.mult(x, y))
print("division is ", calcInstance.div(x, y))
print()
print()

#just to demonstrate what I mean by instances I will create multiple instances of calculator
calcOne = Calculator("Lisa")
calcTwo = Calculator("Nick")
calcThree = Calculator("Anna")

print("calcInstance was created by ", calcInstance.creator)
print("calcOne was created by ", calcOne.creator)
print("calcTwo was created by ", calcTwo.creator)
print("calcThree was created by ", calcThree.creator)
