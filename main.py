# importação das libs 


from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#  Cores

cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"   # letra / letters

# Criação da janela

window = Tk()
window.title('Login')
window.geometry('310x300')
window.configure(bg=cor1)
window.minsize(310, 300)
window.maxsize(310, 300)

# Credenciais Fixas

credentials= ['junior', '123456']

# Função de verificar login

def verify():
    name = entry_name.get()
    password = entry_password.get()

    if name == 'admin' and password == 'admin':
        messagebox.showinfo('Login', 'Seja bem viado Admin !!')
    elif credentials[0] == name and credentials[1] == password:
        messagebox.showinfo('Login', f'Seja bem vindo {credentials[0]} !!')
        
        #deletar itens dentro dos frames baixa e cima
        for w in frame_down.winfo_children():
            w.destroy()
        for w in frame_up.winfo_children():
            w.destroy()

        new_window()
    else:
        messagebox.showwarming('Erro', 'O nome ou senha estão incorretos !!')

# Nova janela

def new_window():
    # Configurar o frame de cima

    label_title = Label(frame_up, text=f'Usuario: {credentials[0]}', anchor=NE, font=('Ivy', 25, 'bold'), bg=cor1, fg=cor4)
    label_title.place(
        x=5,
        y=5
    )

    label_line = Label(frame_up, text='', width=275, font=('Ivy', 1, 'bold'), bg=cor2)
    label_line.place(
        x=10,
        y=45
    )

    label_title = Label(frame_down, text=f'Seja bem vindo {credentials[0]}', anchor=NE, font=('Ivy', 18, 'bold'), bg=cor1, fg=cor4)
    label_title.place(
        x=5,
        y=105
    )


# Frame de cima

frame_up = Frame(window, width=310, height=50, bg=cor1, relief='flat')
frame_up.grid(
    row=0,
    column=0,
    pady=1,
    padx=0,
    sticky=NSEW
)

# Configurar o frame de cima

label_title = Label(frame_up, text='LOGIN', anchor=NE, font=('Ivy', 25, 'bold'), bg=cor1, fg=cor4)
label_title.place(
    x=5,
    y=5
)

label_line = Label(frame_up, text='', width=275, font=('Ivy', 1, 'bold'), bg=cor2)
label_line.place(
    x=10,
    y=45
)

# Frame de baixo

frame_down = Frame(window, width=310, height=250, bg=cor1, relief='flat')
frame_down.grid(
    row=1,
    column=0,
    pady=1,
    padx=0,
    sticky=NSEW
)

# Configurar o frame de baixo

label_name = Label(frame_down, text='Nome *', anchor=NW, font=('futura', 10, 'bold'), bg=cor1, fg=cor4)
label_name.place(
    x=10,
    y=20
)

entry_name = Entry(frame_down, width=25, justify='left', font=('futura', 15), highlightthickness=1, relief='solid')
entry_name.place(
    x=15,
    y=50
)

label_password = Label(frame_down, text='Senha *', anchor=NW, font=('futura', 10, 'bold'), bg=cor1, fg=cor4)
label_password.place(
    x=10,
    y=95
)

entry_password = Entry(frame_down, width=25, justify='left', show='*', font=('futura', 15), highlightthickness=1, relief='solid')
entry_password.place(
    x=14,
    y=130
)

btn_login = Button(frame_down, text='Entrar', command=verify, width=39, height=2, font=('futura', 8, 'bold'), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
btn_login.place(
    x=15,
    y=180
)


window.mainloop()