import tkinter as tk

class Node:
    def __init__(self, canvas, x, y, name, description, time, cost):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = canvas.create_oval(x-50, y-50, x+50, y+50, fill="white", outline="black", tags="node")
        self.name = name
        self.description = description
        self.time = time
        self.cost = cost
        self.text_id = canvas.create_text(x, y, text=name, tags="node_text")

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
    def __init__(self, root, title, author):
        self.root = root
        self.root.title(title)
        self.author = author

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.nodes = []
        self.lines = []
        self.start_node = None
        self.end_node = None

        # Labels and Entry fields
        tk.Label(root, text="Name:").pack()
        self.name_entry = tk.Entry(root, width=20)
        self.name_entry.pack()
        tk.Label(root, text="Description:").pack()
        self.description_entry = tk.Entry(root, width=20)
        self.description_entry.pack()
        tk.Label(root, text="Time:").pack()
        self.time_entry = tk.Entry(root, width=20)
        self.time_entry.pack()
        tk.Label(root, text="Cost:").pack()
        self.cost_entry = tk.Entry(root, width=20)
        self.cost_entry.pack()

        # Buttons
        self.add_node_button = tk.Button(root, text="Add Node", command=self.add_node)
        self.add_node_button.pack()

        self.canvas.bind("<Button-1>", self.click_node)
        self.canvas.bind("<Button-3>", self.delete_object)
        self.name_entry.bind("<Return>", lambda event: self.add_node())


    def add_node(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        time = self.time_entry.get()
        cost = self.cost_entry.get()
        node = Node(self.canvas, 100, 100, name, description, time, cost)
        self.nodes.append(node)

        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)

    def click_node(self, event):
        closest = self.canvas.find_closest(event.x, event.y)
        if "node" in self.canvas.gettags(closest):
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
           

root = tk.Tk()
menu = tk.Tk()
app = App(root, "Work Flow", "Author")
root.mainloop()
