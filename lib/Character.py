# import Weapon
# import Armor
import CharacterDef
import Dice
import math

class Character:
	# General info
	isNPC = None
	name = None
	alignment = None
	characterClass = None
	level = 1
	diety = None
	homeland = None
	race = Race()
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
	attributeScores = []
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
	def __init__():

	def setCharacterRace(self, inRace = None):
		if(self.race == None):
			if(inRace != None):
				self.race = inRace
				self.race.setRaceDetails()
			else:
				self.race.setRandomCommonRace()
		return

	def setName(self, inName = None):
		if (inName == None):
			self.name = self.setRandomName()
		else:
			self.name = inName
		return

	def setRandomName(self):
		self.name = random.choose(self.race.nameList)

	def setSize(self, inSize = None):
		if (inSize == None):
			self.size = self.race.size
		else:
			self.size = inSize
		return

	def setAge(self, inAge = None):
		if(inAge == None):
			self.setRandomAge()
		else:
			self.age = inAge
		return
			
	def setRandomAge(self):
		self.age = Dice.gaussian(self.race.ageRange[0].self.race.ageRange[1])
		return

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
		return

	def setWeight(self, inWeight = None):
		if(inWeight == None):
			self.randomWeight()
		else:
			self.weight = inWeight
		return

	def setRandomWeight(self):
		self.weight = Dice.gaussian(self.race.weightRange[0], self.race.weightRange[1])
		return

	def setHair(self, inHair = None):
		if(inHair != None):
			self.hair = inHair
		else:
			self.hair = self.setRandomHair()
		return

	def setRandomHair(self):
		self.hair = random.choice(self.race.hair)
		return

	def setEyes(self, inEyes):
		if(inEyes != None):
			self.eyes = inEyes
		else:
			self.eyes = self.setRandomEyes()
		return

	def setRandomEyes(self):
		self.eyes = random.choice(self.race.eyes)
		return

	def setSpeed(self):
		self.speed["base"] = self.race.speed
		return

	def setGender(self, inGender):
		if(inGender != None):
			self.gender = inGender
		else:
			self.gender = setRandomGender()
		return

	def setRandomGender(self):
		self.gender = random.choice(["M", "F"])
		return

	def setCharacterClass(self, inClass):
		if (inClass == None):
			self.setRandomClass()
		else:
			self.characterClass = inClass
		return

	def setRandomClass(self):
		self.characterClass = random.choice(self.race.classList)
		return

	def setAlignment(self, inAlignment):
		if (inAlignment == None):
			self.setRandomAlignment()
		else:
			self.alignment = inAlignment
		return

	def setRandomAlignment(self):
		self.alignment = random.choose(self.characterClass.alignmentList)
		return

	def setRandomAttributeScores(self):
		self.attributeScores = Dice.rollStatSet()
		return

	def allocateAttributeScores(self):
		tempAtts = self.attributeScores
		for score in range(1,7):
			if (self.characterClass.statAlloOrder[score] = "str"):
				self.strength["score"] = max(tempAtts)
			else if (self.characterClass.statAlloOrder[score] = "dex"):
				self.dexterity["score"] = max(tempAtts)
			else if (self.characterClass.statAlloOrder[score] = "con"):
				self.constitution["score"] = max(tempAtts)
			else if (self.characterClass.statAlloOrder[score] = "int"):
				self.intelligence["score"] = max(tempAtts)
			else if (self.characterClass.statAlloOrder[score] = "wis"):
				self.wisdom["score"] = max(tempAtts)
			else:
				self.charisma["score"] = max(tempAtts)
			tempAtts.remove(max(tempAtts))
		return

	def setAttributeMods(self):
		self.strength["mod"] = calculateAttributeMod(self.strength["score"])
		self.dexterity["mod"] = calculateAttributeMod(self.dexterity["score"])
		self.constitution["mod"] = calculateAttributeMod(self.constitution["score"])
		self.intelligence["mod"] = calculateAttributeMod(self.intelligence["score"])
		self.wisdom["mod"] = calculateAttributeMod(self.wisdom["score"])
		self.charisma["mod"] = calculateAttributeMod(self.charisma["score"])

	def setLevel(self, inlevel = None):
		if (inLevel == None):
			self.level = 1
		else:
			self.level = inLevel

	def setMaxHP(self, inHP = None):
		if (inHP == None):
			self.hp["max"] = self.characterClass.hitDie + self.constitution["mod"]			else:
			for i in range(1, level):
				roll = Dice.dx(self.characterClass.hitDie)
				if (roll > ((self.characterClass.hitDie / 2) + 1))
					roll = (self.characterClass.hitDie / 2) + 1
				self.hp["max"] = roll + self.constitution["mod"]
		else:
			self.hp["max"] = inHP

def calculateAttributeMod(score):
	return (math.floor(score / 2) - 5)
