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

def getItem(self, name):
	with open('items.csv', mode = 'r') as items:
		itemsFile = csv.DictReader(items)
		for record in itemsFile:
			if (name.lower() == record["name"].lower()):
				self.name = record["name"]
				self.cost = float(record["cost"])
				self.weight = float(record["weight"])
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
				self.itemType = int(record["acBonus"])
				self.itemType = int(record["maxDex"])
				self.itemType = int(record["checkPenalty"])
				self.itemType = float(record["spellFailure"])
				break
	return

def randomItem(self, minValue, maxValue):
	with open('items.csv', mode = 'r') as items:
		itemsFile = csv.DictReader(items)
		tempList = []
		for record in itemsFile:
			if (minValue <= float(record["cost"]) <= maxValue):
				tempItem = Item()
				tempItem.name = record["name"]
				tempItem.cost = record["cost"]
				tempItem.weight = record["weight"]
				tempItem.isMagical = record["isMagical"]
				tempItem.shortDesc = record["shortDesc"]
				tempItem.longDesc = record["longDesc"]
				tempItem.itemType = record["itemType"]
				tempItem.itemType = record["weaponClass"]
				tempItem.itemType = record["weaponType"]
				tempItem.itemType = record["wieldType"]
				tempItem.itemType = record["damageS"]
				tempItem.itemType = record["damageM"]
				tempItem.itemType = record["damageType"]
				tempItem.itemType = record["critMult"]
				tempItem.itemType = record["critMin"]
				tempItem.itemType = record["special"]
				tempItem.itemType = record["armorType"]
				tempItem.itemType = record["acBonus"]
				tempItem.itemType = record["maxDex"]
				tempItem.itemType = record["checkPenalty"]
				tempItem.itemType = record["spellFailure"]
				tempList.append(tempItem)

		randItem = random.choice(tempList)	
	return

def getAllItems(include = None):
	returnList = []
	if ((include == None) or ('items' in include)):
		with open('items.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				tempItem = Item()
				tempItem.name = record["name"]
				tempItem.cost = record["cost"]
				tempItem.weight = record["weight"]
				tempItem.isMagical = record["isMagical"]
				tempItem.shortDesc = record["shortDesc"]
				tempItem.longDesc = record["longDesc"]
				tempItem.itemType = record["itemType"]
				tempItem.itemType = record["weaponClass"]
				tempItem.itemType = record["weaponType"]
				tempItem.itemType = record["wieldType"]
				tempItem.itemType = record["damageS"]
				tempItem.itemType = record["damageM"]
				tempItem.itemType = record["damageType"]
				tempItem.itemType = record["critMult"]
				tempItem.itemType = record["critMin"]
				tempItem.itemType = record["special"]
				tempItem.itemType = record["armorType"]
				tempItem.itemType = record["acBonus"]
				tempItem.itemType = record["maxDex"]
				tempItem.itemType = record["checkPenalty"]
				tempItem.itemType = record["spellFailure"]
				returnList.append(tempItem)
	if ((include == None) or ('weapon' in include)):
		with open('weapons.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				tempItem = Item()
				tempItem.name = record["name"]
				tempItem.cost = record["cost"]
				tempItem.weight = record["weight"]
				tempItem.isMagical = record["isMagical"]
				tempItem.shortDesc = record["shortDesc"]
				tempItem.longDesc = record["longDesc"]
				tempItem.itemType = record["itemType"]
				tempItem.itemType = record["weaponClass"]
				tempItem.itemType = record["weaponType"]
				tempItem.itemType = record["wieldType"]
				tempItem.itemType = record["damageS"]
				tempItem.itemType = record["damageM"]
				tempItem.itemType = record["damageType"]
				tempItem.itemType = record["critMult"]
				tempItem.itemType = record["critMin"]
				tempItem.itemType = record["special"]
				tempItem.itemType = record["armorType"]
				tempItem.itemType = record["acBonus"]
				tempItem.itemType = record["maxDex"]
				tempItem.itemType = record["checkPenalty"]
				tempItem.itemType = record["spellFailure"]
				returnList.append(tempItem)
	if ((include == None) or ('armor' in include)):
		with open('armor.csv', mode = 'r') as items:
			itemsFile = csv.DictReader(items)
			for record in itemsFile:
				tempItem = Item()
				tempItem.name = record["name"]
				tempItem.cost = record["cost"]
				tempItem.weight = record["weight"]
				tempItem.isMagical = record["isMagical"]
				tempItem.shortDesc = record["shortDesc"]
				tempItem.longDesc = record["longDesc"]
				tempItem.itemType = record["itemType"]
				tempItem.itemType = record["weaponClass"]
				tempItem.itemType = record["weaponType"]
				tempItem.itemType = record["wieldType"]
				tempItem.itemType = record["damageS"]
				tempItem.itemType = record["damageM"]
				tempItem.itemType = record["damageType"]
				tempItem.itemType = record["critMult"]
				tempItem.itemType = record["critMin"]
				tempItem.itemType = record["special"]
				tempItem.itemType = record["armorType"]
				tempItem.itemType = record["acBonus"]
				tempItem.itemType = record["maxDex"]
				tempItem.itemType = record["checkPenalty"]
				tempItem.itemType = record["spellFailure"]
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
	