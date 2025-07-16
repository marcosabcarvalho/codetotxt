import os
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkthemes import ThemedTk
from tkinter import ttk

CONFIG_FILE = os.path.expanduser("~/.ultimo_diretorio.txt")

def carregar_ultimo_diretorio():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return f.read().strip()
    return os.path.expanduser("~/Documents")

def salvar_diretorio(diretorio):
    with open(CONFIG_FILE, "w") as f:
        f.write(diretorio)

def gerar_listagem(diretorio):
    nome_diretorio = os.path.basename(diretorio.rstrip("/"))
    arquivo_saida = os.path.join(os.path.expanduser("~"), f"{nome_diretorio}.txt")
    
    with open(arquivo_saida, "w", encoding="utf-8") as f_out:
        for root, _, arquivos in os.walk(diretorio):
            for nome_arquivo in arquivos:
                caminho_completo = os.path.join(root, nome_arquivo)
                try:
                    with open(caminho_completo, "r", encoding="utf-8") as f_in:
                        f_out.write(f"--- {caminho_completo} ---\n")
                        f_out.write(f_in.read())
                        f_out.write("\n\n")
                except Exception as e:
                    f_out.write(f"--- {caminho_completo} ---\n")
                    f_out.write(f"[Erro ao ler arquivo: {e}]\n\n")
    
    return arquivo_saida

def escolher_diretorio():
    ultimo = carregar_ultimo_diretorio()
    diretorio = filedialog.askdirectory(initialdir=ultimo, title="Escolha um diretório")
    if diretorio:
        salvar_diretorio(diretorio)
        caminho_saida = gerar_listagem(diretorio)
        messagebox.showinfo("Concluído", f"Arquivo '{caminho_saida}' gerado com sucesso!")

def main():
    app = ThemedTk(theme="arc")
    app.title("Gerador de Arquivo de Diretório")
    app.geometry("400x150")

    ttk.Label(app, text="Gerar lista de arquivos com conteúdo", font=("Arial", 12)).pack(pady=20)
    ttk.Button(app, text="Selecionar Diretório", command=escolher_diretorio).pack()

    app.mainloop()

if __name__ == "__main__":
    main()
