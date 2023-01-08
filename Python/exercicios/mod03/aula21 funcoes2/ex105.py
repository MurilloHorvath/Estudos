def notas(*n,sit=False):
    '''
    -> Função para analisar notas e sua (opcional) Situação
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    boletim = dict()
    boletim['Quantidade de Notas'] = len(n)
    boletim['Maior Nota'] = max(n)
    boletim['Menor Nota'] = min(n)
    boletim['Média'] = sum(n)/len(n)
    if sit:
        if boletim['Média']>=7:
            boletim['Situação'] = 'Boa'
        elif boletim['Média']>=5:
            boletim['Situação'] = 'Razoável'
        else:
            boletim['Situação'] = 'Ruim'
    return boletim

resp = notas(5.6,7,8,7.5,sit=True)
print(resp)
help(notas)
