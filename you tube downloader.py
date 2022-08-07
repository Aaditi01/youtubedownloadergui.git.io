from tkinter import*
from tkinter import filedialog
from moviepy import*
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
#functions
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)
def download_file():
    get_link = link_field.get()


    user_path = path_label.cget("text")
    screen.title('Downloading')
    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video,user_path)
    screen.title('Download Complete ! Download Another File ....')

screen=Tk()
title = screen.title("Youtube Download")
canvas = Canvas(screen,width=500,height=500)
canvas.pack()
#image logo
logo_img = PhotoImage(file='imgy.png')
 #resize
logo_img = logo_img.subsample(3,3)
canvas.create_image(250,100,image= logo_img)

#link feild
link_field = Entry(screen,width=50,font=('Arial',15))
link_label = Label(screen, text="Enter Download Link:",font=('Arial',15),padx='22')
#select path for saving the file
path_label = Label(screen,text="Select Path for Download",font=('Arial',15))
select_btn = Button(screen,text="Select",bg='green',padx='22',pady='5',font=('Arial',15),fg='#fff',command=select_path)
#add to window
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_btn)
#add widgets to window
canvas.create_window(250,190,window =link_label)
canvas.create_window(250,240,window=link_field)
#download buttons
download_btn = Button(screen,text="Download file",bg='green',padx='22',pady='5',font=('Arial',15),fg='#fff',command=download_file)
#add to canvas
canvas.create_window(250,390,window=download_btn)
screen.mainloop()