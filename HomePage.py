from tkinter import *

#New Window
window = Tk()
window.title("Workflow Homepage.")
window.geometry('900x600')
window.tk.call('tk', 'scaling', 3.0)


window2 = Tk()
window2.title("Test")
window2.geometry('20x50')
window2.tk.call('tk', 'scaling', 1.5)



#adding stuff
lbl = Label(window, text="Enter your diagram name.")
lbl.grid(column = 0, row=0)

txt_spin_value = 1
spinNumber = Spinbox(window, from_ = 1, to = 10, textvariable=txt_spin_value)
spinNumber.grid(column=1, row=0)

btnOk = Button(window, text="Ok")
btnOk.grid(column=0, row=2)

btnCancel = Button(window, text="Cancel")
btnCancel.grid(column=1, row=2)


window.mainloop()
window2.mainloop()






