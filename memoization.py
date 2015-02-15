def memo(f):
	"""Decorator that catches the return value for each call to f(args).
	Then when called again with same args, we can just look it up."""
	cache = {}
	def _f(*args):
		print ("[", args, "] ==> ", end="")
		print (cache)
		try:
			return cache[args]
		except KeyError:
			cache[args] = result = f(*args)
			return result
		except TypeError:
			# some element of args can't be a dict key
			return f(args)

	return _f

@memo
def fib(n):
	if (n <= 1):
		return 1
	else:
		return fib(n-1) + fib(n-2)

## this example is taken from Udacity - cs101
print (fib(4))
print (fib(4))