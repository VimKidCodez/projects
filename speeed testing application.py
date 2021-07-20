from tkinter import *
from speedtest import Speedtest
from tkinter import messagebox


def upade_text():
    speedtest = Speedtest()
    download = speedtest.download()
    upload = speedtest.upload()
    downloadspeed = round(download / (10**6),2)
    uploadspeed = round(upload / (10**6),2)
    downloadLabel.config(test = "Download speed is: "+ str(downloadspeed)+"Mbps")
    uploadLabel.config(test="Apload speed is: " + str(downloadspeed) + "Mbps")

root = Tk()
root.title('internet speed tester')
def popup()
    messagebox.showinfo("help","for further details pls conyract sdsriram@gmal.com")


Button(root,text = "help",command = popup).pack()

button = Button(root,text = "chech wat is my speed",width= 30,command=upade_text)
button.pack()

downloadLabel(root,text = "")
    