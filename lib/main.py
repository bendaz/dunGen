from appJar import gui
import Item
import Character

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
app.startSubWindow("Character", modal=True)
app.setSize(800,400)


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