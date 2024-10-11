import cProfile, pstats, io

def profile(function):

	'''A decorator that uses cProfile to profile a function's runtime'''

	def inner(*args, **kwargs):
		prof = cProfile.Profile()
		prof.enable()
		return_value = function(*args, **kwargs)
		prof.disable()
		string = io.StringIO()
		sortby = 'cumulative'
		stats = pstats.Stats(prof, stream = string).sort_stats(sortby)
		stats.print_stats()
		print(string.getvalue())

		return return_value

	return inner