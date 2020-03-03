# Programmer - python_scripts (Abhijith Warrier)

# Importing necessary packages
import pyqrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    label = Label(text="ENTER TEXT : ", bg="darkolivegreen4")
    label.grid(row=0, column=1, padx=5, pady=5)

    root.entry = Entry(width=30, textvariable=qrInput)
    root.entry.grid(row=0, column=2, padx=5, pady=5)

    button = Button(width=10, text="GENERATE", command=QRCodeGenerate)
    button.grid(row=0, column=3, padx=5, pady=5)

    label = Label(text="QR CODE : ", bg="darkolivegreen4")
    label.grid(row=1, column=1, padx=5, pady=5)

    root.imageLabel = Label(root, background="darkolivegreen4")
    root.imageLabel.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

# Defining QRCodeGenerate() function to create Generate QRCode Images
def QRCodeGenerate():
    # Storing user-input text in a variable
    qrString = qrInput.get()

    # Checking if the user has entered some text then do the following
    if qrString != '':
        # Generate object of QRCode
        qrGenerate = pyqrcode.create(qrString)

        # Setting destination path to save the QRCode Image
        qrCodePath = 'YOUR DESTINATION PATH'
        # Creating name for the image with user-input text as the name and .png as the extension
        # Concatenating the name with the path and storing it in qrCodeName variable
        qrCodeName = qrCodePath + qrString + ".png"

        # Creating png image of the QRCode using png(). To create png image pypng module has to be
        # installed. The png() takes the Filename and Scale Value as the arguments
        qrGenerate.png(qrCodeName, scale = 10)

        # Opening the saved QRCode Image using the open() method of the Image module
        image = Image.open(qrCodeName)
        # Resizing the image using Image.resize()
        image = image.resize((400, 400), Image.ANTIALIAS)
        # Creating object of PhotoImage() class to display the frame
        image = ImageTk.PhotoImage(image)
        # Configuring the label to displaying the QRCode Image
        root.imageLabel.config(image=image)
        root.imageLabel.photo = image

    # If the user has not entered any text then error is shown
    else:
        messagebox.showerror("ERROR", "ENTER A TEXT.!")

# Creating object root of tk
root = tk.Tk()

# Setting the title, window size, disabling the resizing property
# and setting the backgrounc color
root.title("PyQR GENERATOR")
root.geometry("510x500")
root.resizable(False, False)
root.config(background = "darkolivegreen4")

# Creating tkinter variable
qrInput = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()