from tkinter import *
from rembg import remove

from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

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
    forget(upload_btn)

    global textUpl
    textUpl = Label(root, text='Image uploaded')
    # Display elements
    textUpl.pack()
    remove_btn.pack()

# function to remove the bg with library
def remove_background(old_image):
    orig_img = Image.open(old_image)
    forget(textUpl)
    forget(remove_btn)
    global new_img
    global textBgR
    # remove 
    new_img = remove(orig_img)
    textBgR = Label(root, text='Bg removed')
    textBgR.pack()
    # call the function to open the result img
    open_image(new_img)

# https://www.tutorialspoint.com/save-file-dialog-box-in-tkinter
def save_img(new_img):
    # Get the file path using asksaveasfile
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    global text
    # conditional if the path and name had been selected, save, display and hide elements
    if file_path:
        new_img.save(file_path)
        forget(save_btn)
        text = Label(root, text="saved")
        text.pack()
        forget(textBgR)
        forget(frame)
        # btn to call the upload btn again for a new img 
        restart_btn.pack()

# function for open image and display after resize it
def open_image(new_img):
    # set of frame for img
    global frame
    frame = Frame(root,width=200,height=200,bd=5,bg='white')
    # resize img
    new_img_sized = new_img.resize((400, 400))
    # PIL support module for imgs in tkinter 
    photo = ImageTk.PhotoImage(new_img_sized)
    # link the photo to the frame
    photo_label = Label(frame, image=photo)
    photo_label.pack()
    # assign the photo to image, it neccesary step for keep it 
    # in memory while the widget is display. Tkinter 
    photo_label.image = photo
    frame.pack()
    save_btn.pack()

# function to upload a new image 
def upload_next_img():
    # forget elements to clear the window
    forget(frame)
    forget(restart_btn)
    forget(text)
    # call the function for upload img
    upload_img()


# Creates the window
root = Tk()

# window setting
root.title('Image Bg Remover')
root.geometry("550x550")
# element to give space
e = Label(root, width=15, borderwidth=2, font=1.05, justify='right')
e.pack()

# btns
upload_btn = Button(root, text="Upload Image", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=upload_img)
remove_btn = Button(root, text="Remove Bg", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: remove_background(old_image))
save_btn = Button(root, text="Save Image", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda:save_img(new_img))
restart_btn = Button(root, text="Upload New Image", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=upload_next_img)

# call the firts btn, to upluad
upload_btn.pack()

# calls the TK window 
root.mainloop()
