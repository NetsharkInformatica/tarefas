import tkinter as tk
from tkinter import ttk, font,messagebox
from tkinter import PhotoImage

# criar janela

janela = tk.Tk()
janela.title('meu app de tarefas')
janela.config(bg="#F0F0F0")
'''dimensoes da minha janela'''
janela.geometry("600x650")
'''criar cabeçalho'''
fonte_cabecalho=font.Font(family="Arial",size=24, weight="bold")
rotulo_cabecalho= tk.Label(janela,text="meu app de tarefas",
                           font=fonte_cabecalho,bg="#f0f0f0",fg="#333").pack(padx=10)

'''criando funções'''
frame_em_edicao= None

def adicionar_tarefa():
     global frame_em_edicao
     tarefa = entrada_tarefa.get().strip()
     if tarefa and tarefa !="Escreva sua tarefa aqui":
         if frame_em_edicao is not None:
             atualizar_tarefa(tarefa)
             frame_em_edicao=None
         else:
             adicionar_item_tarefa(tarefa)
         entrada_tarefa.delete(0,tk.END)
     else:
         messagebox.showwarning("Entrada de dados inválida!!, por favor insira uma tarefa valida")
         
#carregar icones

icon_editar= PhotoImage(file="imgs/editar.png").subsample(20,20)
icon_deletar=PhotoImage(file="imgs/delete.png").subsample(20,20)
         
def adicionar_item_tarefa(tarefa):
    frame_tarefa=tk.Frame(canvas_interior,bg="#fff",bd=1,relief=tk.SOLID)
    label_tarefa=tk.Label(frame_tarefa,text=tarefa,font=("Arial",16),bg="#fff",width=30,height=2,anchor="w")
    label_tarefa.pack(side=tk.LEFT,padx=10,pady=5,fill=tk.X)
    
    botao_edicao=tk.Button(frame_tarefa,image=icon_editar,command=lambda 
                           f=frame_tarefa,l=label_tarefa:preparar_edicao(f,l),bg="#FFF",relief=tk.FLAT)
    botao_edicao.pack(side=tk.RIGHT,padx=5)
    
    botao_deletar=tk.Button(frame_tarefa,image=icon_deletar,command=lambda 
                            f=frame_tarefa:deletar_tarefa(f),bg="#fff",relief=tk.FLAT)
    botao_deletar.pack(side=tk.RIGHT,padx=5)
    
    frame_tarefa.pack(fill=tk.X,padx=5,pady=5)
    
    botao_check=ttk.Checkbutton(frame_tarefa,command=lambda 
                                label=label_tarefa:alternar_sublinhado(label))
    botao_check.pack(side=tk.LEFT,padx=5)
    
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    
    
def preparar_edicao(frame_tarefa,label_tarefa):
    global frame_em_edicao
    frame_em_edicao= frame_tarefa
    entrada_tarefa.delete(0,tk.END)
    entrada_tarefa.insert(0,label_tarefa.cget("text"))
    

def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao
    for widget in frame_em_edicao.winfo_children():
        if isinstance(widget,tk.Label):
            widget.config(text=nova_tarefa)
        
   

def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    

def alternar_sublinhado(label):
    fonte_atual = label.cget("font")
    if "overstrike" in fonte_atual:
        nova_fonte=fonte_atual.replace(" overstrike","")
    else:
        nova_fonte=fonte_atual + " overstrike"
    label.config(font=nova_fonte)
    
       

#criando o frame

frame=tk.Frame(janela,bg="#f0f0f0")
frame.pack(padx=10)

#criar local de entrada da tarefa no frame

entrada_tarefa=tk.Entry(frame,font=("Arial",14),relief=tk.FLAT,bg="#fff",fg="gray",width=30)
entrada_tarefa.pack(side=tk.LEFT,pady=10,padx=10)

#criar botao adicionar tarefa

botao_adicionar=tk.Button(frame,command=adicionar_tarefa,text="adicionar tarefa",bg="#4caf50",
                          fg="#FFF",height=1,width=15,
                          font=("Arial",15),relief=tk.FLAT,padx=10)
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

'''criando funções'''






janela.mainloop()