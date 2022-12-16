# Inicializa a mini-agenda
def inicializa_agenda(nome_arquivo):
    try:
        mini_agenda = open(nome_arquivo, 'w')
    except:
        print(f'Erro! Não foi póssivel iniciar o aquivo {nome_arquivo}')    

    return nome_arquivo

# Ler um contato
def ler_contato():
    id_contato = input('Id: ')
    nome_contato = input('Nome: ')

    tupla_contato = (id_contato, nome_contato)

    contato = contato[0] + ', ' + contato[1] + '\n'

    return contato

# Insere um novo contato
def insere_contato(contato, nome_arquivo):    
    mini_agenda = open(nome_arquivo, 'a')
    mini_agenda.write(contato)
    mini_agenda.close()

# Lista todos os contatos salvos no arquivo
def listar_contatos(nome_arquivo):
    mini_agenda = open(nome_arquivo, 'r')
    if len(mini_agenda) == 0:
        print('0 contatos registrados!')
    
    for linha in mini_agenda:
        print(linha, end='')

    mini_agenda.close()    

def mostra_menu():            
    print('--- Bem vindo a mini-agenda ---')
    print('1 - Mostrar os contatos registrados')
    print('2 - Insere um novo contato')
    print('3 - Sair')




    
