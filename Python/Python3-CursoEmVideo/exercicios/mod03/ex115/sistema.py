from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'pessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        # Listar conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema.. Até logo!')
        break
    else:
        print(f'{cores("Vermelho")}ERRO! Digite uma Opção Válida!{cores("Limpa")}')
    sleep(1)
