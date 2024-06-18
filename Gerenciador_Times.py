times = []

def adicionar_times():
    while True:
        try:
            nome_time = str(input('Qual o nome do time?: '))
            if nome_time.isdigit():
                raise ValueError('O nome do time precisa conter pelo menos uma letra!.')
            break
        except ValueError as e:
            print(e)
    dic = {'Time': nome_time, 'Nome Jogador': ' ', 'Jogadores': 0}
    times.append(dic)
    print('Time adicionado com sucesso!. ')
    return times

def remover_times():
    listar_times()
    while True:
        try:
            indice_time = int(input('Digite o índice do time que deseja remover: '))
            if 0 <= indice_time < len(times):
                times.pop(indice_time)
                print('Time removido com sucesso!')
                break
            else:
                print('Índice inválido')
        except ValueError:
            print('Digite apenas numeros')
                
def listar_times():
    if times:
        for i, v in enumerate(times):
            print(f'{i} - {v['Time']} - {v['Jogadores']} jogadores')
    else:
        print('Nem um time/jogador cadastrados.')

def adicionar_jogador():
    listar_times()
    while True:
        try:
            indice_time = int(input('Digite o índice do time que deseja adicionar o jogador: '))
            if 0 <= indice_time < len(times):
                times[indice_time]['Nome Jogador'] = str(input('Digite o nome do jogador para adicionar: '))
                times[indice_time]['Jogadores'] += 1
                print('Jogador adicionado com sucesso')
                break
            else:
                print('Índice não localizado')
        except ValueError:
            print('Digite apenas números')
    
def remover_jogador():
    listar_times()
    while True:
        try:
            indice_time = int(input('Digite o índice do time que deseja adicionar o jogador: '))
            if 0 <= indice_time < len(times):
                    times[indice_time]['Nome Jogador'] = str(input('Qual o nome do jogador que deseja remover ?: '))
                    times[indice_time]['Jogadores'] -= 1
                    del times[indice_time]['Nome Jogador']
                    print('Jogador removido com sucesso.')
                    break
            else:
                print('Indice não encontrado')
        except ValueError:
            print('Digite apenas números')
            
def listar_jogadores():
    listar_times()
    while True:
        try:
            indice_time = int(input('Digite o índice do time que deseja ver os jogadores: '))
            if 0 <= indice_time < len(times):
                print(f'{indice_time} - {times[indice_time]['Nome Jogador']}')
                break
            else:
                print('Indice não encontrado')
        except ValueError:
            print('Digite apenas numeros')
            
while True:
    print("""
    [1] Adicionar um time
    [2] Remover um time
    [3] Listar times
    [4] Adicionar jogador em um time
    [5] Remover jogador de um time
    [6] Listar jogadores de um time
    [7] Sair
""")
    
    opc = int(input('Escolha uma opção: '))

    if opc == 1:
        adicionar_times()
    elif opc == 2:
        remover_times()
    elif opc == 3:
        listar_times()
    elif opc == 4:
        adicionar_jogador()
    elif opc == 5:
        remover_jogador()
    elif opc == 6:
        listar_jogadores()
    elif opc == 7:
        break
    else: 
        print('Opção inválida')