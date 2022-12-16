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

    novo_contato = ler_contato()
    mini_agenda.write(novo_contato)


    
