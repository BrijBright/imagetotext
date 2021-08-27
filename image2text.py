from PIL import Image, ImageGrab
import pytesseract
from tkinter import*
from tkinter import ttk
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def imageTotext(image):
    return pytesseract.image_to_string(image)


def imgrab(mode):
    if mode == 0:
        box = (0, 100, 1366/2, 768-50)
        return ImageGrab.grab(box)
    return ImageGrab.grab()


def gui(mode):
    image = imgrab(mode)
    text = imageTotext(image)
    mylabel.insert(END, text)


def otherwindow(mode):
    otherwin = Toplevel()
    Button(otherwin, command=lambda: gui(mode), height=2, width=30,
           bg="blue", text="ADD MORE", fg="white").place(x=0, y=0)
    otherwin.maxsize(width=450, height=50)
    otherwin.mainloop()


root = Tk()
root.maxsize(width=650, height=550)
root.geometry('650x550')
root.title("image2text")
mylabel = Text(root)
mylabel.place(x=0, y=0)
Button(root, command=lambda: gui(0), height=2, width=30,
       bg="blue", text="ADD MORE", fg="white").place(x=5, y=450)

Button(root, command=lambda: otherwindow(1), height=2, width=30,
       bg="blue", text="fullmode", fg="white").place(x=300, y=450)

root.resizable()
root.mainloop()
