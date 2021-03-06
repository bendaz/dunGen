from appJar import gui
import Item
import Character
import CharacterClass
import Common
import Race

def launch(id):
	if (id == "itemsButton"):
		app.showSubWindow("Items")
	elif (id == "characterButton"):
		app.showSubWindow("Character")
	else:
		pass

def updateItemTypeListBox():
	app.clearListBox("items",callFunction=False)
	returnedList = app.getListBox("itemTypes")

	for itemType in returnedList:
		index = tempItem.itemTypesXref.index(itemType)
		itemTypeList = Item.getItemsOfType(tempItem.itemTypes[index])

		for item in itemTypeList:
			app.addListItem("items",Item.getItem(item.name).name)

	return

def updateItemListBox():
	app.clearLabel("name")
	app.clearLabel("shortDesc")
	app.clearMessage("longDesc")

	tempItem = Item.getItem(app.getListBox("items")[0])

	app.setLabel("name",tempItem.name)
	app.setLabel("shortDesc",tempItem.shortDesc)
	app.setMessage("longDesc",tempItem.longDesc)

	return

app = gui("dunGen")

# Define main window
mainMenuNames = ["itemsButton", "characterButton"]
app.addToolbar(mainMenuNames, launch, findIcon=True)

#########################
# Define character window
#########################

# Set up the window
app.startSubWindow("Character", modal=True)

# Get info needed for character creation window
(commonRaces,rareRaces,goblinoidRaces) = Race.getRacesLists()
allRaceList = (commonRaces + rareRaces + goblinoidRaces)
allRaceList.sort()
allRaceList.insert(0, "-Race-")

allClassList = CharacterClass.commonClassesNames
allClassList.insert(0, "-Class-")

alignmentList = ["-Align-", "LG", "LN", "LE", "NG", "N", "NE", "CG", "CN", "CE"]

Common.sizeList.insert(0, "-Size-")

# Display character creation fields
# Row, Col, Colspan, Rowspan
app.setPadding([10,5])

app.setSticky("ew")	
app.addEntry("nameField", 1, 1, 4)
app.setEntryDefault("nameField", "Name")

app.addEntry("ageField", 1, 7, 2)
app.setEntryDefault("ageField", "Age")

app.addOptionBox("genderField", ["-Sex-","M","F"], 1, 5, 2)

app.addOptionBox("alignmentField", alignmentList, 2, 7, 2)

app.setSticky("w")
app.addOptionBox("sizeField", (Common.sizeList), 2, 3, 2)

app.setSticky("ew")
app.addOptionBox("raceField", (allRaceList), 2, 1, 2)

app.setSticky("e")
app.addLabel("levelLabel", "Lvl:", 3, 1, 1)
app.setLabelAlign("levelLabel", "right")
app.setSticky("w")
app.addSpinBoxRange("levelField", 1, 20, 3, 2, 1)
app.setSpinBoxWidth("levelField", 5)

app.setSticky("ew")
app.addOptionBox("classField", allClassList, 3, 3, 2)

app.setSticky("ew")
app.addLabel("heightLabel", "Height (ft/in)", 7, 1, 2)
app.setSticky("w")
app.setLabelAlign("heightLabel", "center")
app.addSpinBoxRange("heightFtField", 0, 100, 8, 1, 1)
app.setSpinBoxWidth("heightFtField", 3)
app.addSpinBoxRange("heightInField", 0, 11, 8, 2, 1)
app.setSpinBoxWidth("heightInField", 3)

app.setSticky("ew")
app.addEntry("hairField", 3, 5, 2)
app.setEntryDefault("hairField", "Hair")

app.addEntry("eyesField", 3, 7, 2)
app.setEntryDefault("eyesField", "Eyes")

app.addEntry("speedField", 2, 5, 2)
app.setEntryDefault("speedField", "Speed")

app.stopSubWindow()

#########################
# Define items window
#########################
tempItem = Item.Item()
itemsList = []

# Set up the window
resourcesMenu = ["Item Dictionary"]
app.startSubWindow("Items", modal=True)
app.setSize(800,400)

# Item types box
app.startFrame("itemTypesFrame",row=0,column=0)
app.setSticky("nesw")
app.setStretch("both")
app.addListBox("itemTypes",tempItem.itemTypesXref,0,0)
app.setListBoxMulti("itemTypes",multi=True)
app.setListBoxChangeFunction("itemTypes",updateItemTypeListBox)
app.stopFrame()

# Items list box
app.startFrame("itemsFrame",row=0,column=1)
app.setSticky("nesw")
app.setStretch("both")
app.addListBox("items",[],0,1)
app.setListBoxGroup("itemTypes", group=True)
app.setListBoxGroup("items", group=True)
app.setListBoxChangeFunction("items",updateItemListBox)
app.stopFrame()

# Item view boxes
app.startFrame("detailsFrame",row=0,column=2)
app.setStretch("both")
app.setSticky("nesw")
app.addLabel("name","")
app.addLabel("shortDesc","")
app.addEmptyMessage("longDesc")
app.stopFrame()

app.stopSubWindow()

app.go()