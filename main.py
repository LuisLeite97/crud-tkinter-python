from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkcalendar import Calendar, DateEntry
from datetime import date

from PIL import Image, ImageTk


co0 = "#2e2d2b" #preto
co1 = "#feffff" #branco
co2 = "#038cfc" #azul
co3 = "#403d3d" #letras
bkg = "#045F7F" 

#classe define janela

janela = Tk()

janela.geometry('700x400')
class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frame_principal()
        janela.mainloop()
    def tela(self):
        self.janela.title('SySenior')
        self.janela.geometry('700x400')
        self.janela.configure(background=bkg)
        self.janela.resizable(width=FALSE, height=FALSE)
    def frame_principal(self):
        self.frame = Frame(self.janela, bd=4, bg='white',
                           highlightbackground='lightgray', highlightthickness=2)
        self.frame.place(relx= 0.02,rely=0.02, relwidth=0.96, relheight=0.5)
        self.frame_lista = Frame(self.janela, bd=4, bg='white',
                           highlightbackground='lightgray', highlightthickness=2)
        self.frame_lista.place(relx= 0.02,rely=0.53, relwidth=0.96, relheight=0.3)

'''style = ttk.Style(janela)
style.theme_use("clam")'''

Application()

