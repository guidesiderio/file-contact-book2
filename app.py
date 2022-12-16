import os

# Inicializa a mini-agenda
def inicializa_agenda(nome_arquivo = 'agenda.txt'):
    try:
        mini_agenda = open(nome_arquivo, 'a')
    except:
        print(f'Erro! Não foi póssivel iniciar o aquivo {nome_arquivo}')   
        print() 

    return nome_arquivo

# Lê um contato
def ler_contato():
    id_contato = input('Id: ')
    nome_contato = input('Nome: ')
    print()

    tupla_contato = (id_contato, nome_contato)

    contato = tupla_contato[0] + ', ' + tupla_contato[1] + '\n'

    return contato

# Insere um novo contato no arquivo
def insere_contato(contato, nome_arquivo):    
    mini_agenda = open(nome_arquivo, 'a')
    mini_agenda.write(contato)
    mini_agenda.close()

# Lista todos os contatos salvos no arquivo
def listar_contatos(nome_arquivo):
    mini_agenda = open(nome_arquivo, 'r')
    if os.path.getsize(nome_arquivo) == 0:
        print('0 contato registrado!')
    
    for linha in mini_agenda:
        print(linha, end='')

    print()    

    mini_agenda.close()    

# Menu de opções
def mostra_menu():            
    print('--- Bem vindo a mini-agenda ---')
    print('1 - Mostrar os contatos registrados')
    print('2 - Insere um novo contato')
    print('3 - Sair')
    print()

# Aplicação
nome_arquivo = inicializa_agenda()
mostra_menu()    
ler_opcao = input('Qual a opção? ')
opcao = int(ler_opcao)
while(opcao != 3):
    if opcao == 1:
        print('# Lista de contatos #')
        listar_contatos(nome_arquivo)
    if opcao == 2:
        print('# Novo contato #')
        contato = ler_contato()
        insere_contato(contato, nome_arquivo)   
    mostra_menu()    
    ler_opcao = input('Qual a opção? ')
    opcao = int(ler_opcao)     
