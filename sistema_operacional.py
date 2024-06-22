# Sistema operacional baseado em linux.
import os 
import getpass
import platform
import time
from logs import registrar_log


# Criando uma função de cadastro e armazenando em um arquivo
def cadastro():
    cadastro_nome = input('Digite seu nome: ')
    cadastro_email = input('Crie seu email: ')
    cadastro_senha = getpass.getpass('Crie sua senha: ')

    # Armazenando os dados em um arquivo.
    with open('banco_de_dados.txt', 'a') as arquivo_1:
        arquivo_1.write(f'{cadastro_nome}:{cadastro_email}:{cadastro_senha}\n')

        # Verificando se ha um usuario cadastrado.
        if os.path.exists('banco_de_dados.txt'):
            with open('banco_de_dados.txt', 'r') as verificar:
                for linha in verificar:
                    partes = linha.strip().split(':')
                    if len(partes) == 3:
                        _, armazenamento_email, _ = partes
                        if armazenamento_email == cadastro_email:
                            print('Email ja existente. Tente novemente!')
                            registrar_log(f'Tentativa de cadastro com usuário existente para o email: {cadastro_email}')
                            return

        # Colocando tempo.
        print(f'Fazendo cadastro...')
        time.sleep(4)
        
        # Historico de logs do que acontece com aplicação
        registrar_log(f'Cadastro feito com sucesso para o email: {cadastro_email}')


# Criando Função de login
def login(email, senha):

    # Colocando uma condição de não passa na etapa, se caso não existe usuários
    if not os.path.exists('banco_de_dados.txt') or os.path.getsize('banco_de_dados.txt') == 0:
        print('Nenhum usuário cadastrado!')
        registrar_log('Tentiva de login invalido, por que não usuário cadastrado!')

    # Abrindo um banco de dados, para ler o banco de dados para identifiacar os usuários.    
    with open('banco_de_dados.txt', 'r') as arquivo_2:
        for linha in arquivo_2:
            partes = linha.strip().split(':')
            if len (partes) == 3:
                armazenando_nome, armazenado_email, armazenando_senha = partes
                if armazenado_email == email and armazenando_senha == senha:
                    print('Fanzendo Login...')
                    time.sleep(5)
                    registrar_log(f'login bem-sucedido para o email: {email}')
                return True
    return False

# comandos de linux.
def comandos():
    comandos = input(os.environ())
    os.system(comandos)


# comando de limpar terminal
def clear():
    limpar = platform.system()
    if limpar == 'Linux':
        os.system('clear')

# Criando uma função de com o usuario quiser sair vai ter 3 segundos, para o programa ser interrompido para quando o usuario quiser dessiste e volta ao programa.
def sair():
    for i in range(3, 0, -1):
        print(f'{i}')
        time.sleep(0.9)

# Criando Função para resetar o linux.
def resetar():
    with open('banco_de_dados.txt', 'w') as arquivo_3:
        arquivo_3.write('')
        registrar_log('Sistema resetado.')
        

# Fanzendo as aplicações funcionarem.
while True:
    print('1. Entrar em linux')
    print('2. Sair')
    print('3. Resetar')

    try:
        escolha = input('\nDigite um opção: ')
        if escolha == '1':
            pergunta = input('\nVocê tem conta em linux S/N: ')

            if pergunta in ('N', 'n'):
                print('\nFaça seu cadastro aqui!\n')

                cadastro()
            elif pergunta in ('S', 's'):
                print('\nFaça seu login!\n')

                login_email = input('Digite seu email: ')
                login_senha = getpass.getpass('Digite sua senha: ')
                if login(login_email, login_senha):
                    print('Login feito com sucesso')
                    print('Entrando em linux...')
                    time.sleep(4)
                    comandos()
                else:
                    print('usuário ou senha incorreto!')
        elif escolha == '2':
            print('Saindo...')
            registrar_log('Encerrando programa!')
            sair()
            exit()
        elif escolha == 'clear':
            clear()
        elif escolha == '3':
            email = input('Digite seu email: ')
            senha = getpass.getpass('Digite sua senha: ')
            pergunta_1 = input('Você tem certeza que quer resetar o linux S/N: ')
            if pergunta_1 in ('S', 's'):
                if login(email, senha):
                    print('Apagando Tudo...')
                    time.sleep(3)
                    resetar()
            elif pergunta_1 in ('N', 'n'):
                print('cancelando...')
                time.sleep(3)
    except(KeyboardInterrupt):
        print('\n\nProcesso interrompido pelo usuário :(\n', )
        registrar_log('Processo interrompido!')
        continue
