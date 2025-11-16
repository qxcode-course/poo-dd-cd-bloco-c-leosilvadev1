class Crianca:
    def __init__(self, nome: str, idade : int):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}:{self.idade}"

class Pula:
    def __init__(self):
        self.espera: list[Crianca] = []
        self.pulapula: list[Crianca] = []

    def arrive(self, nome: str, idade: int):
        self.espera.insert(0, Crianca(nome, idade))

    def enter(self):
        if self.espera:
            crianca = self.espera.pop()
            self.pulapula.insert(0, crianca)
        else:
            print("Não há ninguem")

    def leave(self):
        if self.pulapula:
            crianca = self.pulapula.pop()
            self.espera.insert(0, crianca)

    def remove(self,nome : str):
        for i, c in enumerate(self.espera):
            if c.nome == nome:
                del self.espera[i]
                return

        for i, c in enumerate(self.pulapula):
            if c.nome == nome:
                del self.pulapula[i]
                return

        print(f"fail: {nome} nao esta no pula-pula")

    def __str__(self):
        espera = ", ".join([str(c) for c in self.espera])

        pulapula = ", ".join([str(c) for c in self.pulapula])

        return f"[{espera}] => [{pulapula}]"

def main():
    pula = Pula()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pula)
        elif args[0] == "leave":
            pula.leave()
        elif args[0] == "remove":
            pula.remove(args[1])
        elif args [0] == "arrive":
            pula.arrive(args[1], int(args[2]))
        elif args[0] == "enter":
            pula.enter()
main()