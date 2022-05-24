#for x in range(4):
#	print "for", x, "in range(4):"
#	pass

print "kkkkkkkkkk"

class Car:
	"""docstring for ClassName"""
	def __init__(self, model, color):
		self.model = model
		self.color = color

		self.start()

	def start(self):

		print(self.model + ", has started")
		pass

mycar = Car("BMW","red")
print mycar

def myFunc(a):
	return len(a)
	pass

x = map(myFunc,('apple','orange','banana'))

print x

print(list(x))