"""
Usamos a pathlib para trabalhar com caminhos, pastas e arquivos
de forma que um código funcione em Windows, Linux e Mac.
"""

from pathlib import Path

# Obtendo o caminho (raiz) absoluto com Path
caminho_projeto = Path()
print(caminho_projeto.absolute())

# Obtendo o caminho do arquivo atual com Path
caminho_arquivo = Path(__file__)
print(caminho_arquivo)

# Obtendo o caminho da pasta acima com parent
print(caminho_arquivo.parent.parent)

# Criando pastas e arquivos usando _truediv_ (barra)
ideias = caminho_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')

# Obtendo o caminho da pasta pessoal do usuário (home)
print(Path.home() / 'Desktop')

"""
Salvando um arquivo com touch
Apagando um arquivo com unlink
Escrevendo dados dentro de um arquivo (básico)
Lendo dados de um arquivo
Escrevendo dados dentro de um arquivo (avançado)
"""
arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
arquivo.touch()
# print(arquivo)
# arquivo.write_text('Olá mundo')
# print(arquivo.read_text())
# arquivo.unlink()
arquivo.write_text('')
with arquivo. open('a+') as file:
    file.write('Uma linha')

print(arquivo.read_text())

# Criando pastas com mkdir
caminho_pasta = Path.home() / 'Desktop' / 'Python'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey')

# Apagando uma pasta que tem conteúdo de forma recursiva

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    file.touch()

    if file.exists():
        file.unlink()
    else:
        file.touch()
    
    with file.open('a+') as text_file:
        text_file.write('Olá mundo')
        text_file.write(f'file_{i}.txt')

def rmtree(root: Path, remove_root = True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else: 
            print('FILE: ', file)
            file.unlink()
        
        if remove_root:
            root.rmdir()


rmtree(caminho_pasta)