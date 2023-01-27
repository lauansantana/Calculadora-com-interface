from tkinter import *
from tkinter import ttk

#Cores
cor_fundo = '#12141f' #preto azulado
cor_fundo2 = '#21222c' #azul escuro
cor_branco = '#ffffff'
cor_roxo = '#4f3fc7'
cor_cinza = '#17181c'

#Janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("236x310")
janela.config(bg=cor_fundo2)

#Tela
tela = Frame(janela, width=235, height=50, bg=cor_fundo)
tela.grid(row=0, column=0)

corpo = Frame(janela, width=235, height=268)
corpo.grid(row=1, column=0)

#variavel valores
valores = ''

valor_texto = StringVar()

#Funçao
def entrada_valores(event):
    global valores

    valores = valores+str(event)
    valor_texto.set(valores) #passando valor para a tela

#funçao calculo
def calculo():
    global valores
    resultado = eval(valores)

    valor_texto.set (str(resultado))
    #print(resultado)

#funçao limpar
def limpar():
    global valores
    valores = ""
    valor_texto.set('')


#Fonte da tela
#valor_texto = StringVar()
app_label = Label(tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font='ivy 17 bold', bg=cor_fundo, fg=cor_branco )
app_label.place(x=0, y=0)

# Botoes
# Linha de botoes 1
b1 = Button(corpo, command= limpar, text="C", width=11, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(corpo, command= lambda: entrada_valores('%'), text="%", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=120, y=0)
b3 = Button(corpo, command= lambda: entrada_valores('/'), text="÷", width=5, height=2, bg=cor_roxo, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=180, y=0)

#Linha de botoes 2
b4 = Button(corpo, command= lambda: entrada_valores('7'), text="7", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(corpo, command= lambda: entrada_valores('8'), text="8", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=60, y=52)
b6 = Button(corpo, command= lambda: entrada_valores('9'), text="9", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=120, y=52)
b7 = Button(corpo, command= lambda: entrada_valores('*'), text="*", width=5, height=2, bg=cor_roxo, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=180, y=52)

#Linha de botoes 3
b8 = Button(corpo, command= lambda: entrada_valores('4'), text="4", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(corpo, command= lambda: entrada_valores('5'), text="5", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=60, y=104)
b10 = Button(corpo, command= lambda: entrada_valores('6'), text="6", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=120, y=104)
b11 = Button(corpo, command= lambda: entrada_valores('-'), text="-", width=5, height=2, bg=cor_roxo, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=180, y=104)

#Linha de botoes 4
b12 = Button(corpo, command= lambda: entrada_valores('1'), text="1", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(corpo, command= lambda: entrada_valores('2'), text="2", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=60, y=156)
b14 = Button(corpo, command= lambda: entrada_valores('3'), text="3", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=120, y=156)
b15 = Button(corpo, command= lambda: entrada_valores('+'), text="+", width=5, height=2, bg=cor_roxo, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=180, y=156)

#Linha de botoes 5
b16 = Button(corpo, command= lambda: entrada_valores('0'), text="0", width=11, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(corpo, command= calculo, text="=", width=5, height=2, bg=cor_roxo, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=180, y=208)
b18 = Button(corpo, command= lambda: entrada_valores('.'), text=".", width=5, height=2, bg=cor_fundo2, fg=cor_branco, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=120, y=208)

janela.mainloop()