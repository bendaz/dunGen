import Item

class Shop:
	randomize = None
	city = None
	name = None
	owner = None
	shopType = None
	inventory = None

	# TODO: randomize city, name, owner
	def __init__(self, randomize, city = None, name = None, owner = None, shopType = None, inventory = None):
		self.city = city
		self.name = name
		self.owner = owner
		self.shopType = shopType
		self.inventory = inventory

		if (randomize.lower() == 'y'):
			if (city == None):
				pass
			if (name == None):
				pass
			if (owner == None):
				pass
			if (shopType == None):
				self.shopType == random.choose(shopTypes)
			if (inventory == None):
				if (shopType == 'general'):
					self.inventory = Item.getItemsOfType('gear')
				elif (shopType == 'blacksmith'):
					self.inventory = Item.getItemsOfType('weapons') + Item.getItemsOfType('armor')
				elif (shopType == 'stable'):
					self.inventory = Item.getItemsOfType('stable')
				elif (shopType == 'armorer'):
					self.inventory = Item.getItemsOfType('armor')
				elif (shopType == 'weaponsmith'):
					self.inventory = Item.getItemsOfType('weapons')
				elif (shopType == 'dock'):
					self.inventory = Item.getItemsOfType('boat')
				else:
					self.inventory = getAllItems()
	return

	#Takes a list of itemTypes to be included in the inventory
	def buildInventory(itemTypes):
		for itemType in itemTypes:
			self.inventory.extend(Item.getItemsOfType(itemType))

shopTypes = ['general', 'blacksmith', 'stable', 'armorer', 'weaponsmith', 'dock']

