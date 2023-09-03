import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# CARACTERIZANDO A PÁGINA -------------------

window = tkinter.Tk()
window.title("Registre-se")

frame = tkinter.Frame(window)
frame.pack()


# FUNÇÃO DE MENSAGENS ----------------------------------    
 
#def enter_data():
    #accept = validacao_var.get()
    #if accept == "Aceito":
        ##Informacao do user ----------
        #primeiro_nome = primeiro_nome_input.get()
        #sobrenome = sobrenome_input.get()
        #if primeiro_nome and sobrenome and email:
            #cargo = cargo_combobox.get()
           # sexo = sexo_combobox.get()

            ##Informacoes do cargo ----
           # resgistrado_label = reg_status_var.get()

            #tkinter.messagebox.showinfo(title="Finalizado", message="Resgistro de funcionário concluído!")

            #print("Primeiro nome:", primeiro_nome, "Sobrenome:", sobrenome)
            #print("Cargo:", cargo, "Sexo:", sexo)
            #print("Status de Registro:", resgistrado_label)
            #print("-"*50)

        #else:
            #tkinter.messagebox.showwarning(title="Erro", message="Primeiro nome e Sobrenome obrigatórios")

    #else:
        #tkinter.messagebox.showwarning(title="Ocorreu um erro", message="Você não aceitou os termos da empresa")

#
# FUNÇAO EPIS -----------------------------------------

def epi(): # Função que deu certo -> porém mostra em OUTRA janela -> fazer ajustes sobre EPIs

    print("dentro do epi ")

    cargo = cargo_combobox.get()

    if cargo == "Produção":
        tkinter.messagebox.showinfo(title="Equipamentos", message="""Equipamentos necessários:
-> Luvas
-> Capacetes
-> Coletes
-> Óculos""")

    elif cargo == "":
        tkinter.messagebox.showinfo(title="Equipamentos", message="""Selecione um cargo para saber o equipamento necessário!""")

    elif cargo == "Supervisor":
        tkinter.messagebox.showinfo(title="Equipamentos", message="""Equipamentos necessários:
-> Capacetes""")

    elif cargo == "Produção Química":
        tkinter.messagebox.showinfo(title="Equipamentos", message="""Equipamentos necessários:

-> Luvas
-> Capacetes
-> Coletes
-> Botas
-> Óculos
-> Blusa""")

    elif cargo == "Soldador":
        tkinter.messagebox.showinfo(title="Equipamentos", message="""Equipamentos necessários:
                                   
-> Luvas
-> Capacetes
-> Coletes
-> Botas
-> Óculos""")


infoepi_frame = None

def epi2() : # Função deu certo
   
    print("dentro do epi 2")

    global infoepi_frame   # Acessar a variável global
   
    if infoepi_frame:  # Destruir o widget anterior, se existir
        infoepi_frame.destroy()

    infoepi_frame = tk.LabelFrame(frame, text="Equipamentos Necessários:")
    infoepi_frame.grid(row=2, column=0, padx=20, pady=20)

    cargo = cargo_combobox.get()


    if cargo == "Produção":
        epi_produ = tkinter.Label(infoepi_frame, text="""-> Protetor Auditivo\n       -> Óculos de Segurança\n           -> Capacete de Segurança\n    -> Luvas de Segurança\n -> Botas de Proteção\n              -> Máscaras ou Respiradores""")
        epi_produ.grid(row=0, column=2, padx=25)

   
    elif cargo == "":
        epi_produ = tkinter.Label(infoepi_frame, text="-> Selecione algum cargo ")
        epi_produ.grid(row=0, column=2, padx=62)
   
    elif cargo == "Soldador":
        epi_produ = tkinter.Label(infoepi_frame, text="""    -> Luvas de Segurança\n-> Protetor Auditivo\n-> Avental de Raspa\n                  -> Calçado de Segurança          \n    -> Óculos de Proteção\n                        -> Respirador de Soldagem            """)
        epi_produ.grid(row=0, column=2)
   
    elif cargo == "Supervisor":      
        epi_produ = tkinter.Label(infoepi_frame, text="""-> Capacetes\n                   -> Coletes de Segurança\n                -> Óculos de Proteção""")
        epi_produ.grid(row=0, column=2, padx=30)
   
    elif cargo == "Produção Química":        
        epi_produ = tkinter.Label(infoepi_frame, text="""-> Luvas Laboratoriais\n      -> Aventais de Segurança\n           -> Máscaras ou Respiradores\n-> Óculos de Proteção\n  -> Macacões Químicos\n                  -> Toucas para Segurar o Cabelo""")
        epi_produ.grid(row=0, column=2, padx=10)



#------------------------------------------------1ª PARTE------------------------------------------------

# TITULO ------------------------------------

infouser_frame = tkinter.LabelFrame(frame, text="Informações Pessoais")
infouser_frame.grid(row=0, column=0, padx=20, pady=20)

# INSERIR O NOME E SOBRENOME ----------------

primeiro_nome = tkinter.Label(infouser_frame, text="Nome *")
primeiro_nome.grid(row=0, column=0)
sobrenome = tkinter.Label(infouser_frame, text="Sobrenome *")
sobrenome.grid(row=0, column=1)
primeiro_nome_input = tkinter.Entry(infouser_frame)
sobrenome_input = tkinter.Entry(infouser_frame)
primeiro_nome_input.grid(row=1, column=0)
sobrenome_input.grid(row=1, column=1)

# INSERIR O SEXO ----------------------------

