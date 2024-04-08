#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        tk2 = tk.Tk(master)
        tk2.configure(height=1200, width=1200)
        frame4 = ttk.Frame(tk2)
        frame4.configure(height=1000, width=1000)
        self.Message1 = tk.Message(frame4, name="message1")
        self.Message1.configure(text='message1')
        self.Message1.grid(column=0, row=0, sticky="w")
        self.Message2 = tk.Message(frame4, name="message2")
        self.Message2.configure(text='message2')
        self.Message2.grid(column=1, row=0)
        frame4.grid(column=0, row=0)

        make_draggable(self.Message1)
        make_draggable(self.Message2)

        # Main widget
        self.mainwindow = tk2

    def run(self):
        self.mainwindow.mainloop()

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

if __name__ == "__main__":
    app = NewprojectApp()
    app.run()
