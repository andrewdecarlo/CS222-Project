


import tkinter as tk



root = tk.Tk()


root.title("Main Menu")

#Change background
root.config(bg="black")




#Create Menu labels/buttons and configure colors
newProjectLabel = tk.Label(root, text="Create New Project")
newProjectLabel.config(bg="black")
newProjectLabel.config(fg="white")

titleLabel = tk.Label(root, text="Project title: ")
titleLabel.config(bg="black")
titleLabel.config(fg="white")
titleInput = tk.Entry(root)

authorLabel = tk.Label(root, text="Author name: ")
authorLabel.config(bg="black")
authorLabel.config(fg="white")
authorInput = tk.Entry(root)

createButton = tk.Button(root, text="Create", HomePageStart(authorInput.get(), titleInput.get()) )

whitespace = tk.Label(root, text="")
whitespace.config(bg="black")

newProjectLabel.grid(row=1, column=0)
titleLabel.grid(row=2, column=0)
titleInput.grid(row=2, column=1)
authorLabel.grid(row=3, column=0)
authorInput.grid(row=3, column=1)
createButton.grid(row=4, column=0)
whitespace.grid(row=5, column=0)

openExistingLabel = tk.Label(root, text="Open Existing Proejct")
openExistingLabel.config(bg="black")
openExistingLabel.config(fg="white")

openButton = tk.Button(root, text="Browse")
openExistingLabel.grid(row=6, column=0)
openButton.grid(row=7, column=0)


home = HomePageStart(titleInput.get(), authorInput.get())

print("1")
root.mainloop()







