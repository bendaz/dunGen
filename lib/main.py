from appJar import gui

def launch(id):
	if (id == "itemsButton"):
		app.showSubWindow("Items")
	else:
		pass

app = gui("dunGen")

# Define main window
app.addImage("itemsButton", "imgs/itemsButton.gif")
app.setImageSubmitFunction("itemsButton", launch)

# Define items window
resourcesMenu = ["Item Dictionary"]
app.startSubWindow("Items", modal=True)
app.setSize(500,400)
app.addMenuList(Resources)
app.addLabel("itemWindowLabel", "Items")
app.stopSubWindow()

app.go()