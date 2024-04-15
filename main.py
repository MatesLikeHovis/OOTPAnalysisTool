import list_generation
from tkinter import ttk
import tkinter as tk
from RangeSlider.RangeSlider import RangeSliderH
import batter
import pitcher
import teambuilder
from tkinter import filedialog as fd
from tkinter import messagebox
import os

myFont = ('Raleway',13,'normal')
root = tk.Tk()
root.title("OOTP25 Rating Analyst Tool")
root.iconbitmap(r'Data\SmashIcons_Baseball.ico')
batter_list = []
pitcher_list = []
my_list = []
csv_location = ''
cust_location = ''

def show_tooltip(self):
    # Create a new top-level window with the tooltip text
    self.tooltip_window = tk.Toplevel(root)
    tooltip_label = tk.Label(self.tooltip_window, 
                             text="This button will submit your data")
    tooltip_label.pack()
 
    # Use the overrideredirect method to remove the window's decorations
    self.tooltip_window.overrideredirect(True)
 
    # Calculate the coordinates for the tooltip window
    x = root.winfo_pointerx() + 20
    y = root.winfo_pointery() + 20
    self.tooltip_window.geometry("+{}+{}".format(x, y))

def hide_tooltip(self):
    # Destroy the tooltip window
    self.tooltip_window.destroy()
    self.tooltip_window = None

def generate_lists(csv_location):
    global batter_list, pitcher_list
    try:
        batter_list, pitcher_list = list_generation.make_lists(csv_location)
        if batter_list and pitcher_list:
            listStatus.set('OK!')
            listColor.set('green')
            list_status_bar.config(text="List Status " + listStatus.get(), fg=listColor.get())
    except Exception:
        messagebox(master=None, message="There was an error while generating lists.")

def generate_my_list(cust_location):
    global my_list
    try:
        my_list = list_generation.make_my_lists(cust_location)
        print(my_list)
    except Exception:
        messagebox(master=None, message="There was an error while generating my list.")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(
    menubar,
    tearoff=0
)

analyze_menu = tk.Menu(
    menubar,
    tearoff=0
)

def locate_csv():
    global csvStatus, csvColor, csv_location
    filetypes=[('CSV Files','*.csv')]
    try:
        filename = fd.askopenfilename(
            title="Please locate the csv file",
            initialdir='Data\CSV Files',
            filetypes=filetypes
        )
        if filename:
            csvStatus.set('OK!')
            csvColor.set('green')
            csv_status_bar.config(text="CSV Status " + csvStatus.get(), fg=csvColor.get())
        csv_location = filename
    except:
        messagebox(master=None, message="There was an error in locating the csv file.")

def locate_custom_csv():
    global cust_Status, cust_Color, cust_location, my_list
    filetypes=[('CSV Files','*.csv')]
    try:
        filename = fd.askopenfilename(
            title="Please locate the custom csv file",
            initialdir='Data\CSV Files',
            filetypes=filetypes
        )

        cust_location = filename
        generate_my_list(cust_location)
        if filename and my_list:
            cust_Status.set('Found')
            cust_Color.set('green')
            cust_status_bar.config(text="Custom CSV Status " + cust_Status.get(), fg=cust_Color.get())
    except:
        messagebox(master=None, message="There was an error in locating the csv file.")

def initial_csv_check():
    global csvStatus, csvColor, csv_location
    try:
        csv_location = 'Data\CSV Files\pt_card_list.csv'
        generate_lists(csv_location)
        if (listStatus.get() == 'OK!'):
            csvStatus.set('OK!')
            csvColor.set('green')
            csv_status_bar.config(text="CSV Status " + csvStatus.get(), fg=csvColor.get())
    except:
        return

def custom_csv_check(cust_Status, cust_Color, cust_location):
    global my_list
    try:
        list_of_files = os.listdir('Data\CSV Files')
        for each_file in list_of_files:
            if each_file.startswith('Collection_'):
                cust_location = each_file
        actual_location = "Data\CSV Files\\" + cust_location
        generate_my_list(actual_location)

        if cust_location != '' and my_list:
            cust_Status.set('Found')
            cust_Color.set('green')
            cust_status_bar.config(text="Custom CSV Status " + cust_Status.get(), fg=cust_Color.get())
    except:
        return

def open_batter_menu():
    global canvas
    if canvas:
        canvas.destroy()
    canvas = tk.Canvas(root, width=1000, height=600)
    canvas.grid(columnspan=5)
    batter.batter_menu(myFont, batter_list, my_list, canvas)

file_menu.add_command(
    label="Locate CSV File",
    command=lambda: locate_csv())

file_menu.add_command(
    label="Create Player Lists",
    command=lambda: generate_lists(csv_location))

analyze_menu.add_command(
    label="Batter Analysis Tool",
    command=open_batter_menu)

file_menu.add_command(
    label="Locate Team-Only Custom CSV File",
    command=lambda:locate_custom_csv()
)

def open_pitcher_menu():
    global canvas
    if canvas:
        canvas.destroy()
    canvas = tk.Canvas(root, width=1000, height=600)
    canvas.grid(columnspan=5)
    pitcher.pitcher_menu(myFont, pitcher_list, my_list, canvas)

def open_teambuilder_menu():
    global canvas
    if canvas:
        canvas.destroy()
    canvas = tk.Canvas(root, width=1000, height=600)
    canvas.grid(columnspan=5)
    teambuilder.teambuilder_menu(myFont, batter_list, my_list, canvas)

analyze_menu.add_command(
    label="Pitcher Analysis Tool",
    command=open_pitcher_menu
    )
analyze_menu.add_command(
    label="Team Builder Tool",
    command=open_teambuilder_menu
)

file_menu.add_command(
    label='Exit',
    command=root.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu
)

menubar.add_cascade(
    label="Analyze",
    menu=analyze_menu
)

canvas = tk.Canvas(root, width=1000, height=600)
canvas.grid(columnspan=5)

instructions = tk.Label(canvas,pady=100, padx=100,text="Welcome to The Unofficial OOTP25 WAR (Weighting and Rating) Tool", font=myFont)
instructions.grid(columnspan=3, column=1, row=0)
instructions2 = tk.Label(canvas,pady=10, text="use the Menu to open an analysis report type.")
instructions2.grid(columnspan=3, column=1,row=1)
listStatus = tk.StringVar(value="Not Generated")
csvStatus = tk.StringVar(value="Not Loaded")
cust_Status = tk.StringVar(value="Not Loaded")
listColor = tk.StringVar(value="red")
csvColor = tk.StringVar(value='red')
cust_Color = tk.StringVar(value='orange')
csv_status_bar = tk.Label(canvas,pady=5,padx=5, text="CSV Status " + csvStatus.get(), fg=csvColor.get())
csv_status_bar.grid(column=1,row=2)
cust_status_bar = tk.Label(canvas,padx=5,pady=5,text="Custom CSV Status "+ cust_Status.get(), fg=cust_Color.get())
cust_status_bar.grid(column=2,row=2)
list_status_bar = tk.Label(canvas,padx=5,pady=5,text="List Status " + listStatus.get(), fg=listColor.get())
list_status_bar.grid(column=3,row=2)
initial_csv_check()
custom_csv_check(cust_Status, cust_Color, cust_location)
root.mainloop()



