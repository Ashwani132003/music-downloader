
from pytube import YouTube
from tkinter import filedialog

from tkinter import * 
import os


root = Tk()
root.geometry('800x800')
root.title('Siwach Youtube music Downloader')


try:
    def func(default=''):
        def Download():
            out_file = video.download(output_path='.')

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            d=Label(text='Download Completed!!', font=('Times',20,'normal'), fg='Red' ) 
            d.place(relx=0.5, rely=0.375, anchor=CENTER)

            
        url=link.get()
        
        try:
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            
            
        except:
            l=Label(text='Please Enter a valid Url', font=('Times',20,'normal'), fg='Red' ) 
            l.place(relx=0.5, rely=0.375, anchor=CENTER)
            
        else:
            
            D_button = Button(root, text='Download',font=('Times',20,'normal'),command=Download)
            D_button.place(relx=0.5, rely=0.375, anchor=CENTER)
except:
    print('Error Occured')    



welcome = Label(text='Youtube Video Downloader', fg='White', bg='Red', font=('Times',28,'normal'),width=22)
welcome.place(relx=0.5, rely=0.155, anchor=CENTER)

link = Entry(width = 20, borderwidth=3, font=('Times',24,'normal'), justify=CENTER, bg='yellow')
link.insert(0, 'Enter Url')

link.place(relx=0.5, rely=0.275, anchor=CENTER)

enter = Button(root, text='Enter', fg='White', bg='Red', font=('Times',16,'normal'), command=func)
enter.place(relx=0.7, rely=0.275, anchor=CENTER)    
    

root.bind('<Return>',func)

root.mainloop()