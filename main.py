import clipboard
from tkinter import *
import tkinter.font as font

root = Tk()
root.configure(background='black')
root.title("Ultra Mega Clipboard !")
root.geometry("370x900")
myFont = font.Font(size=20)

def copy_name(event):
    clipboard.copy("David Marom")

def copy_title(event):
    clipboard.copy("Product Manager")

def copy_number(event):
    clipboard.copy("0587077017")

def copy_li(event):
    clipboard.copy("https://www.linkedin.com/in/maromdavid/")

def copy_mail(event):
    clipboard.copy("davidmarom.product@gmail.com")




main_frame = Frame(root, width=300, height=200, bg="black")
main_frame.pack()

btn_1 = Button(main_frame, text="David Marom", width = 20, height = 3, bg="black", fg="#00FF00")
btn_1['font'] = myFont
btn_1.bind("<Button-1>", copy_name)
btn_1.pack()

btn_2 = Button(main_frame, text="Product Manager", width = 20, height = 3 , bg="black", fg="#00FF00" )
btn_2['font'] = myFont
btn_2.bind("<Button-1>", copy_title)
btn_2.pack()

btn_3 = Button(main_frame, text="0587077017", width = 20, height = 3 , bg="black", fg="#00FF00" )
btn_3['font'] = myFont
btn_3.bind("<Button-1>", copy_number)
btn_3.pack()

btn_4 = Button(main_frame, text="LinkedIn", width = 20, height = 3 , bg="black", fg="#00FF00" )
btn_4['font'] = myFont
btn_4.bind("<Button-1>", copy_li)
btn_4.pack()

btn_5 = Button(main_frame, text="Mail", width = 20, height = 3 , bg="black", fg="#00FF00" )
btn_5['font'] = myFont
btn_5.bind("<Button-1>", copy_mail)
btn_5.pack()

root.mainloop()


