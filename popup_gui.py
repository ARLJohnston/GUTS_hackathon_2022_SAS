from cgitb import text
import tkinter as tk
import os

def find_files(x) -> list:
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            x.insert(tk.END,file)

    return x

def selected_options():
    selected = []
    for select in splash_filename.curselection():
        selected.append(splash_filename.get(select))
    
    lt = lat.get(1.0,tk.END)
    lng = long.get(1.0,tk.END)

    selected.append(lt)
    selected.append(lng)

    return selected

def main_window(*args,**kwargs):
    ## yeet the main window code here
    print(*args)
    return None

splash_root = tk.Tk()

splash_root.geometry("400x500")

splash_label = tk.Label(splash_root,font=18)


file_lab = tk.Label(splash_root,font=18,text="Select files to import: ")

splash_filename = tk.Listbox(splash_root,selectmode="multiple",height=10)

find_files(splash_filename)


lat_lab = tk.Label(splash_root,font=18,text="Latitude")
lat = tk.Text(splash_root,height = 2, width=20)
long_lab = tk.Label(splash_root,font=18,text="Longitude")
long = tk.Text(splash_root,height=2, width =20)


button = tk.Button(splash_root,text="Map",command= lambda: (main_window(selected_options),splash_root.destroy()))

# PACK STUFF
splash_label.pack()
file_lab.pack()
splash_filename.pack()
lat_lab.pack()
lat.pack(expand=True)
long_lab.pack()
long.pack(expand=True)

button.pack()

tk.mainloop()


