from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from stegano import lsb
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def set_background():
    # Load background image
    bg_image = Image.open(resource_path("C:/Users/madin/Desktop/stegno/Steganography GUI Application for Secure Communication/assets/background_image.jpg"))
    bg_image = bg_image.resize((950, 750), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)

    # Create a Canvas widget to place the background image
    canvas = Canvas(root, width=950, height=750)
    canvas.pack(fill="both", expand=True)

    # Set the background image
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image  # Keep a reference to avoid garbage collection

root = Tk()
root.title("Steganography GUI Application for Secure Communication")
root.geometry("950x750")
root.resizable(False, False)
root.configure(bg="#ffffff")
root.iconbitmap(resource_path("C:/Users/madin/Desktop/stegno/Steganography GUI Application for Secure Communication/assets/Logo.ico"))

# Set background image
set_background()

def show_image():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image",
        filetype=(
            ("Image Files", "*.png *.jpeg *.jpg *.bmp *.gif *.tiff"),
            ("All Files", "*.*")
        )
    )
    img = Image.open(filename)
    img = img.resize((450, 450), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

def hide_data():
    global secret
    message = text1.get(1.0, END)
    
    secret = lsb.hide(str(filename), message)

def show_data():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    if 'secret' in globals():
        secret.save(resource_path("C:/Users/madin/Desktop/stegno/Steganography GUI Application for Secure Communication/Hidden.png"))
    else:
        
        print("No secret data to save.")


logo = PhotoImage(file=resource_path("C:/Users/madin/Desktop/stegno/Steganography GUI Application for Secure Communication/assets/output-onlinepngtools.png"))
Label(root, image=logo, bg="#ffffff").place(x=10, y=10)

Label(root, text="Stegnography", bg="#34495e", fg="white", font="arial 30 bold").place(x=90, y=15)

f = Frame(root, bd=3, bg="#2c3e50", width=450, height=450, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="#2c3e50")
lbl.place(x=10, y=5)

frame2 = Frame(root, bd=3, width=450, height=450, relief=GROOVE, bg="#34495e")
frame2.place(x=480, y=80)

text1 = Text(frame2, font="Roboto 14", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=450, height=450)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=430, y=0, height=445)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3 = Frame(root, bd=3, bg="#2f4155", width=450, height=150, relief=GROOVE)
frame3.place(x=10, y=550)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=show_image, bg="#ffffff").place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save, bg="#ffffff").place(x=230, y=30)

frame4 = Frame(root, bd=3, bg="#2f4155", width=450, height=150, relief=GROOVE)
frame4.place(x=480, y=550)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=hide_data).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=show_data).place(x=230, y=30)

root.mainloop()