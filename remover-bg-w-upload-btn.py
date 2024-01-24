from tkinter import *
from rembg import remove

from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

import time
from PIL import Image, ImageTk


# https://www.geeksforgeeks.org/python-forget_pack-and-forget_grid-method-in-tkinter/
def forget(widget): 
    # This will remove the widget from toplevel 
    # basically widget do not get deleted 
    # it just becomes invisible and loses its position 
    # and can be retrieve 
    widget.pack_forget() 

# Starter variables
old_image = "a.png"
output_image = "bgRemoved.png"


# Upload Image Function
def upload_img():
    # To open dialog box to upload the image 
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        # get the path to the image
        orig_img = Image.open(file_path)
        # save the image from the path
        orig_img.save(old_image)
    # Hide the upload btn
    forget(btn_1)

    global textUpl
    textUpl = Label(root, text='Image uploaded')
    # Display elements
    textUpl.pack()
    btn_2.pack()


def remove_background(old_image):
    orig_img = Image.open(old_image)
    forget(textUpl)
    forget(btn_2)
    global new_img
    global text
    new_img = remove(orig_img)
    text = Label(root, text='Bg removed')
    text.pack()
    open_image(new_img)

# https://www.tutorialspoint.com/save-file-dialog-box-in-tkinter
def save_img(new_img):
    # Get the file path using asksaveasfile
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    if file_path:
        new_img.save(file_path)
        forget(btn_3)
        t = Label(root, text="saved")
        t.pack()
        forget(text)

        
def open_image(new_img):
    global frame
    frame = Frame(root,width=200,height=200,bd=5,bg='white')
    
    new_img_sized = new_img.resize((400, 400))
    photo = ImageTk.PhotoImage(new_img_sized)

    photo_label = Label(frame, image=photo)
    photo_label.pack()
    photo_label.image = photo
    btn_3.pack()
    frame.pack()


# Creates the window
root = Tk()

root.title('Image Bg Removed')
root.geometry("500x500")
e = Label(root, width=15, borderwidth=2, font=1.05, justify='right')
e.pack()

btn_1 = Button(root, text="upload", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=upload_img)
btn_2 = Button(root, text="remove bg", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: remove_background(old_image))
btn_3 = Button(root, text="save img", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda:save_img(new_img))

btn_1.pack()


# upload_img()
# remove_background(old_image)
# open_image(new_img)

root.mainloop()
