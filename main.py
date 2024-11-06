import tkinter as tk
from tkinter import messagebox
import requests as rq 
from ttkbootstrap import Style


janela = tk.Tk()
janela.title("Informações Meteorológica")
janela.geometry("600x400")
style = Style(theme="darkly")
style.theme_use("darkly")
janela.resizable( False, False)
fontes = ("verdana", 12)

#Funções
def pegar_dados(cidade: str):
    chave_API = "58f5d3f893621ea2078657cd523e52bb"
    lang = "pt"
    ls = [lbl_pressao_1,lbl_resutado_1, lbl_resutado_2, lbl_vento_1]
    verde = "green"
    for i in ls:
        i["fg"]= verde
        i["font"]= ("verdana", 10, "bold")
    try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_API}&units=metric&lang={lang} "
            resposta = rq.get(url)
            dados = resposta.json()
            lbl_resutado_1["text"] = f'{dados["main"]["temp"]} ̣CELSO'
            lbl_resutado_2["text"] = f'{dados["main"]["humidity"]}%'
            lbl_pressao_1["text"] = f'{dados["main"]["pressure"]} Pa'
            lbl_vento_1["text"] = f'{dados["wind"]["speed"]} m/s'
            lbl_nome["text"] = dados["name"]
    except:
        messagebox.showwarning("AVISO", "Cidade Inválida\nOu\nVerifica a Conexão.")


lb_principal = tk.Label(janela,font = ("verdana", 20, "bold"), text = "METEOROLOGIA")
lb_principal.pack(pady = 30)

lb_info = tk.Label(janela, text = "Insira aqui o nome da Cidade:")
lb_info.pack()

en_cidade = tk.Entry(janela, width = 30)
en_cidade.pack()

    
btb_buscar = tk.Button(janela, font = ("verdana", 14, "bold"),command = lambda: pegar_dados(en_cidade.get()), text = "BUSCAR")
btb_buscar.pack(pady = 20)

frm_1 = tk.Frame(janela)
#Temperatura
lbl_temperatura = tk.Label(frm_1, font =fontes, text = "Temperatura")
lbl_temperatura.grid(row = 0, column = 0)
lbl_resutado_1 = tk.Label(frm_1)
lbl_resutado_1.grid(row = 1, column = 0  )

#Velocidade do vento
lbl_vento = tk.Label(frm_1,font =fontes, text = "Velocidade do Vento")
lbl_vento.grid(row = 2, column = 0)
lbl_vento_1 = tk.Label(frm_1)
lbl_vento_1.grid(row = 3, column = 0)

#Humidade
lbl_umidade = tk.Label(frm_1,font =fontes, text = "Humidade")
lbl_umidade.grid(row = 0, column = 1, padx = 20)
lbl_resutado_2 = tk.Label(frm_1)
lbl_resutado_2.grid(row = 1, column = 1, padx = 20 )

#Pressão
lbl_pressao = tk.Label(frm_1,font =fontes, text = "Pressão")
lbl_pressao.grid(row = 2, column = 1, padx = 20)
lbl_pressao_1 = tk.Label(frm_1)
lbl_pressao_1.grid(row = 3, column = 1, padx = 20 )
frm_1.pack()

lbl_nome = tk.Label(janela, font = ("verdana", 13, "bold"))
lbl_nome.pack()



janela.mainloop()