
import numpy as np
import pygame as py
import scipy.io.wavfile as wav
from scipy.io.wavfile import write
from tkinter import *
import time
from pygame import mixer
root = Tk()
root.geometry('450x180')
root.title("Synth")

mixer.init()


def C():
    mixer.music.load("C.wav")
    mixer.music.play()
    time.sleep(0.5)

    mixer.music.stop()
def Db():
    mixer.music.load("C#.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def D():
    mixer.music.load("D.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def Eb():
    mixer.music.load("D#.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def E():
    mixer.music.load("E.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def F():
    mixer.music.load("F.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def Gb():
    mixer.music.load("F#.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def G():
    mixer.music.load("G.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def Ab():
    mixer.music.load("G#.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def A():
    mixer.music.load("A.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def Bb():
    mixer.music.load("A#.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def B():
    mixer.music.load("B.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()

def C2():
    mixer.music.load("C2.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def Db2():
    mixer.music.load("C#2.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def D2():
    mixer.music.load("D2.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def Eb2():
    mixer.music.load("D#2.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def E2():
    mixer.music.load("E2.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def F2():
    mixer.music.load("F2.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()
def Gb2():
    mixer.music.load("F#2.wav")
    mixer.music.play()
    time.sleep(0.3)
    mixer.music.stop()

        
b = Button(root, height=10, width=5, command=C, bg="white")
b.grid(row=0,column=1)

b2 = Button(root, height=10, width=5, command=D, bg="white")
b2.grid(row=0,column=2)

b3 = Button(root, height=10, width=5, command=E, bg="white")
b3.grid(row=0,column=3)

b4 = Button(root, height=10, width=5, command=F, bg="white")
b4.grid(row=0,column=4)

b5 = Button(root, height=10, width=5, command=G, bg="white")
b5.grid(row=0,column=5)

b6 = Button(root, height=10, width=5, command=A, bg="white")
b6.grid(row=0,column=6)

b7 = Button(root, height=10, width=5, command=B, bg="white")
b7.grid(row=0,column=7)

b8 = Button(root, height=10, width=5, command=C2, bg="white")
b8.grid(row=0,column=8)

b9 = Button(root, height=10, width=5, command=D2, bg="white")
b9.grid(row=0,column=9)

b10 = Button(root, height=10, width=5, command=E2, bg="white")
b10.grid(row=0,column=10)

#b11 = Button(root, height=10, width=5, command=F2, bg="white")
#b11.grid(row=0,column=11)

a1 = Button(root, command=Db, width=2, height=6, bg="black")
a1.place(x=32,y=0)

a2 = Button(root, command=Eb, width=2, height=6, bg="black")
a2.place(x=77,y=0)

a3 = Button(root, command=Gb, width=2, height=6, bg="black")
a3.place(x=167,y=0)

a4 = Button(root, command=Ab, width=2, height=6, bg="black")
a4.place(x=213,y=0)

a5 = Button(root, command=Bb, width=2, height=6, bg="black")
a5.place(x=257,y=0)

a6 = Button(root, command=Db2, width=2, height=6, bg="black")
a6.place(x=347,y=0)

a7 = Button(root, command=Eb2, width=2, height=6, bg="black")
a7.place(x=393,y=0)

#a8 = Button(root, command=Gb2, width=2, height=6, bg="black")
#a8.place(x=478,y=0)

    
    


root.mainloop()






