import tkinter as tk
from tkinter import ttk, font,messagebox
from tkinter import PhotoImage

# criar janela

janela = tk.Tk()
janela.title('meu app de tarefas')
janela.config(bg="#F0F0F0")
janela.geometry("600x650")
fonte_cabecalho=font.Font(family="Roboto",size=24, weight="bold")
rotulo_cabecalho= tk.Label(janela,text="meu app de tarefas",
                           font=fonte_cabecalho,bg="#f0f0f0",fg="#333").pack(padx=10)
#criando o frame

frame=tk.Frame(janela,bg="#f0f0f0")
frame.pack(padx=10)

#criar local de entrada da tarefa no frame

entrada_tarefa=tk.Entry(frame,font=("Roboto",14),relief=tk.FLAT,bg="#fff",fg="gray",width=30)
entrada_tarefa.pack(side=tk.LEFT,pady=10,padx=10)

#criar botao adicionar tarefa

botao_adicionar=tk.Button(frame,text="adicionar tarefa",bg="#4caf50",
                          fg="#FFF",height=1,width=15,font=("Garamond",15),relief=tk.FLAT,padx=10)
botao_adicionar.pack(padx=10,side=tk.LEFT)

#criar um frame para lista de tarefas com rolagem

frame_lista_tarefas= tk.Frame(janela,bg="#fff")
frame_lista_tarefas.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)
'''criar canvas de tarefas'''
canvas = tk.Canvas(frame_lista_tarefas,bg="#fff")
canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
#scrollbar
scrollbar=tk.Scrollbar(frame_lista_tarefas,orient="vertical",command=canvas.yview)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
'''configuração do scrollbar'''
canvas.configure(yscrollcommand=scrollbar.set)

'''criar um canva que será a parte interior do canvas principal, que receberá as tarefas'''
canvas_interior= tk.Frame(canvas,bg="#fff")
'''configurrar janela para que scrollbar reconheça'''
canvas.create_window((0,0),window=canvas_interior,anchor="nw")
canvas_interior.bind("<Configure>",lambda e:canvas.configure(scrollregion=canvas.bbox("all")))






janela.mainloop()