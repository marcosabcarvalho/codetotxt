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

def gerar_listagem(diretorio, incluir_subdirs):
    nome_diretorio = os.path.basename(diretorio.rstrip("/"))
    arquivo_saida = os.path.join(os.path.expanduser("~"), f"{nome_diretorio}.txt")

    with open(arquivo_saida, "w", encoding="utf-8") as f_out:
        if incluir_subdirs:
            # percorre tudo, incluindo subdiretórios
            for root, _, arquivos in os.walk(diretorio):
                for nome_arquivo in arquivos:
                    escrever_arquivo(root, nome_arquivo, f_out)
        else:
            # apenas diretório principal
            for nome_arquivo in os.listdir(diretorio):
                caminho = os.path.join(diretorio, nome_arquivo)
                if os.path.isfile(caminho):
                    escrever_arquivo(diretorio, nome_arquivo, f_out)

    return arquivo_saida

def escrever_arquivo(root, nome_arquivo, f_out):
    caminho_completo = os.path.join(root, nome_arquivo)
    try:
        with open(caminho_completo, "r", encoding="utf-8") as f_in:
            f_out.write(f"--- {caminho_completo} ---\n")
            f_out.write(f_in.read())
            f_out.write("\n\n")
    except Exception as e:
        f_out.write(f"--- {caminho_completo} ---\n")
        f_out.write(f"[Erro ao ler arquivo: {e}]\n\n")

def escolher_diretorio():
    ultimo = carregar_ultimo_diretorio()
    diretorio = filedialog.askdirectory(initialdir=ultimo, title="Escolha um diretório")
    if not diretorio:
        return
    salvar_diretorio(diretorio)
    incluir = var_incluir.get()
    caminho_saida = gerar_listagem(diretorio, incluir)
    messagebox.showinfo("Concluído",
        f"Arquivo '{caminho_saida}' gerado com sucesso!\n"
        f"{'Incluiu' if incluir else 'Não incluiu'} subdiretórios."
    )

def main():
    app = ThemedTk(theme="arc")
    app.title("Gerador de Arquivo de Diretório")
    app.geometry("450x200")

    frame = ttk.Frame(app, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Gerar lista de arquivos com conteúdo", font=("Arial", 12)).pack(pady=(0,10))

    global var_incluir
    var_incluir = tk.BooleanVar(value=True)
    chk = ttk.Checkbutton(
        frame,
        text="Incluir subdiretórios",
        variable=var_incluir
    )
    chk.pack(anchor="w", pady=(0,10))

    ttk.Button(frame, text="Selecionar Diretório", command=escolher_diretorio).pack()

    app.mainloop()

if __name__ == "__main__":
    main()
