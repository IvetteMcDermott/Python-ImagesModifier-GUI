from tkinter import *
from rembg import remove

from PIL import Image, ImageTk


def open_image(new_img):
    frame = Frame(root,width=200,height=200,bd=5,bg='white')

    new_img_sized = new_img.resize((400, 400))
    photo = ImageTk.PhotoImage(new_img_sized)

    photo_label = Label(frame, image=photo)
    photo_label.pack()
    photo_label.image = photo
    frame.pack()
    return photo

# Creates the window
root = Tk()

old_image = "us-kerry.jpg"
output_image = "rmv-us-kerry.png"

orig_img = Image.open(old_image)
new_img = remove(orig_img)

new_img.save(output_image)

root.title('Image removes')
root.geometry("400x400")

open_image(new_img)
root.mainloop()
