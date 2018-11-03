class Race:
	name = None
	ageRange = [0, 0]
	heightRange = [0, 0]
	weightRange = [0, 0]
	speed = 0
	size = None
	desc = None
	strBonus = 0
	dexBonus = 0
	conBonus = 0
	intBonus = 0
	wisBonus = 0
	chaBonus = 0
	nameList = None
	classList = None

	def setRandomCommonRace(self):
		self.name = random.choice(commonRaces)
		self.setRaceDetails()
		return

	def setRandomRareRace(self):
		self.name = random.choice(rareRaces)
		self.setRaceDetails()
		return

	def setRandomeGoblinoidRace(self):
		self.name = random.choice(goblinoidRaces)
		self.setRaceDetails()
		return

	def setRaceDetails(self):
		with open('races.csv', mode = 'r') as races:
		racesFile = csv.DictReader(races)
		for record in racesFile:
			if (name.lower() == record["name"].lower()):
				self.ageRange[0] = record["ageRangeL"]
				self.ageRange[1] = record["ageRangeU"]
				self.heightRange[0] = record["heightRangeL"]
				self.heightRange[1] = record["heightRangeU"]
				self.weightRange[0] = record["weightRangeL"]
				self.weightRange[1] = record["weightRangeU"]
				self.speed = record["speed"]
				self.size = record["size"]
				self.desc["desc"]
				break
		return

commonRaces = ["Dwarf", "Elf", "Gnome", "Half elf", "Half orc", "Halfling", "Human"]
rareRaces = []
goblinoidRaces = ["Goblin", "Orc", "Hobgoblin"]

def randomRace():
	roll = Dice.dx(100)
	if(roll <= 90):
		# TODO: move random race to race class
		return random.choice(commonRaces)
	else:
		return random.choice(rareRaces)
