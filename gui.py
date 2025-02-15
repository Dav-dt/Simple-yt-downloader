import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mg
import os
import pytubefix as pt

import utils, custom

outputDir = ""
root = tk.Tk()
root.configure(bg=custom.bgColor)
root.title("YT-Downloader Companion")
root.geometry(custom.dimensions)
root.iconbitmap("icon.ico")

def changeDirOutput()->None:
    """
    Filedialog function to change output directory.
    """
    global outputDir
    dir_ = fd.askdirectory()
    if dir_:
        outputDir = dir_

    return None

def clear_input()->None:
    """
    Clears the text input field when clicked.
    """
    valueD.set("")

    return None

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Change Directory Output", command=changeDirOutput)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=utils.sendToGithubPage)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

title = tk.Label(root, text="YT-Downloader Companion", bg="#864db8", fg=custom.fg, font=custom.fontTitle)
title.pack(pady=(20, 10))

var = tk.StringVar(value='mp4')

frame_radio_buttons = tk.Frame(root, bg=custom.bg)
frame_radio_buttons.pack(pady=(10, 20))

mp4 = tk.Radiobutton(frame_radio_buttons, text='Download MP4(Video)', variable=var, value='mp4', bg=custom.bg, fg=custom.fg, font=custom.font, bd=2, relief="solid")
mp4.grid(row=0, column=0, padx=10)

mp3 = tk.Radiobutton(frame_radio_buttons, text='Download MP3(Audio)', variable=var, value='mp3', bg=custom.bg, fg=custom.fg, font=custom.font, bd=2, relief="solid")
mp3.grid(row=0, column=1, padx=10)

frame_input = tk.Frame(root, bg=custom.bg)
frame_input.pack(pady=20)

valueD = tk.StringVar(value="Paste Youtube Link")
entree = tk.Entry(frame_input, textvariable=valueD, width=30, bg=custom.bg, fg=custom.fg, font=custom.font, bd=2, relief="solid")
entree.grid(row=0, column=0, padx=(10, 0))

clear_button = tk.Button(frame_input, text="Clear", bg=custom.bg, fg=custom.fg, font=custom.font, command=clear_input, bd=2, relief="solid")
clear_button.grid(row=0, column=1, padx=(10, 0))

def download()->None:
    """
    function to download
    """
    global outputDir

    target = valueD.get()
    if not target or "youtu" not in target:
        mg.showerror("Value Error", "You must specify a valid URL")
        return

    try:
        vid = pt.YouTube(target)

        if var.get() == "mp4":
            rvid = vid.streams.get_highest_resolution()
            output_path = outputDir if outputDir else utils.makeDefaultOutPutDir()
            rvid.download(output_path=output_path)
            mg.showinfo("Success", f"{var.get()} downloaded successfully")

        elif var.get() == "mp3":
            audio_stream = vid.streams.get_audio_only()
            output_path = outputDir if outputDir else utils.makeDefaultOutPutDir()
            audio_stream.download(output_path=output_path, filename=f"{vid.title}.mp3")
            mg.showinfo("Success", "MP3 downloaded successfully")

    except Exception as r:
        mg.showerror("Error", f"Could not download the video: {str(r)}")

dlButton = tk.Button(root, text="Download", bg=custom.bg, fg=custom.fg, font=custom.font, command=download, bd=2, relief="solid")
dlButton.pack(pady=20)
