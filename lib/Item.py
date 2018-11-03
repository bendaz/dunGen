import csv
import random

class Item:
	name = None
	cost = 0
	weight = 0
	isMagical = False
	shortDesc = None
	longDesc = None
	itemType = None
	weaponClass = None
	weaponType = None
	wieldType = None
	damageS = None
	damageM = None
	damageType = None
	critMult = 0
	critMin = 20
	special = None
	armorType = None
	acBonus = 0
	maxDex = None
	checkPenalty = 0
	spellFailure = 0

	def __init__(self, record = None):
		if (record != None):
			self.name = record["name"]
			self.cost = record["cost"]
			self.weight = record["weight"]
			self.isMagical = record["isMagical"]
			self.shortDesc = record["shortDesc"]
			self.longDesc = record["longDesc"]
			self.itemType = record["itemType"]
			self.itemType = record["weaponClass"]
			self.itemType = record["weaponType"]
			self.itemType = record["wieldType"]
			self.itemType = record["damageS"]
			self.itemType = record["damageM"]
			self.itemType = record["damageType"]
			self.itemType = record["critMult"]
			self.itemType = record["critMin"]
			self.itemType = record["special"]
			self.itemType = record["armorType"]
			self.itemType = record["acBonus"]
			self.itemType = record["maxDex"]
			self.itemType = record["checkPenalty"]
			self.itemType = record["spellFailure"]
		else:
			return
		return
		
# When adding to this, add logic to getItemsOfType method
itemTypes = ['gear', 'stable', 'clothes', 'boat', 'weapons', 'armor', 'simpleWeapons', 'martialWeapons', 'exoticWeapons']

def getItem(self, name):
	with open('items.csv', mode = 'r') as items:
		itemsFile = csv.DictReader(items)
		for record in itemsFile:
			if (name.lower() == record["name"].lower()):
				tempItem = Item(record)
				break
	return tempItem

def randomItem(minValue, maxValue):
	with open('items.csv', mode = 'r') as items:
		itemsFile = csv.DictReader(items)
		tempList = []
		for record in itemsFile:
			if (minValue <= float(record["cost"]) <= maxValue):
				tempItem = Item(record)
				tempList.append(tempItem)

	return random.choice(tempList)	

