from tkinter import *
root = Tk()
# window size
root.geometry("500x500")

#window title
root.title("this is a title- suling chu")

#lable creation
label = Label(root,text ="this is a lable- suling chu")
label.pack()

#creating entry box
label2 = Label(root,text ="Name:")
label2.pack(side = "left")
entry = Entry(root,width = 40)
entry.pack(side = "left")

#creating a button
button = Button(root,text = "this is a button so you can click it- suling chu",background = "yellow",command = root.destroy)
button.pack(side = "top")

root.mainloop()