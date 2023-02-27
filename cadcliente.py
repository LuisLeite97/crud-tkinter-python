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
        self.frame_cadpaciente()
        self.buttonsframe()
        janela.mainloop()
        style=ttk.Style(janela)
        style.theme_use("clam")
    def tela(self):
        self.janela.title('SySenior')
        self.janela.geometry('700x400')
        self.janela.configure(background=co0)
        self.janela.resizable(width=FALSE, height=FALSE)
    def frame_cadpaciente(self):
        self.frame = Frame(self.janela, bd=4, bg='lightgray',
                           highlightbackground='lightgray', highlightthickness=2)
        self.frame.place(relx= 0.02,rely=0.02, relwidth=0.96, relheight=0.5)

        self.frame_lista = Frame(self.janela, bd=4, bg='white',
                           highlightbackground='lightgray', highlightthickness=2)
        self.frame_lista.place(relx= 0.02,rely=0.53, relwidth=0.96, relheight=0.3)
    def buttonsframe(self):
        #botão busca
        self.bt_limpar = Button(self.frame, text='Buscar', font=('verdana', 8))
        self.bt_limpar.place(relx=0.11, rely=0.06, relwidth=0.10, relheight=0.15)
        #botão limpar
        self.bt_buscar = Button(self.frame, text='Limpar', font=('verdana', 8))
        self.bt_buscar.place(relx=0.22, rely=0.06, relwidth=0.10, relheight=0.15)
        #botão novo     
        self.bt_novo = Button(self.frame, text='NOVO', bd=3, bg='lightgreen', font=('verdana', 10, 'bold'))
        self.bt_novo.place(relx=0.87, rely=0.01, relwidth=0.10, relheight=0.15)
        #botão alterar  
        self.bt_alterar = Button(self.frame, text='Alterar',font=('verdana', 8))
        self.bt_alterar.place(relx=0.87, rely=0.2, relwidth=0.10, relheight=0.15)
        #botão apagar       
        self.bt_Apagar = Button(self.frame, text='Apagar', bd=3,bg='indian red',font=('verdana', 8))
        self.bt_Apagar.place(relx=0.87, rely=0.4, relwidth=0.10, relheight=0.15)
        #label e insert de código para abrir cadastro
        self.lb_codigo = Label(self.frame, text = 'Código', background='lightgray')
        self.lb_codigo.place(relx=0.002, rely=0.001)

        self.codigo_entry = Entry(self.frame, background='lightgray')
        self.codigo_entry.place(relx=0.002, rely=0.1, relwidth=0.1, relheight=0.10)
        #label e insert de nome do paciente
        self.lb_nomepaciente = Label(self.frame, text = 'Nome Paciente:', background='lightgray')
        self.lb_nomepaciente.place(relx=0.002, rely=0.25)

        self.nomepaciente = Entry(self.frame)
        self.nomepaciente.place(relx=0.002, rely=0.36, relwidth=0.3, relheight=0.10)
        #label e insert CPF paciente
        self.lb_cpfpaciente = Label(self.frame, text = 'CPF:', background='lightgray')
        self.lb_cpfpaciente.place(relx=0.002, rely=0.46)

        self.cpfpaciente = Entry(self.frame)
        self.cpfpaciente.place(relx=0.002, rely=0.56, relwidth=0.2, relheight=0.10)
        #label e insert Telefone
        self.lb_fonepaciente = Label(self.frame, text = 'Telefone:', background='lightgray')
        self.lb_fonepaciente.place(relx=0.28, rely=0.46)

        self.fonepaciente = Entry(self.frame)
        self.fonepaciente.place(relx=0.28, rely=0.56, relwidth=0.2, relheight=0.10)
    def listaframe(self):
        self.listacliente = ttk.Treeview(self.frame_lista, height=3, columns=("col1", "col2", "col3"))
        self.listacliente.heading("#0", text="")
        self.listacliente.heading("#1", text="ID")
        self.listacliente.heading("#2", text="Nome")
        self.listacliente.heading("#3", text="Telefone")

'''style = ttk.Style(janela)
style.theme_use("clam")'''

Application()

