import tkinter as tk
from tkinter import *

def homePage():
    entryData = []
   
    root = tk.Tk()
    
    root.title("Main Menu")

    #Change background
    root.config(bg="black")

    #Create Menu labels/buttons and configure colors
    newProjectLabel = tk.Label(root, text="Create New Project:")
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
    
    colorLabel = tk.Label(root, text="Color Theme")
    colorLabel.config(bg="black")
    colorLabel.config(fg="white")
    colorSelection = tk.StringVar(root)
    colorSelection.set("White")
    options = ["White", "Black", "Red", "Green", "Blue"]
    colorInput = tk.OptionMenu(root, colorSelection, *options)

    createButton = tk.Button(root, text="Create", command= lambda: getEntryFields(root,titleInput.get(),authorInput.get(),entryData, colorSelection.get()))
    driverButton = tk.Button(root, text="Driver", command= lambda: Driver())

    whitespace = tk.Label(root, text="")
    whitespace.config(bg="black")

    newProjectLabel.grid(row=1, column=0, pady=5)
    titleLabel.grid(row=2, column=0)
    titleInput.grid(row=2, column=1)
    authorLabel.grid(row=3, column=0)
    authorInput.grid(row=3, column=1, pady=5, padx=10)
    colorLabel.grid(row=4, column=0)
    colorInput.grid(row=4, column=1, pady=5)
    createButton.grid(row=5, column=0)
    driverButton.grid(row=5, column=1, pady=5)
    whitespace.grid(row=6, column=0)


    openExistingLabel = tk.Label(root, text="Open Existing Proejct")
    openExistingLabel.config(bg="black")
    openExistingLabel.config(fg="white")

    openButton = tk.Button(root, text="Browse")
    openExistingLabel.grid(row=6, column=0, padx=10)
    openButton.grid(row=6, column=1, pady=10)

    def getEntryFields(root, title, author, list, color):
    
        if(title != "" and author != "" and color != ""):
                list.clear()
                list.append(title)
                list.append(author)
                list.append(color)
                root.destroy()
        else:
            #Change input fields to red background if empty
            if not title:
                titleInput.configure(bg="red")
            else:
                titleInput.configure(bg="white")
            if not author:
                authorInput.configure(bg="red")
            else:
                authorInput.configure(bg="white")
            print("System Empty Field Error")

    #Opening the debug screen 
    entryData.append(titleInput.get())
    entryData.append(authorInput.get())
   
    root.mainloop()
    return entryData

    





class Node:
    node_counter = 0
    def __init__(self, canvas, x, y, name, description, time, cost):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = canvas.create_oval(x-50, y-50, x+50, y+50, fill="white", outline="black", tags="node" + str(self.node_counter))
        self.name = name
        self.description = description
        self.time = time
        self.cost = cost
        self.text_id = canvas.create_text(x, y, text=name, tags="node_text")
        Node.node_counter += 1

        self.canvas.tag_bind(self.id, "<ButtonPress-1>", self.start_drag)
        self.canvas.tag_bind(self.id, "<B1-Motion>", self.drag)
        self.canvas.tag_bind(self.id, "<ButtonRelease-1>", self.end_drag)


    def start_drag(self, event):
        self.drag_data = {'x': event.x, 'y': event.y}

    def drag(self, event):
        delta_x = event.x - self.drag_data['x']
        delta_y = event.y - self.drag_data['y']
        self.canvas.move(self.id, delta_x, delta_y)
        self.canvas.move(self.text_id, delta_x, delta_y)
        self.x += delta_x
        self.y += delta_y
        self.drag_data = {'x': event.x, 'y': event.y}

    def end_drag(self, event):
        self.drag_data = None

