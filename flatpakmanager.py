#!/usr/bin/env python3
### Program to manage uninstalled flatpaks ###

print("Import functions...")
import tkinter as gui
from tkinter import messagebox
import subprocess
import os

#get version
print("Get version of the application...")
run_path = os.path.abspath(os.path.dirname(__file__))
version = open(run_path + "/version.txt", "r")
version = version.readline()
print("flatpakmanager version", version)

print("Load definitons...")
#what happens after yes/no button
def runcommand(command):
    print("Process confirmed.")
    print(command)
    successfulchecker = subprocess.run((command), shell=True)
    if successfulchecker.returncode == 0:
        messagebox.showinfo("Successful", "Everything cleaned.")
    else:
        messagebox.showerror("Error", "An error occurred")

def cancelcom():
    print("Operation canceled.")

#button definitons
def uninstalled_config():
    sure = messagebox.askyesno("Sure?", "Do you want to continue?")
    if sure == False:
        cancelcom()
    else:
        runcommand('''flatpak remove --delete-data -y''')

def unused_depend():
    sure = messagebox.askyesno("Sure?", "Do you want to continue?")
    if sure == False:
        cancelcom()
    else:
        runcommand('''flatpak remove --unused -y''')

def remove_config_depend():
    sure = messagebox.askyesno("Sure?", "Do you want to continue?")
    if sure == False:
        cancelcom()
    else:
        runcommand('''flatpak remove --unused --delete-data -y''')

def remove_all():
    sure = messagebox.askyesno("Sure?", "Do you want to continue?")
    if sure == False:
        cancelcom()
    else:
        runcommand('''flatpak remove --all -y''')

def aboutprogram():
    showversion = ("Version: " + version)
    showinfolines = ["Flatpak manager", "Developed by Palace4Software", "", showversion, "", "", "This software is distributed under the MIT License."]
    messagebox.showinfo("About", "\n".join(showinfolines))

def exitprogram():
    GUI.destroy()

#GUI
print("Setup graphical user interface...")
GUI = gui.Tk()
GUI.title("Flatpakmanager")
GUI.geometry("400x350")
GUI.resizable(width=False, height=False)

space1 = gui.Label(GUI).pack(expand=True, fill="x")

headline = gui.Label(text="Flatpak Manager for unused flatpaks", font=("Liberation Serif", 13))
headline.pack(expand=True, fill="x")

space2 = gui.Label(GUI).pack(expand=True, fill="both")

oldconfigbutton = gui.Button(GUI, text="Remove old config", bg="#008000", fg="#ffffff", command=uninstalled_config)
oldconfigbutton.pack() #button1
unuseddepenbutton = gui.Button(GUI, text="Remove unused flatpaks (e.g. runtimes)", bg="#005ce6", fg="#ffffff", command=unused_depend)
unuseddepenbutton.pack() #button2
configdependbutton = gui.Button(GUI, text="Remove the unused flatpaks and old config", bg="#3333cc", fg="#ffffff", command=remove_config_depend)
configdependbutton.pack() #button3
removeall = gui.Button(GUI, text="Remove all installed flatpaks (without config)", bg="#990000", fg="#ffffff", command=remove_all)
removeall.pack() #button4

space3 = gui.Label(GUI).pack(expand=True, fill="both")

aboutbutton = gui.Button(GUI, text="About", command=aboutprogram)
aboutbutton.pack(side="left") #about button
exitbutton = gui.Button(GUI, text="Exit", command=exitprogram)
exitbutton.pack(side="right") #exit button

space4 = gui.Label(GUI).pack(expand=True, fill="x")

print("Application ready.")

GUI.mainloop()
print("Exit program...")
