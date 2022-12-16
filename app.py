# Inicializa a mini-agenda

def inicializa_agenda(nome_arquivo = 'agenda.txt'):
    try:
        f = open(nome_arquivo, 'w')
    except:
        print(f'Erro! Não foi póssivel iniciar o aquivo {nome_arquivo}')    

    return nome_arquivo

# Ler um contato

def ler_contato():
    id_contato = input('Id: ')
    nome_contato = input('Nome: ')

    contato = (id_contato, nome_contato)

    return contato
        