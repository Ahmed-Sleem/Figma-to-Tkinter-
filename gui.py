#imports
import webbrowser
import re
import sys
import os
import  tkinter as tk
import tkinter.messagebox as tk1
import tkinter.filedialog
from pathlib import Path


# Add tkdesigner to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
try:
    from tkdesigner.designer import Designer
except ModuleNotFoundError:
    raise RuntimeError("Couldn't add tkdesigner to the PATH.")
    
    
    
    
# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

# Required in order to add data files to Windows executable
path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

output_path = ""


def btn_clicked():
    token = token_entry.get()
    URL = URL_entry.get()
    output_path = path_entry.get()
    output_path = output_path.strip()
    
    if not token:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Token.")
        return
    if not URL:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter URL.")
        return
    if not output_path:
        tk.messagebox.showerror(
            title="Invalid Path!", message="Enter a valid output path.")
        return
    
    match = re.search(
        r'https://www.figma.com/file/([0-9A-Za-z]+)', URL.strip())
    if match is None:
        tk.messagebox.showerror(
            "Invalid URL!", "Please enter a valid file URL.")
        return
    
    file_key = match[1].strip()
    token = token.strip()
    output = Path(f"{output_path}/build").expanduser().resolve()
    
    if output.exists() and not output.is_dir():
        tk1.showerror(
            "Exists!",
            f"{output} already exists and is not a directory.\n"
            "Enter a valid output directory.")
    elif output.exists() and output.is_dir() and tuple(output.glob('*')):
        response = tk1.askyesno(
            "Continue?",
            f"Directory {output} is not empty.\n"
            "Do you want to continue and overwrite?")
        if not response:
            return
        
    designer = Designer(token, file_key, output)
    designer.design()
    
    tk.messagebox.showinfo(
        "Success!", f"Project successfully generated at {output}.")
    
    
def select_path():
    global output_path
    
    output_path = tk.filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, output_path)
    
    
def know_more_clicked():
    instructions = (
        "https://github.com/Ahmed-Sleem/Figma-to-Tkinter-"
    )
    webbrowser.open_new_tab(instructions)
    
    
def make_label(master, x, y, h, w, *args, **kwargs):
    f = tk.Frame(master, height=h, width=w)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)
    
    label = tk.Label(f, *args, **kwargs)
    label.pack(fill=tk.BOTH, expand=1)
    
    return label






#gui 
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

logo = tk.PhotoImage(file=ASSETS_PATH /"logo.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Figma to TK")


window.geometry("461x440")
window.configure(bg = "#212223")


canvas = Canvas(
    window,
    bg = "#212223",
    height = 440,
    width = 461,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat"
)
button_1.place(
    x=14.0,
    y=389.0,
    width=204.0,
    height=32.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=know_more_clicked,
    relief="flat",
    cursor="hand2"
)
button_2.place(
    x=244.0,
    y=389.0,
    width=204.0,
    height=32.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    116.0,
    204.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    114.5,
    209.0,
    image=entry_image_1
)
URL_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
URL_entry.place(
    x=34.0,
    y=194.0,
    width=161.0,
    height=28.0
)

canvas.create_text(
    27.0,
    174.0,
    anchor="nw",
    text="FILE URL : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 10 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    116.0,
    106.0,
    image=image_image_2
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    114.5,
    111.0,
    image=entry_image_2
)
token_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
token_entry.place(
    x=34.0,
    y=96.0,
    width=161.0,
    height=28.0
)

canvas.create_text(
    27.0,
    76.0,
    anchor="nw",
    text="TOKEN :",
    fill="#FFFFFF",
    font=("Inter SemiBold", 10 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    116.0,
    316.0,
    image=image_image_3
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command= select_path,
    relief = 'flat')
    

button_3.place(
    x=143.0,
    y=330.0,
    width=61.0,
    height=32.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    114.5,
    307.0,
    image=entry_image_3
)
path_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
path_entry.place(
    x=34.0,
    y=292.0,
    width=161.0,
    height=28.0
)

canvas.create_text(
    27.0,
    272.0,
    anchor="nw",
    text="OUTPUT PATH",
    fill="#FFFFFF",
    font=("Inter SemiBold", 10 * -1)
)

canvas.create_text(
    21.0,
    19.0,
    anchor="nw",
    text="Figma to TK",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    345.99510192871094,
    218.0,
    image=image_image_4
)

canvas.create_text(
    251.0,
    123.0,
    anchor="nw",
    text="Button",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    359.0,
    123.0,
    anchor="nw",
    text="Button",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    251.0,
    153.0,
    anchor="nw",
    text="Line",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    359.0,
    153.0,
    anchor="nw",
    text="Line",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    251.0,
    183.0,
    anchor="nw",
    text="Text",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    359.0,
    183.0,
    anchor="nw",
    text="anything",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    251.0,
    208.0,
    anchor="nw",
    text="Rectangle",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    359.0,
    208.0,
    anchor="nw",
    text="Rectangle",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    251.0,
    238.0,
    anchor="nw",
    text="TextArea",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    359.0,
    238.0,
    anchor="nw",
    text="TextArea",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    251.0,
    268.0,
    anchor="nw",
    text="TextBox",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    359.0,
    268.0,
    anchor="nw",
    text="Entry",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    251.0,
    298.0,
    anchor="nw",
    text="Image",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    359.0,
    298.0,
    anchor="nw",
    text="Image",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    251.0,
    328.0,
    anchor="nw",
    text="ButtonHover ",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    359.0,
    328.0,
    anchor="nw",
    text="hover",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    262.0,
    72.0,
    anchor="nw",
    text="Figma",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    358.0,
    72.0,
    anchor="nw",
    text="TKinter",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    251.0,
    19.0,
    anchor="nw",
    text="Naming Code",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
