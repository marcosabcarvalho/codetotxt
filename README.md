
Segue como você pode persistir seu Personal Access Token (PAT) para não ter que digitá‑lo a cada push ou clone:
git config --global credential.helper store




# src2txt

Um utilitário gráfico em Python para gerar um arquivo `.txt` com a listagem de todos os arquivos de um diretório (e opcionalmente seus subdiretórios), incluindo o conteúdo de cada um.

## Descrição

O **src2txt** apresenta uma interface simples (Tkinter + ttkthemes) que permite:

- Navegar interativamente até o diretório desejado (padrão: `~/Documents`).
- Persistir a última pasta aberta para agilizar usos futuros.
- Escolher, via checkbox, se a busca deve incluir subdiretórios ou ficar apenas na raiz.
- Gerar um arquivo de saída na sua pasta home, com o mesmo nome do diretório selecionado (`<NomeDoDiretório>.txt`), contendo:
  - O caminho completo de cada arquivo.
  - O conteúdo textual (UTF‑8) de cada arquivo.
  - Mensagens de erro para arquivos não legíveis (binários, sem permissão etc.).

Ideal para auditoria de código‑fonte, revisão de projetos, criação de backups em texto ou análise de conteúdos sem sair da linha de comando clássica.

## Funcionalidades

- ✔️ UI leve e temática (ttkthemes “arc”)
- ✔️ Persistência automática da última pasta usada
- ✔️ Checkbox para ativar/desativar varredura recursiva
- ✔️ Relatório único com estrutura clara e mensagens de erro contextualizadas

## Requisitos

- Python 3.8+  
- Módulos:
  - `ttkthemes`
  - `tkinter` (já incluído no pacote padrão do Python)
- Sistema Linux/Ubuntu (testado em Python 3.11 com PEP 668 habilitado)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://seu-repo.git
   cd nome-do-projeto




