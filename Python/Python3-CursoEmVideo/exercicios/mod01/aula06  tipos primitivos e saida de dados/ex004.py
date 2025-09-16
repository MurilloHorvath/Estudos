sub = '\033[4m'
limpa = '\033[m'

txt1 = input('Digite algo: ')
print('O tipo primitivo desse valor é {}{}{}'.format(sub,type(txt1),limpa))
print('Só tem espaços? {}{}{}'.format(sub,txt1.isspace(),limpa))
print('É um número? {}{}{}'.format(sub,txt1.isnumeric(),limpa))
print('É alfabético? {}{}{}'.format(sub,txt1.isalpha(),limpa))
print('É alfanumérico? {}{}{}'.format(sub,txt1.isalnum(),limpa))
print('Esta em maiúsculas? {}{}{}'.format(sub,txt1.isupper(),limpa))
print('Está em minúsculas? {}{}{}'.format(sub,txt1.islower(),limpa))
print('Está capitalizada? {}{}{}'.format(sub,txt1.istitle(),limpa))