sexo = tkinter.Label(infouser_frame, text="Sexo")
sexo_combobox = ttk.Combobox(infouser_frame,values=[ "", "Feminino", "Masculino", "Prefiro não dizer"])
sexo.grid(row=0, column=2)
sexo_combobox.grid(row=1, column=2)


# INSERIR SENHA E EMAIL --------------------

email = tkinter.Label(infouser_frame, text="Email")
email.grid(row=2, column=0)
senha = tkinter.Label(infouser_frame, text="Senha")
senha.grid(row=2, column=1)

atencao = tkinter.Label(infouser_frame, text="""* OBSERVAÇÃO *
-> A senha NÃO é do email,
mas sim a que será usada no seu LOGIN!!""", foreground= "red")
atencao.grid(row=4, column=1)

email_input = tkinter.Entry(infouser_frame)
email_input.grid(row=3, column=0)
senha_input = tkinter.Entry(infouser_frame)
senha_input.grid(row=3, column=1)

#Para todos os capos de informação de usuário, ele adiciona um espaçamento -------------

for widget in infouser_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



#------------------------------------------------2ª PARTE------------------------------------------------

# TITULO ------------------------------------

infojob_frame = tkinter.LabelFrame(frame, text="Ocupação no Trabalho")
infojob_frame.grid(row=1, column=0, padx=20, pady=20)

# CARGO -------------------------------------

cargo = tkinter.Label(infojob_frame, text="Área de atuação")
cargo_combobox = ttk.Combobox(infojob_frame,values=[ "", "Produção", "Supervisor", "Produção Química", "Soldador"])
cargo.grid(row=1, column=0)
cargo_combobox.grid(row=2, column=0)


botao = tkinter.Button(infojob_frame, text="Saber EPIs", command= epi2) # Pode mudar a funçao
botao.grid(row=2, column=1, sticky="news", padx=20, pady=20)

# STATUS DE REGISTRO?????? ------------------------

#### VERIFICAR SE É NECESSARIO ISSO
#resgistrado_label = tkinter.Label(infojob_frame, text="Status do registro")
#reg_status_var = tkinter.StringVar(value="Nao Registrado")
#registrado_check = tkinter.Checkbutton(infojob_frame, text="Ja registrado", variable=reg_status_var, onvalue="Registrado", offvalue="Nao Registrado")

# Adiciona um espaçamento -------------------

for widget in infojob_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



#------------------------------------------------3ª PARTE------------------------------------------------

# TERMOS E CONDIÇÕES ------------------------

termos_frame = tkinter.LabelFrame(frame, text="Termos e Condições *")
termos_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

validacao_var = tkinter.StringVar(value="Não aceito")
termos_check = tkinter.Checkbutton(termos_frame, text="Eu aceito os termos e condições", variable=validacao_var, onvalue="Aceito", offvalue="Nao Aceito")
termos_check.grid(row=0, column=0)



#------------------------------------------------4ª PARTE------------------------------------------------

#-----------------------------Implementando Firestore-----------------------------------

#-----------------------------ligando----------------------------------------------
cred = credentials.Certificate('ezpoint-cd326-firebase-adminsdk-6yfjv-7e14cc16f2.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

#------------------------------Estrutura----------------------------------------------

#primeiro_nome = primeiro_nome_input.get()
#sobrenome = sobrenome_input.get()
#cargo = cargo_combobox.get()
#sexo = sexo_combobox.get()

#fire = {
  #"nome": primeiro_nome,
  #"sobrenome": sobrenome,
  #"cargo": cargo,
  #"sexo": sexo
#}

#data = [fire]
#--------------------------------------Gravação-------------------------------------------
result = db.collection('Funcionarios').document("users").get()

#--------------------
def enter_data():
    accept = validacao_var.get()
    
    if accept == "Aceito":
        primeiro_nome = primeiro_nome_input.get()
        sobrenome = sobrenome_input.get()
        email = email_input.get()
        
        if primeiro_nome and sobrenome and email:
            cargo = cargo_combobox.get()
            sexo = sexo_combobox.get()

            result = db.collection('Funcionarios').where('email', '==', email).get()

            if len(result) == 0:
                fire = {
                    "nome": primeiro_nome,
                    "sobrenome": sobrenome,
                    "cargo": cargo,
                    "sexo": sexo,
                    "email": email
                }

                doc_ref = db.collection("Funcionarios").document()
                doc_ref.set(fire)

                tkinter.messagebox.showwarning(title="Sucesso", message="Registro feito com sucesso!!!")
            else:
                tkinter.messagebox.showwarning(title="Erro", message="Usuário já existente")
        else:
            tkinter.messagebox.showwarning(title="Ocorreu um erro", message="Nome, sobrenome e email são obrigatórios")
    else:
        tkinter.messagebox.showwarning(title="Ocorreu um erro", message="Você não aceitou os termos da empresa")

#-----------------------TESTES -- TESTES -- TESTES -- TESTES --------------------------
import tkinter.messagebox

def teste_print():
    emailteste = email_input.get()
    result = db.collection('Funcionarios').where('email', '==', emailteste).get()
    if len(result) == 0:
        tkinter.messagebox.showwarning(title="Erro", message="Login feito com sucesso!!!")
    else:
        tkinter.messagebox.showwarning(title="Erro", message="Usuário já existente")

    

# BOTÃO DE REGISTRO -------------------------

botao = tkinter.Button(frame, text="Registrar", command= enter_data)
botao.grid(row=4, column=0, sticky="news", padx=20, pady=20)






window.mainloop()