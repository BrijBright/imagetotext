from pynput import keyboard
from PIL import Image, ImageGrab
import pytesseract
from tkinter import*
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# pynput upgradre (version 1 tart)
# need pynput module
alt = 0
z = 0


def fun():
    global alt, s
    if alt == 1 and z == 1:
        gui(1)


def on_press(key):
    global alt, z
    if str(key) == "Key.alt_l":
        alt = 1
    if str(key).replace("'", '') == 'z':
        z = 1
    fun()


def on_release(key):
    global alt, z
    alt = 0
    z = 0


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
# pynput upgradre (version 1 end)


def imageTotext(image):
    return pytesseract.image_to_string(image)


def imgrab(mode):
    if mode == 0:
        box = (0, 100, 1366/2, 768-50)
        return ImageGrab.grab(box).convert("L")
    return ImageGrab.grab().convert("L")


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
root.title("image2text BY BRIJKISHOR GUPTA")
mylabel = Text(root)
mylabel.place(x=0, y=0)

lb = Label(root, text="press 'alt z' to extract text",
           font=('Helvatical bold', 15))
lb.place(x=150, y=400)

Button(root, command=lambda: gui(0), height=2, width=30,
       bg="blue", text="ADD MORE", fg="white").place(x=5, y=450)

Button(root, command=lambda: otherwindow(1), height=2, width=30,
       bg="blue", text="fullmode", fg="white").place(x=300, y=450)

root.resizable()
root.mainloop()
