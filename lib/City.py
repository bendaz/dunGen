class City:
	kingdom = None
	name = None
	isCapital = False
	pop = 0
	area = 0
	popDensity = 0
	numInns = 0
	inns = []
	numGenStores = 0
	genStores = []
	numBlacksmiths = 0
	blacksmiths = []
	numApothecaries = 0
	apothecaries = []
	numMagicShops = 0
	magicShops = []
	#hasKing
	#king
	#numDukes
	#dukes

	def __init__(self, name, pop, area):
		self.name = name
		self.pop = pop
		self.area = area
		self.popDensity = float(pop) / float(area)
