
def adicionar_tarefas(tarefas, nome_tarefa):
    tarefa = {"nome":nome_tarefa, "concluida":False}
    tarefas.append(tarefa)
    print(f"Tarefa {tarefa["nome"]} adicionada!")
    return 

def visualizar_tarefas(tarefas):
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else " "
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, numero_tarefa, nome_atualizado):
    indice_atualizado = int(numero_tarefa) -1
    if indice_atualizado >= 0 and indice_atualizado < len(tarefas):
        tarefas[indice_atualizado]["nome"] = nome_atualizado
        print(f"\nO nome da tarefa {numero_tarefa} atualizada para {nome_atualizado}")
    else: 
        print(f"Não existe a tarefa {numero_tarefa}")
    return

def completar_tarefa(tarefas, numero_tarefa):
    indice_atualizado = int(numero_tarefa) -1
    if indice_atualizado >= 0 and indice_atualizado < len(tarefas):
        tarefas[indice_atualizado]["concluida"] = True
        print(f"\nO nome da tarefa {numero_tarefa} concluída!")
    else:
        print(f"Não existe a tarefa {numero_tarefa}")
    
    return

def deletar_tarefa_concluidas(tarefas):
    for tarefa in tarefas:
        if tarefa["concluida"]:
            tarefas.remove(tarefa)
    return



tarefas = []
while True:
    print("\nEscolha o que você quer fazer:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar nome da tarefa")
    print("4. Concluir tarefa")
    print("5. Remover tarefas concluídas")
    print("6. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        print("-----CRIAR TAREFAS-----")
        tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefas(tarefas, tarefa)
    
    elif opcao == "2":
        print("-----LISTA DE TAREFAS-----")
        visualizar_tarefas(tarefas)

    elif opcao == "3":
        print("-----ATUALIZAR NOME DAS TAREFAS-----")
        visualizar_tarefas(tarefas)
        tarefa = input("Digite o número da tarefa que deseja ATUALIZAR: ")
        nome_atualizado = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, tarefa, nome_atualizado)
    
    elif opcao == "4":
        print("-----COMPLETAR TAREFAS-----")
        visualizar_tarefas(tarefas)
        tarefa = input("Digite o número da tarefa que deseja COMPLETAR: ")
        completar_tarefa(tarefas, tarefa)
    
    elif opcao == "5":
        deletar_tarefa_concluidas(tarefas)
        print("Tarefas concluídas deletadas")
        
    elif opcao == "6":
        print("Saindo do gerenciador de tarefas...")
        break

print("Programa finalizado")