import random

class Personagem:
    
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = int(vida)
        self.__nivel = int(nivel)

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
       
    def exibir_detalhes(self):
        return ( f" \n Personagem: {self.get_nome()} \n Vida: {self.get_vida()} \n Nivel: {self.get_nivel()}")
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel()*2, self.get_nivel()*4)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade 

    def exibir_detalhes(self):
        return (f"{super().exibir_detalhes()} \n habilidade {self.get_habilidade()}")
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel()*3, self.get_nivel()*5) # Dano aumentado
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} executou um ataque especial no {alvo.get_nome()} e causou {dano} de dano")


class Inimigo(Personagem):
    
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return (f"{super().exibir_detalhes()} \n Tipo {self.get_tipo()}")
    

class Jogo():
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Superman", vida=100, nivel=5, habilidade="Super-Força")
        self.inimigo = Inimigo(nome="Coriga", vida=100, nivel=5, tipo="Malandro")

    def iniciar_batalha(self):
        print("Iniciando Batalha...")
        while self.heroi.get_vida() > 0 and  self.inimigo.get_vida() > 0:
            print("Detalhes dos Personagens: ")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione enter para atacar")
            print("Escolha uma opção: \n1- Ataque normal  \n2- Ataque especial \n  ")
            escolha = int(input("Digita a opção:"))

            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            elif escolha == 2:
                self.heroi.ataque_especial(self.inimigo)
            else:
                print(f"Não existe a opção {escolha}, tente novamente!")
            
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("Parabéns você venceu!")
        else: 
            print("Você perdeu!")   

jogo = Jogo()
jogo.iniciar_batalha()
