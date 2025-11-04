class Pessoa:
    def __init__(self, nome : str):
        self.nome : str = nome

    def __str__(self):
        return self.nome

class Budega:
    def __init__(self, num_caixas : int):
        self.espera : list[Pessoa] = []
        self.caixas : list[Pessoa | None] = []

        for i in range(num_caixas):
            self.caixas.append(None)

    def arrive(self, pessoa : Pessoa):
        self.espera.append(pessoa)

    def call(self, index : int):
        if index < 0 or index >= len(self.caixas):
            print("Index inexistente")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        self.caixas[index] = self.espera[0]
        del self.espera[0]

    def finish(self, index : int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return
        self.caixas[index] = None

    def give_up(self, nome : str):
        for i, pessoa in enumerate(self.espera):
            if pessoa.nome == nome: 
                aux = self.espera[i]
                del self.espera[i]
                return aux
        return None

    def __str__(self):
        caixas = ", ".join(["-----" if x is None
                            else str(x) for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])

        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

def main():
    budega : Budega | None = None
    while True:
        line  = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        if args[0] == "init":
            num = int(args[1])
            budega = Budega(num)

        elif args[0] == "arrive":
            if budega is not None:
                nome = args[1]
                budega.arrive(Pessoa(nome))
            else:
                print("fail: budega não iniciada")

        elif args[0] == "call":
            if budega is not None:
                index = int(args[1])
                budega.call(index)
            else:   
                print("fail: budega não iniciada")

        elif args[0] == "finish":
            if budega is not None:
                index = int(args[1])
                budega.finish(index)
            else:
                print("fail: budega não iniciada")

        elif args[0] == "show":
            print(budega)
                

main()