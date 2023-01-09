from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'{cores("Vermelho")}Houve um ERRO na criação do arquivo!{cores("Limpa")}')
    else:
        print(f'{cores("Verde")}Arquivo {nome} criado com sucesso{cores("Limpa")}')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'{cores("Vermelho")}Erro ao ler arquivo!{cores("Limpa")}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'{cores("Vermelho")}Houve um ERRO na abertura do arquivo!{cores("Limpa")}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'{cores("Vermelho")}Houve um ERRO na hora de escrever os dados{cores("Limpa")}')
        else:
            print(f'{cores("Verde")}Novo registro de {nome} adicionado.{cores("Limpa")}')
            a.close()