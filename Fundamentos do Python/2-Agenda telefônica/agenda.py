def salvar_contato(contatos):
    contato = {"nome":"", "telefone":"", "email":"", "favorito":False}
    contato["nome"]  = input("digite o nome: ")
    contato["telefone"] = input("digite o telefone: ")
    contato["email"] = input("digite o email: ")
    contatos.append(contato)
    print("Contato salvo!")
    return

def visualizar_contatos(contatos):
    if len(contatos) == 0:
        print("Nenhum contato cadastrado!")
        return
    for indice, contato in enumerate(contatos):
        favorito = "☆" if contato["favorito"] else ""
        print(f"\n{indice+1}. {contato["nome"]} {favorito}")
        print(f"Telefone: {contato["telefone"]}")
        print(f"Email: {contato["email"]}")
    return

def editar_contato(contatos):

    if len(contatos) == 0:
        print("Nenhum contato cadastrado!")
        return

    visualizar_contatos(contatos)

    contato_escolhido = input("Digite o número do contato que deseja EDITAR: ")

    try:
        indice_do_contato = int(contato_escolhido) - 1
    except ValueError:
        print("Digite um número válido!")
        return

    if indice_do_contato >= 0 and indice_do_contato < len(contatos):
        contato = contatos[indice_do_contato]

        print(f"\nEditando contato: {contato['nome']}")
        print("Deixe em branco e dê enter para manter o valor atual.") 

        novo_nome = input(f"Novo nome ({contato['nome']}): ")
        novo_telefone = input(f"Novo telefone ({contato['telefone']}): ")
        novo_email = input(f"Novo email ({contato['email']}): ")

        if novo_nome != "":
            contato["nome"] = novo_nome

        if novo_telefone != "":
            contato["telefone"] = novo_telefone

        if novo_email != "":
            contato["email"] = novo_email

        print("Contato editado com sucesso!")

    else:
        print("Contato inválido!")

    return

def deletar_contato(contatos):
    if len(contatos) == 0:
        print("Nenhum contato cadastrado!")
        return

    visualizar_contatos(contatos)

    contato_escolhido = input("Digite o número do contato que deseja EXCLUIR: ")

    try:
        indice_do_contato = int(contato_escolhido) - 1
    except ValueError:
        print("Digite um número válido!")
        return

    if 0 <= indice_do_contato < len(contatos):
        contatos.pop(indice_do_contato)
        print("Contato excluído com sucesso!")
    else:
        print("Contato não encontrado!")
    
def favoritar_contatos(contatos):

    if len(contatos)==0:
        print("Não exite contatos salvos")
        return
    
    visualizar_contatos(contatos)
    contato_escolhido = int(input("Qual contato deseja favoritar/desfavoritar ")) - 1
    
    try:
        print("----Contatos Favoritos---")
        if contato_escolhido >= 0 and contato_escolhido < len(contatos):
            if contatos[contato_escolhido]["favorito"]:
                contatos[contato_escolhido]["favorito"] = False
                print(f"Contato {contatos[contato_escolhido]["nome"]} desavoritado")
            else:
                contatos[contato_escolhido]["favorito"] = True
                print(f"Contato {contatos[contato_escolhido]["nome"]} Favoritado")
        
    except ValueError as e:
        print(f"O contato {contato_escolhido +1} não existe")
    return

def listar_favoritos(contatos):
    indice = 0
    for contato in contatos:
        if contato["favorito"]:
           indice += 1
           print(f"\n {indice}. {contato["nome"]} ☆")
           print(f"Telefone: {contato["telefone"]}")
           print(f"Email: {contato["email"]}")

    return     
        

contatos = []

while True:
    print("\n1. Salvar Contato")
    print("2. Visualizar Contatos Salvos")
    print("3. Editar Contato")
    print("4. Favoritar/Desfavoritar Contatos")
    print("5. Lista de Favoritos")
    print("6. Deletar Contato")
    print("7. Sair da aplicação")

    opcao = input("Digite o número da opcão: ")

    if opcao == "1":
        print("---- Salvar Contato -----")
        salvar_contato(contatos)

    elif opcao == "2":
        print("---- Visualizar contatos salvos -----")
        visualizar_contatos(contatos)

    elif opcao == "3":
        print("---- Editar contato -----")
        editar_contato(contatos)

    elif opcao == "4":
        print("---- Favoritar/Desfavoritar contato -----")
        favoritar_contatos(contatos)
   
    elif opcao == "5":
        listar_favoritos(contatos)

    elif opcao == "6":
        deletar_contato(contatos)

    elif opcao == "7":
        print("saindo...")
        print("Aplicação encerrada!")
        break
    