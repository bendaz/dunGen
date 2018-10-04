# import Weapon
# import Armor
import CharacterDef
import Dice

class Character:
	# General info
	isNPC = None
	name = None
	alignment = None
	characterClass = None
	level = 0
	diety = None
	homeland = None
	race = None
	size = None
	gender = None
	age = None
	heightFt = 0
	heightIn = 0
	weight = 0
	hair = None
	eyes = None
	speed = {"base": 0,
			 "withArmor": 0,
			 "fly": 0,
			 "swim": 0,
			 "climb": 0,
			 "burrow": 0}
	# Non character sheet
	homeCity = None
	backstory = None
	occupation = None
	# Attributes
	strength = {"score": 0,
				"mod": 0,
				"tempScore": 0,
				"tempMod": 0}
	dexterity = {"score": 0,
				"mod": 0,
				"tempScore": 0,
				"tempMod": 0}
	constitution = {"score": 0,
				"mod": 0,
				"tempScore": 0,
				"tempMod": 0}
	intelligence = {"score": 0,
				"mod": 0,
				"tempScore": 0,
				"tempMod": 0}
	wisdom = {"score": 0,
				"mod": 0,
				"tempScore": 0,
				"tempMod": 0}
	charisma = {"score": 0,
				"mod": 0,
				"tempScore": 0,
				"tempMod": 0}
	hp = {"max": 0, "current": 0, "nonlthlDmg": 0}
	initiative = 0
	ac = {"base": 0, "touch": 0, "ff": 0}
	fortSave = {"tot": 0, "base": 0, "abilityMod": 0, "magicMod": 0, "miscMod": 0, "tempMod": 0}
	refSave = {"tot": 0, "base": 0, "abilityMod": 0, "magicMod": 0, "miscMod": 0, "tempMod": 0}
	willSave = {"tot": 0, "base": 0, "abilityMod": 0, "magicMod": 0, "miscMod": 0, "tempMod": 0}
	bab = 0
	cmb = 0
	cmd = 0
	spellResist = 0
	# Skills
	skillPoints = 0
	acrobatics = {"classSkill": False, "total": 0, "attribute": 2, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	appraise = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	bluff = {"classSkill": False, "total": 0, "attribute": 6, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	climb = {"classSkill": False, "total": 0, "attribute": 1, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	craft1 = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	craft2 = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	craft3 = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	diplomacy = {"classSkill": False, "total": 0, "attribute": 6, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	disableDevice = {"classSkill": False, "total": 0, "attribute": 2, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	disguise = {"classSkill": False, "total": 0, "attribute": 6, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	escapeArtist = {"classSkill": False, "total": 0, "attribute": 2, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	fly = {"classSkill": False, "total": 0, "attribute": 2, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	handleAnimal = {"classSkill": False, "total": 0, "attribute": 6, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	heal = {"classSkill": False, "total": 0, "attribute": 5, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	intimidate = {"classSkill": False, "total": 0, "attribute": 6, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgeArcana = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgeDungeoneering = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgeEngineering = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgeGeography = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgeHistory = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgeLocal = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgeNature = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgeNobility = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgePlanes = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	knowledgeReligion = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	linguistics = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	perception = {"classSkill": False, "total": 0, "attribute": 5, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	perform1 = {"classSkill": False, "total": 0, "attribute": 6, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	perform2 = {"classSkill": False, "total": 0, "attribute": 6, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	profession1 = {"classSkill": False, "total": 0, "attribute": 5, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	profession2 = {"classSkill": False, "total": 0, "attribute": 5, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	ride = {"classSkill": False, "total": 0, "attribute": 2, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	senseMotive = {"classSkill": False, "total": 0, "attribute": 5, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	sleightOfHand = {"classSkill": False, "total": 0, "attribute": 2, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	spellcraft = {"classSkill": False, "total": 0, "attribute": 4, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	stealth = {"classSkill": False, "total": 0, "attribute": 2, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	survival = {"classSkill": False, "total": 0, "attribute": 5, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	swim = {"classSkill": False, "total": 0, "attribute": 1, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	useMagicDevice = {"classSkill": False, "total": 0, "attribute": 6, "abilityMod": 0, "ranks": 0, "miscMod": 0}
	languages = {}
	# Feats and abilities
	feats = {}
	specialAbilities = {}
	# Spells
	domainSchool = None
	lvl0Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl1Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl2Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl3Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl4Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl5Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl5Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl6Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl7Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl8Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	lvl9Spells = {"numSpellsKnown":0, "spellsKnown": {}, "saveDC": 0, "spellsPerDay": 0, "bonusSpells": 0}
	# Equipment
	# Weapons
	weapon1 = None
	weapon2 = None
	weapon3 = None
	weapon4 = None
	weapon5 = None
	# AC Items
	armor1 = None
	armor2 = None
	armor3 = None
	armor4 = None
	armor5 = None
	# Gear
	gear = {}
	carryWeight = 0
	weightLimit = {"ltLoad": 0,
					"medLoad": 0,
					"hvyLoad": 0,
					"liftOverHead": 0,
					"lifOffGround": 0,
					"drag": 0}
	# Money
	totalMoney = 0
	currency = {"CP": 0, "SP": 0, "GP": 0, "PP": 0}
	# XP
	xp = 0

	# Member functions
	def setRace(self, inRace = None):
		if(self.race == None):
			if(inRace != None):
				self.race = inRace
			else:
				self.race = randomRace()
	
	def randomRace():
		roll = Dice.dx(100)
		if(roll <= 90):
			# TODO: move random race to race class
			return random.choice(CharacterDef.commonRaces)
		else:
			return random.choice(CharacterDef.rareRaces)

	def setSize(self):
		self.size = self.race.size

	def setAge(self, inAge = None):
		if(inAge != None):
			self.age = inAge
		else:
			self.age = randomAge(self)
			
	def randomAge(self):
		ageRange = self.race.ageRange
		return randint(ageRange[0], ageRange[1])

	def setHeight(self, inFeet = None, inInches = None):
		if(inInches != None or inFeet != None):
			heightRange = self.race.heightRange
			totalInches = randint(heightRange[0], heightRange[1])
			if(inInches != None and inFeet != None):
				self.heightFt = totalInches / 12
				self.heightIn = totalInches % 12
			else if(inInches != None and inFeet == None):
				self.heightFt = totalInches / 12
				self.heightIn = inInches
			else
				self.heightFt = inFeet
				self.heightIn = totalInches % 12
		else:
			self.heightFt = inFeet
			self.heightIn = inInches

	def setWeight(self, inWeight = None):
		if(inWeight != None):
			self.weight = inWeight
		else:
			self.randomWeight(self)

	def randomWeight(self):
		weightRange = self.weight.weightRange
		return randint(weightRange[0],weightRange[1])

	def setHair(self, inHair = None):
		if(inHair != None):
			self.hair = inHair
		else:
			self.hair = randomHair(self)

	def randomHair(self):
		return random.choice(self.race.hair)

	def setEyes(self, inEyes):
		if(inEyes != None):
			self.eyes = inEyes
		else:
			self.eyes = randomEyes(self)

	def randomEyes(self):
		return random.choice(self.race.eyes)

	def setSpeed(self):
		self.speed = self.race.speed

	def setGender(self, inGender):
		if(inGender != None):
			self.gender = inGender
		else:
			self.gender = random.choice(["M", "F"])
