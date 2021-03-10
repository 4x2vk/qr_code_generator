#!/usr/bin/env python3
import PIL.Image
from PIL import Image
import qrcode
from tkinter import *

root = Tk()
root.title('QR-code generator')

def myClick():
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,)
    url = f_name.get()
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    #saving to current folder
    fileName = "qr-code-example.png"
    img.save(fileName)

name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20, pady=(10, 0))

label = Label(root, text='Enter URL')
label.grid(row=0, column=0, pady=(10, 0))

submit_btn = Button(root, text="Generate", command=myClick)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()
