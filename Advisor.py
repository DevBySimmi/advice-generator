from tkinter import *
from tkinter import messagebox
import random

# Main Window
root = Tk()
root.title("Random Advisor Application")
root.geometry("500x350")
root.config(bg="#1e1e2f")

# Advice List
advice_list = [
    "Believe in yourself 💖",
    "Every day is a fresh start 🌸",
    "Small progress is still progress 🚀",
    "Stay positive and work hard 😎",
    "Dream big and dare more ✨"
]

# Function to show advice
def get_advice():
    advice = random.choice(advice_list)
    advice_label.config(text=advice)

# Function to copy advice
def copy_advice():
    root.clipboard_clear()
    root.clipboard_append(advice_label.cget("text"))
    messagebox.showinfo("Copied", "Advice copied successfully ✅")

# Title
title = Label(
    root,
    text="💡 Random Advice Generator",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# Advice Box
advice_label = Label(
    root,
    text="Click the button for advice 😊",
    font=("Arial", 14),
    wraplength=350,
    width=30,
    height=5,
    bg="white",
    fg="#333",
    relief="ridge",
    bd=3
)
advice_label.pack(pady=20)

# Get Advice Button
btn1 = Button(
    root,
    text="Get Advice 🎲",
    font=("Arial", 12, "bold"),
    bg="#6c63ff",
    fg="white",
    padx=10,
    pady=5,
    command=get_advice
)
btn1.pack(pady=10)

# Copy Button
btn2 = Button(
    root,
    text="Copy Advice 📋",
    font=("Arial", 12, "bold"),
    bg="#ff6584",
    fg="white",
    padx=10,
    pady=5,
    command=copy_advice
)
btn2.pack()

root.mainloop()
