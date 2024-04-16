import tkinter as tk

def printColor(event):
    print(selection.get())

#Create Main Window
root = tk.Tk()
root.title("Main Menu")

#Change background
root.config(bg="black")

#Create Menu labels/buttons and configure colors
newProjectLabel = tk.Label(root, text="Create New Project")
newProjectLabel.config(bg="black")
newProjectLabel.config(fg="white")

#Title input
titleLabel = tk.Label(root, text="Project title: ")
titleLabel.config(bg="black")
titleLabel.config(fg="white")
titleInput = tk.Entry(root)

#Author input
authorLabel = tk.Label(root, text="Author name: ")
authorLabel.config(bg="black")
authorLabel.config(fg="white")
authorInput = tk.Entry(root)

#Color selection
colorLabel = tk.Label(root, text="Color Theme")
colorLabel.config(bg="black")
colorLabel.config(fg="white")
selection = tk.StringVar(root)
selection.set("White")
options = ["White", "Black", "Red", "Green", "Blue"]
colorInput = tk.OptionMenu(root, selection, *options, command=printColor)

createButton = tk.Button(root, text="Create")

whitespace = tk.Label(root, text="")
whitespace.config(bg="black")

newProjectLabel.grid(row=1, column=0)
titleLabel.grid(row=2, column=0)
titleInput.grid(row=2, column=1)
authorLabel.grid(row=3, column=0)
authorInput.grid(row=3, column=1)
colorLabel.grid(row=4, column=0)
colorInput.grid(row=4, column=1)
createButton.grid(row=5, column=0)
whitespace.grid(row=6, column=0)

openExistingLabel = tk.Label(root, text="Open Existing Proejct")
openExistingLabel.config(bg="black")
openExistingLabel.config(fg="white")

openButton = tk.Button(root, text="Browse")
openExistingLabel.grid(row=6, column=0)
openButton.grid(row=7, column=0)



root.mainloop()