class App:
    def __init__(self, root, title, name, color):
        self.root = root
        self.root.title(title)
        self.author = name

        self.canvas = tk.Canvas(root, width=600, height=400, bg=color)
        self.canvas.pack()

        self.nodes = {}
        self.lines = []
        self.start_node = None
        self.end_node = None

        # Labels and Entry fields
        nameLabel = tk.Label(root, text="Name:")
        nameLabel.pack()
        nameLabel.place(x=0, y=425)
        root.update()

        descLabel = tk.Label(root, text="Description:")
        descLabel.place(x=0, y=(nameLabel.winfo_y() + nameLabel.winfo_height() + 5))
        root.update()

        timeLabel = tk.Label(root, text="Time:")
        timeLabel.place(x=0, y=(descLabel.winfo_y() + descLabel.winfo_height() + 5))
        root.update()

        costLabel = tk.Label(root, text="Cost:")
        costLabel.place(x=0, y=(timeLabel.winfo_y() + timeLabel.winfo_height() + 5))
        root.update()

        self.name_entry = tk.Entry(root, width=20)
        self.name_entry.place(x=(nameLabel.winfo_x() + descLabel.winfo_reqwidth()), y=nameLabel.winfo_y())
        root.update()

        self.description_entry = tk.Entry(root, width=20)
        self.description_entry.place(x=(descLabel.winfo_x() + descLabel.winfo_width()), y=descLabel.winfo_y())
        
        self.time_entry = tk.Entry(root, width=20)
        self.time_entry.place(x=(timeLabel.winfo_x() + descLabel.winfo_width()), y=timeLabel.winfo_y())
        
        self.cost_entry = tk.Entry(root, width=20)
        self.cost_entry.place(x=(costLabel.winfo_x() + descLabel.winfo_width()), y=costLabel.winfo_y())

        # Buttons
        self.add_node_button = tk.Button(root, text="Add Node", command=self.add_node)
        self.add_node_button.place(x=75, y=(costLabel.winfo_y() + costLabel.winfo_height() + 5))

        window_height = nameLabel.winfo_y() + descLabel.winfo_reqheight() + timeLabel.winfo_reqheight() + costLabel.winfo_reqheight() + self.add_node_button.winfo_reqheight() + 50
        root.geometry(f"600x{window_height}")

        #Node details display
        self.detailsLabel = tk.Label(root, text="Node details:")
        self.detailsLabel.place(x=(root.winfo_width()/2.5), y=410)
        
        root.update()

        #Button bindings
        self.canvas.bind("<Button-1>", self.click_node)
        self.canvas.bind("<Button-3>", self.delete_object)
        self.name_entry.bind("<Return>", lambda event: self.add_node)

        
    def add_node(self):
        if(self.time_entry.get() != "" and self.name_entry.get() != "" and self.cost_entry.get() != "" and  self.description_entry.get() != ""):
            name = self.name_entry.get()
            description = self.description_entry.get()
            time = self.time_entry.get()
            cost = self.cost_entry.get()
            node = Node(self.canvas, 100, 100, name, description, time, cost)
            self.nodes[self.canvas.gettags(node.id)[0]] = node
            

            # Clear entry fields
            self.name_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.cost_entry.delete(0, tk.END)
        else:
            print("System Empty Field Error")

    def click_node(self, event):
        closest = self.canvas.find_closest(event.x, event.y)
        tag = self.canvas.gettags(closest)[0]  
        if self.nodes.get(tag) is not None:
            node = self.nodes[tag]
            self.display_details(node)
            if self.start_node is None:
                self.start_node = closest
            else:
                if self.start_node != closest:
                    self.end_node = closest
                    self.draw_line()

    def draw_line(self):
        start_coords = self.canvas.coords(self.start_node)
        end_coords = self.canvas.coords(self.end_node)
        if start_coords[0] < end_coords[0]:
            line = self.canvas.create_line(start_coords[0]+100, start_coords[1]+50, end_coords[0]+0, end_coords[1]+50, tags="line")
        else:
            line = self.canvas.create_line(start_coords[0]+0, start_coords[1]+50, end_coords[0]+100, end_coords[1]+50, tags="line")
        self.lines.append(line)
        self.start_node = None
        self.end_node = None

    def delete_object(self, event):
        closest = self.canvas.find_closest(event.x, event.y)
        if "line" in self.canvas.gettags(closest):
            self.canvas.delete(closest)
            self.lines.remove(closest)

        if "node" in self.canvas.gettags(closest):
            self.canvas.delete(closest)
            self.nodes.remove(closest)

        if "node_text" in self.canvas.gettags(closest):
            self.canvas.delete(closest)
    
    def display_details(self, node):
        nodeName = tk.Label(root, text="Node name: " + node.name)
        nodeName.place(x=(root.winfo_width()/2.5), y=(self.detailsLabel.winfo_y() + self.detailsLabel.winfo_height() + 5))
        root.update()

        nodeDescription = tk.Label(root, text="Description: " + node.description)
        nodeDescription.place(x=(root.winfo_width()/2.5), y=(nodeName.winfo_y() + nodeName.winfo_height() + 5))
        root.update()

        nodeTime = tk.Label(root, text="Time: " + node.time)
        nodeTime.place(x=(root.winfo_width()/2.5), y=(nodeDescription.winfo_y() + nodeDescription.winfo_height() + 5))
        root.update()

        nodeCost = tk.Label(root, text="Cost: " + node.cost)
        nodeCost.place(x=(root.winfo_width()/2.5), y=(nodeTime.winfo_y() + nodeTime.winfo_height() + 5))
        root.update()

class Driver:
    def __init__(self):
        print("Start Driver Class")
        print("Acess the information from the command prompt")
        #creating the platform for debug screen.
        self.testScreen = tk.Tk()
        self.testScreen.title("Driver")
        self.testScreen.geometry('3000x300')
        self.testScreen.tk.call('tk', 'scaling', 2)
        self.testScreen.title("Unit Class Testing")

        #Debug Buttons for testing classes
        self.buttonNodeClass = Button(self.testScreen, text="Node Class")
        self.buttonNodeClass.grid(column=0, row=0)

        #canvas, x, y, name, description, time, cost

        self.x_entry = tk.Entry(root)
        self.x_entry.grid(column=1, row=0)

        self.y_entry = tk.Entry(root, width=20)
        self.y_entry.grid(columr=2, row=0)

        self.name_entry = tk.Entry(root, width=20)
        self.name_entry.grid(column=3, row=0)

        self.description_entry = tk.Entry(root, width=20)
        self.description_entry.grid(column=4,row=0)
        
        self.time_entry = tk.Entry(root, width=20)
        self.time_entry.grid(column=5, row=0)

        
        self.buttonAppClass = Button(self.testScreen, text="App Class  ")
        self.buttonAppClass.grid(column=0, row=1)
        
        self.testScreen.mainloop()


x = homePage()

if len(x) > 2:
    root = tk.Tk()
    app = App(root, x[0],x[1],x[2])
    root.mainloop()