from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        super().__init__()
        self.fonte = ("Arial", 20)
        
        self.title("Database Connection")
        self.geometry("1280x720")
        self.sidebar()
        self.tela_boas_vindas()
        self.create_tela_cadastro()
        self.create_tela_consulta()
        
    def sidebar(self):
        self.sidebar_frame = Frame(self, width=100, bg='lightgray')
        self.sidebar_frame.pack(side=LEFT, fill=Y)
        
        self.button1 = Button(self.sidebar_frame, text = "Cadastrar", command=self.tela_cadastro, font=self.fonte)
        self.button1.pack(pady = 10)
        
        self.button2 = Button(self.sidebar_frame, text = "Consultar", command=self.tela_consulta, font=self.fonte)
        self.button2.pack(pady = 10)

    def tela_boas_vindas(self):
        self.tela_boas_vindas_frame = Frame(self, bg='white')
        self.tela_boas_vindas_frame.pack(fill=BOTH, expand=True)
        
        self.label = Label(self.tela_boas_vindas_frame, text="Bem-vindo ao sistema de cadastro e consulta!", font=self.fonte, bg='white')
        self.label.pack(pady=20)     
           
    def create_tela_cadastro(self):
        self.tela_cadastro_frame = Frame(self, bg='white')
        
        Label(self.tela_cadastro_frame, text="Tela de Cadastro", font=self.fonte, bg='white').pack(pady=20)
        
    def create_tela_consulta(self):
        self.tela_consulta_frame = Frame(self, bg='white')
        
        Label(self.tela_consulta_frame, text="Tela de Consulta", font=self.fonte, bg='white').pack(pady=20)
        
    def tela_cadastro(self):
        self.tela_boas_vindas_frame.pack_forget()
        self.tela_consulta_frame.pack_forget()
        self.tela_cadastro_frame.pack(fill=BOTH, expand=True)
    
    def tela_consulta(self):
        self.tela_boas_vindas_frame.pack_forget()
        self.tela_cadastro_frame.pack_forget()
        self.tela_consulta_frame.pack(fill=BOTH, expand=True)

app = App()
app.mainloop()