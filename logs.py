from datetime import datetime

def registrar_log(mensagem):
    with open('logs.txt', 'a') as log:
        log.write(f'{datetime.now()} - {mensagem}\n')