def getItemsOfType(itemType):
	returnList = []
	if (itemType not in itemTypes):
		return
	if (itemType == 'gear'):
		with open('items.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				if (record["itemType"] == itemType):
					tempItem = Item(record)
					returnList.append(tempItem)
		return returnList
	elif (itemType == 'stable'):
		with open('items.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				if (record["itemType"] == itemType):
					tempItem = Item(record)
					returnList.append(tempItem)
		return returnList
	elif (itemType == 'clothes'):
		with open('items.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				if (record["itemType"] == itemType):
					tempItem = Item(record)
					returnList.append(tempItem)
		return returnList
	elif (itemType == 'boat'):
		with open('items.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				if (record["itemType"] == itemType):
					tempItem = Item(record)
					returnList.append(tempItem)
		return returnList
	elif (itemType == 'weapons'):
		with open('weapons.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				if (record["itemType"] == itemType):
					tempItem = Item(record)
					returnList.append(tempItem)
		return returnList
	elif (itemType == 'armor'):
		with open('armor.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				if (record["itemType"] == itemType):
					tempItem = Item(record)
					returnList.append(tempItem)
		return returnList
	elif (itemType == 'simpleWeapons'):
		with open('weapons.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				if ((record["itemType"] == "weapons") and (record["weaponClass"] == 'simple')):
					tempItem = Item(record)
					returnList.append(tempItem)
		return returnList
	elif (itemType == 'martialWeapons'):
		with open('weapons.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				if ((record["itemType"] == "weapons") and (record["weaponClass"] == 'martial')):
					tempItem = Item(record)
					returnList.append(tempItem)
		return returnList
	elif (itemType == 'exoticWeapons'):
		with open('weapons.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				if ((record["itemType"] == "weapons") and (record["weaponClass"] == 'exotic')):
					tempItem = Item(record)
					returnList.append(tempItem)
		return returnList

def getAllItems(include = None):
	returnList = []
	if ((include == None) or ('items' in include)):
		with open('items.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				tempItem = Item(record)
				returnList.append(tempItem)
	if ((include == None) or ('weapon' in include)):
		with open('weapons.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				tempItem = Item(record)
				returnList.append(tempItem)
	if ((include == None) or ('armor' in include)):
		with open('armor.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				tempItem = Item(record)
				returnList.append(tempItem)
	return returnList

def addItem(name, cost, weight, isMagical, shortDesc, longDesc, itemType, weaponClass, weaponType, wieldType, \
		damageS, damageM, damageType, critMult, critMin, special, armorType, acBonus, maxDex, checkPenalty, spellFailure):
	if (itemType.lower() != 'weapon' and itemType.lower() != 'armor'):
		with open('items.csv', mode = 'a') as items:
			fieldNames = ['name', 'cost', 'weight', 'isMagical', 'shortDesc', 'longDesc', 'itemType', 'weaponClass', 'weaponType', 'wieldType', \
				'damageS', 'damageM', 'damageType', 'critMult', 'critMin', 'special', 'armorType', 'acBonus', 'maxDex', 'checkPenalty', 'spellFailure']
			writer = csv.DictWriter(items, fieldnames=fieldNames)
			writer.writerow({'name': name, 'cost': cost, 'weight': weight, 'isMagical': isMagical, 'shortDesc': shortDesc, 'longDesc': longDesc, 'itemType': itemType, \
				'weaponClass': weaponClass, 'weaponType': weaponType, 'wieldType': wieldType, 'damageS': damageS, 'damageM': damageM, 'damageType': damageType, \
				'critMult': critMult, 'critMin': critMin, 'special': special, 'armorType': armorType, 'acBonus': acBonus, 'maxDex': maxDex, 'checkPenalty': checkPenalty, \
				'spellFailure': spellFailure})
	elif (itemType.lower() == 'weapon'):
		with open('weapons.csv', mode = 'a') as items:
			fieldNames = ['name', 'cost', 'weight', 'isMagical', 'shortDesc', 'longDesc', 'itemType', 'weaponClass', 'weaponType', 'wieldType', \
				'damageS', 'damageM', 'damageType', 'critMult', 'critMin', 'special', 'armorType', 'acBonus', 'maxDex', 'checkPenalty', 'spellFailure']
			writer = csv.DictWriter(items, fieldnames=fieldNames)
			writer.writerow({'name': name, 'cost': cost, 'weight': weight, 'isMagical': isMagical, 'shortDesc': shortDesc, 'longDesc': longDesc, 'itemType': itemType, \
				'weaponClass': weaponClass, 'weaponType': weaponType, 'wieldType': wieldType, 'damageS': damageS, 'damageM': damageM, 'damageType': damageType, \
				'critMult': critMult, 'critMin': critMin, 'special': special, 'armorType': armorType, 'acBonus': acBonus, 'maxDex': maxDex, 'checkPenalty': checkPenalty, \
				'spellFailure': spellFailure})
	elif (itemType.lower() == 'armor'):
		with open('armor.csv', mode = 'a') as items:
			fieldNames = ['name', 'cost', 'weight', 'isMagical', 'shortDesc', 'longDesc', 'itemType', 'weaponClass', 'weaponType', 'wieldType', \
				'damageS', 'damageM', 'damageType', 'critMult', 'critMin', 'special', 'armorType', 'acBonus', 'maxDex', 'checkPenalty', 'spellFailure']
			writer = csv.DictWriter(items, fieldnames=fieldNames)
			writer.writerow({'name': name, 'cost': cost, 'weight': weight, 'isMagical': isMagical, 'shortDesc': shortDesc, 'longDesc': longDesc, 'itemType': itemType, \
				'weaponClass': weaponClass, 'weaponType': weaponType, 'wieldType': wieldType, 'damageS': damageS, 'damageM': damageM, 'damageType': damageType, \
				'critMult': critMult, 'critMin': critMin, 'special': special, 'armorType': armorType, 'acBonus': acBonus, 'maxDex': maxDex, 'checkPenalty': checkPenalty, \
				'spellFailure': spellFailure})
	return
