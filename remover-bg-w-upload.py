from tkinter import *
from rembg import remove

from tkinter import filedialog
import time
from PIL import Image, ImageTk


def upload_img():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        orig_img = Image.open(file_path)


old_image = "IMG_20210319_150555867_HDR.jpg"
output_image = "somwhere.png"


def remove_background(old_image):

    orig_img = Image.open(old_image)
    global new_img
    new_img = remove(orig_img)
    new_img.save(output_image)
    

def open_image(new_img):
    frame = Frame(root,width=200,height=200,bd=5,bg='white')

    new_img_sized = new_img.resize((400, 400))
    photo = ImageTk.PhotoImage(new_img_sized)

    photo_label = Label(frame, image=photo)
    photo_label.pack()
    photo_label.image = photo
    frame.pack()
    

# Creates the window
root = Tk()


root.title('Image Bg Removed')
root.geometry("400x400")


upload_img()
remove_background(old_image)
open_image(new_img)

root.mainloop()
