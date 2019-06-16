import random

class CharacterClass:
	statAlloOrder = None
	numberHitDice = 1
	hitDie = 1

	def __init__(self, inStatAlloOrder = None, inNumberHitDice = None, inHitDie = None):
		self.statAlloOrder = inStatAlloOrder
		self.numberHitDice = inNumberHitDice
		self.hitDie = inHitDie
		return

#These are valid orders for stat allocation
#TODO: Move to an external file to be customizable
BarbAlloList = [
					["str", "con", "dex", "wis", "int", "cha"],
					["str", "dex", "con", "wis", "int", "cha"]
				]
BardAlloList = [
					["cha", "dex", "int", "wis", "con", "str"]
				]
ClericAlloList = [
					["wis", "con", "str", "cha", "dex", "int"],
					["wis", "str", "con", "cha", "dex", "int"]
				]
DruidAlloList = [
					["wis", "dex", "con", "int", "cha", "str"]
				]
FighterAlloList = [
					["str", "con", "dex", "int", "cha", "wis"],
					["dex", "con", "str", "int", "cha", "wis"]
				]
MonkAlloList = [
					["dex", "con", "wis", "int", "cha", "str"]
				]
PaladinAlloList = [
					["str", "cha", "con", "dex", "wis", "int"],
					["str", "con", "cha", "dex", "wis", "int"]
				]
RangerAlloList = [
					["dex", "int", "wis", "con", "str", "cha"]
				]

RogueAlloList = [
					["dex", "int", "cha", "con", "wis", "str"],
					["int", "dex", "cha", "con", "wis", "str"]
				]
SorcererAlloList = [
					["cha", "dex", "con", "int", "wis", "str"]	
				]
WizardAlloList = [
					["int", "dex", "con", "wis", "cha", "str"]
				]

Barbarian = CharacterClass(inStatAlloOrder = random.choice(BarbAlloList), 
	inNumberHitDice = 1, inHitDie = 12)
Bard = CharacterClass(inStatAlloOrder = random.choice(BardAlloList),
	inNumberHitDice = 1, inHitDie = 8)
Cleric = CharacterClass(inStatAlloOrder = random.choice(ClericAlloList),
	inNumberHitDice = 1, inHitDie = 8)
Druid = CharacterClass(inStatAlloOrder = random.choice(DruidAlloList),
	inNumberHitDice = 1, inHitDie = 8)
Fighter = CharacterClass(inStatAlloOrder = random.choice(FighterAlloList),
	inNumberHitDice = 1, inHitDie = 10)
Monk = CharacterClass(inStatAlloOrder = random.choice(MonkAlloList),
	inNumberHitDice = 1, inHitDie = 8)
Paladin = CharacterClass(inStatAlloOrder = random.choice(PaladinAlloList),
	inNumberHitDice = 1, inHitDie = 10)
Ranger = CharacterClass(inStatAlloOrder = random.choice(RangerAlloList),
	inNumberHitDice = 1, inHitDie = 10)
Rogue = CharacterClass(inStatAlloOrder = random.choice(RogueAlloList),
	inNumberHitDice = 1, inHitDie = 8)
Sorcerer = CharacterClass(inStatAlloOrder = random.choice(SorcererAlloList),
	inNumberHitDice = 1, inHitDie = 6)
Wizard = CharacterClass(inStatAlloOrder = random.choice(WizardAlloList),
	inNumberHitDice = 1, inHitDie = 6)

commonClasses = [Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger,
	Rogue, Sorcerer, Wizard]
commonClassesNames = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
	"Paladin", "Ranger", "Rogue", "Sorcerer", "Wizard"]
#advancedClasses = [Alchemist, Antipaladin, Cavalier, Inquisitor, Oracle, Summoner, Witch]
