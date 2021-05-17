from pytube import YouTube
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import sys
import threading as thr

from pytube.exceptions import RegexMatchError

LINK = ''
PATH = ''


def download_video():
    global LINK, PATH
    LINK = top.link_box.get()
    PATH = top.path_box.get()
    top.link_box.config(state="disabled")
    top.path_box.config(state="disabled")
    top.download_button.config(state="disabled")
    top.browse_button.config(state="disabled")
    top.state_label.config(text="Downloading Video....")
    thr.Thread(target=start_downloading_stream, args=(LINK, PATH)).start()
    return 0


def start_downloading_stream(link, path):
    try:
        yt = YouTube(link)
        yt.streams.first().download(path)
        top.state_label.config(text="Download complete....")
        top.link_box.config(state="normal")
        top.path_box.config(state="normal")
        top.download_button.config(state="normal")
        top.browse_button.config(state="normal")
        top.link_box.delete("0", "end")
        top.path_box.delete("0", "end")
    except RegexMatchError:
        top.state_label.config(text="Video Not Found!")
        top.link_box.config(state="normal")
        top.path_box.config(state="normal")
        top.download_button.config(state="normal")
        top.browse_button.config(state="normal")
    return 0


def get_directory():
    get_path = filedialog.askdirectory()
    top.path_box.delete("0", "end")
    top.path_box.insert("0", get_path)
    return 0


top = tk.Tk()

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
top.style = ttk.Style()
if sys.platform == "win32":
    top.style.theme_use('winnative')
top.style.configure('.', background=_bgcolor)
top.style.configure('.', foreground=_fgcolor)
top.style.configure('.', font="TkDefaultFont")
top.style.map('.', background=[('selected', _compcolor), ('active',_ana2color)])

top.geometry("600x450+383+106")
top.minsize(120, 1)
top.maxsize(1366, 745)
top.resizable(1,  1)
top.title("YTD-GT")
top.configure(background="#ffffff")
top.configure(highlightbackground="#ffffff")
top.configure(highlightcolor="#ffffff")

top.heading = tk.Label(top)
top.heading.place(relx=0.0, rely=0.0, height=111, width=604)
top.heading.configure(activebackground="#f9f9f9")
top.heading.configure(activeforeground="black")
top.heading.configure(background="#000000")
top.heading.configure(disabledforeground="#a3a3a3")
top.heading.configure(font="-family {Segoe UI} -size 24 -weight bold")
top.heading.configure(foreground="#ffffff")
top.heading.configure(highlightbackground="#d9d9d9")
top.heading.configure(highlightcolor="black")
top.heading.configure(text='''YTD-GT''')

top.subheading = tk.Label(top)
top.subheading.place(relx=0.0, rely=0.178, height=21, width=604)
top.subheading.configure(activebackground="#f9f9f9")
top.subheading.configure(activeforeground="black")
top.subheading.configure(background="#000000")
top.subheading.configure(disabledforeground="#a3a3a3")
top.subheading.configure(foreground="#ffffff")
top.subheading.configure(highlightbackground="#d9d9d9")
top.subheading.configure(highlightcolor="black")
top.subheading.configure(text='''Py Tech. V1.0''')

top.link_box_label = tk.Label(top)
top.link_box_label.place(relx=0.117, rely=0.289, height=21, width=124)
top.link_box_label.configure(activebackground="#ffffff")
top.link_box_label.configure(activeforeground="black")
top.link_box_label.configure(background="#ffffff")
top.link_box_label.configure(disabledforeground="#a3a3a3")
top.link_box_label.configure(font="-family {Segoe UI} -size 12")
top.link_box_label.configure(foreground="#000000")
top.link_box_label.configure(highlightbackground="#d9d9d9")
top.link_box_label.configure(highlightcolor="black")
top.link_box_label.configure(justify='left')
top.link_box_label.configure(text='''YouTube Link''')

top.link_box = ttk.Entry(top)
top.link_box.place(relx=0.133, rely=0.356, relheight=0.091, relwidth=0.777)
top.link_box.configure(font="-family {Segoe UI} -size 12")
top.link_box.configure(takefocus="")
top.link_box.configure(cursor="ibeam")

top.path_box_label = tk.Label(top)
top.path_box_label.place(relx=0.117, rely=0.489, height=21, width=124)
top.path_box_label.configure(activebackground="#f9f9f9")
top.path_box_label.configure(activeforeground="black")
top.path_box_label.configure(background="#ffffff")
top.path_box_label.configure(disabledforeground="#a3a3a3")
top.path_box_label.configure(font="-family {Segoe UI} -size 12")
top.path_box_label.configure(foreground="#000000")
top.path_box_label.configure(highlightbackground="#d9d9d9")
top.path_box_label.configure(highlightcolor="black")
top.path_box_label.configure(justify='left')
top.path_box_label.configure(text='''Download Path''')

top.path_box = ttk.Entry(top)
top.path_box.place(relx=0.133, rely=0.556, relheight=0.091, relwidth=0.577)
top.path_box.configure(font="-family {Segoe UI} -size 12")
top.path_box.configure(takefocus="")
top.path_box.configure(cursor="ibeam")

top.browse_button = ttk.Button(top)
top.browse_button.place(relx=0.733, rely=0.553, height=43, width=106)
top.browse_button.configure(takefocus="")
top.browse_button.configure(text='''Browse''')
top.browse_button.configure(command=get_directory)

top.state_label = tk.Label(top)
top.state_label.place(relx=0.333, rely=0.667, height=21, width=214)
top.state_label.configure(activebackground="#f9f9f9")
top.state_label.configure(activeforeground="black")
top.state_label.configure(background="#ffffff")
top.state_label.configure(disabledforeground="#a3a3a3")
top.state_label.configure(foreground="#000000")
top.state_label.configure(highlightbackground="#d9d9d9")
top.state_label.configure(highlightcolor="black")
top.state_label.configure(text=''' ''')

top.download_button = ttk.Button(top)
top.download_button.place(relx=0.333, rely=0.733, height=45, width=216)
top.download_button.configure(takefocus="")
top.download_button.configure(text='''Download''')
top.download_button.configure(command=download_video)

top.footer = tk.Label(top)
top.footer.place(relx=-0.017, rely=0.867, height=61, width=614)
top.footer.configure(activebackground="#f9f9f9")
top.footer.configure(activeforeground="black")
top.footer.configure(background="#000000")
top.footer.configure(disabledforeground="#a3a3a3")
top.footer.configure(foreground="#ffffff")
top.footer.configure(highlightbackground="#d9d9d9")
top.footer.configure(highlightcolor="black")
top.footer.configure(text='''Copyright Pratik GT 2020 All Rights Reserved | Py Tech''')

top.mainloop()
