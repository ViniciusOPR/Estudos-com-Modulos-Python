# O módulo os para interação com o sistema
# Doc: https://docs.python.org/3/library/os.html
# O módulo `os` fornece funções para interagir com o sistema operacional.
# Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
# arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
# diretório. O método os.system() permite executar comandos do sistema
# operacional a partir do seu código Python.
# Windows 11 (PowerShell), Linux, Mac = clear
# Windows (antigo, cmd) = cls

import math
import os
from itertools import count

# os.system('cls')
os.system('echo "Hello world"')

print('a' * 20)
print('a' * 20)
print('a' * 20)

# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
print()
print('Trabalhando com OS.PATH - caminhos')

caminho = os.path.join('C:Users', 'Ouro Preto', 'Downloads', 'Titan Launcher')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)
print(os.path.exists(r'F:\\Estudos Python-HTML-SQL\\PythonRemake\\modulospython'))
print(os.path.abspath('.'))
print(diretorio, arquivo)
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))

# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
print()
print('Trabalhando com OS.LISTDIR')
caminho_nav = os.path.join('C:Users', 'Ouro Preto', 'Music', 'Giovani Tracks')

for pasta in os.listdir(caminho_nav):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for arquivos in os.listdir(caminho_completo_pasta):
        print(' ', arquivos)

# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
print()
print('Trabalhando com OS.WALK')

caminho_walk = os.path.join('C:Users', 'Ouro Preto', 'Music', 'Mellow Sonic')
counter = count()

for root, dirs, files in os.walk(caminho_walk):
    the_counter = next(counter)
    print(the_counter, 'Pasta Atual', root)

    for dir_ in dirs:
        print(' ', the_counter, 'DIR:', dir_)
    
    for file_ in files:
        print(' ', the_counter, 'FILE:', file_)

        # PARA VER CAMINHO COMPLETO DOS ARQUIVOS NAS PASTAS
        # caminho_completo_arquivo = os.path.join(root, file_)
        # print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)

# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
print()
print('Trabalhando com OS.STAT E OS.PATH.GETSIZE')

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

caminho_getsize_stat = os.path.join('D:Games', 'O Protetor - Capitulo Final 2023 1080p FULL HD WEB-DL DUAL 5.1')
counter = count()

for root, dirs, files in os.walk(caminho_getsize_stat):
    the_counter = next(counter)
    print(the_counter, 'Pasta Atual', root)

    for dir_ in dirs:
        print(' ', the_counter, 'DIR:', dir_)
    
    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print(' ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))


